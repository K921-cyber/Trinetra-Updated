import logging
from app.plugins.base import OSINTPlugin, PluginResult
import httpx
import hashlib

logger = logging.getLogger(__name__)


class EmailFinderPlugin(OSINTPlugin):
    plugin_id = "email-finder"
    name = "Email Finder"
    category = "person"
    description = "Email profile detection on 20+ platforms via EmailRep + direct checks"
    input_types = ["email"]
    icon = "📧"

    # Services to check for email registration.
    # Format: (display_name, url, method, payload_attr, response_check)
    # response_check: if callable, gets called with the response; if string, checked as substring
    REGISTRATION_CHECKS = [
        ("GitHub",       "https://api.github.com/search/users?q={email}+in:email", "GET", None,
         lambda r: r.json().get("total_count", 0) > 0),
        ("Twitter/X",    "https://api.twitter.com/i/users/email_available.json", "POST",
         {"email": "{email}"}, lambda r: r.status_code != 200),
        ("Spotify",      "https://www.spotify.com/api/signup/checkEmail", "POST",
         {"email": "{email}"}, lambda r: r.status_code != 200),
        ("Adobe",        "https://auth.services.adobe.com/signup/v2/users/check", "POST",
         {"email": "{email}"}, lambda r: r.status_code != 200),
        ("WordPress.com","https://public-api.wordpress.com/rest/v1.1/users/{email}/posts", "GET", None,
         lambda r: r.status_code == 200),
        ("Disqus",       "https://disqus.com/api/3.0/users/details.json?email={email}", "GET", None,
         lambda r: r.status_code == 200),
        ("Pinterest",    "https://www.pinterest.com/resource/UserEmailExistsResource/get/", "GET",
         {"email": "{email}"}, lambda r: "true" in r.text.lower()),
        ("Tumblr",       "https://www.tumblr.com/svc/account/register", "POST",
         {"email": "{email}"}, lambda r: "already" in r.text.lower()),
        ("Flickr",       "https://identity.flickr.com/checkusername", "POST",
         {"email": "{email}"}, lambda r: r.status_code != 200),
        ("Imgur",        "https://imgur.com/signin", "POST",
         {"email": "{email}"}, lambda r: "find your account" in r.text.lower()),
        ("Mixcloud",     "https://www.mixcloud.com/check_email/", "POST",
         {"email": "{email}"}, lambda r: "taken" in r.text.lower() or "exists" in r.text.lower()),
        ("Twitch",       "https://www.twitch.tv/accounts/check_availability", "POST",
         {"email": "{email}"}, lambda r: r.status_code != 200),
        ("Medium",       "https://medium.com/_/api/users/email/available", "POST",
         {"email": "{email}"}, lambda r: not r.json().get("available", True)),
        ("HackerNews",   "https://news.ycombinator.com/x", "POST",
         {"email": "{email}"}, lambda r: "already taken" in r.text.lower()),
        ("Keybase",      "https://keybase.io/_/api/1.0/user/lookup.json?email={email}", "GET", None,
         lambda r: r.status_code == 200 and "them" not in r.text.lower()),
        ("BitBucket",    "https://bitbucket.org/api/2.0/user/email/{email}", "GET", None,
         lambda r: r.status_code != 404),
        ("Telegram",     "https://oauth.telegram.org/auth/check_email", "POST",
         {"email": "{email}"}, lambda r: "exists" in r.text.lower()),
        ("Quora",        "https://www.quora.com/main/email_available", "POST",
         {"email": "{email}"}, lambda r: not r.json().get("available", True)),
        ("Reddit",       "https://www.reddit.com/api/check-email", "POST",
         {"email": "{email}"}, lambda r: not r.json().get("is_available", True)),
    ]

    async def run(self, target: str) -> PluginResult:
        email = target.strip().lower()
        domain = email.split("@")[1] if "@" in email else "N/A"
        md5_hash = hashlib.md5(email.encode()).hexdigest()

        results = {}
        profiles_found = []

        # --- PART 1: EmailRep.io intelligence ---
        emailrep_data = {}
        try:
            async with httpx.AsyncClient(timeout=8) as client:
                resp = await client.get(
                    f"https://emailrep.io/{email}",
                    headers={
                        "User-Agent": "TRINETRA-OSINT/1.0",
                        "Accept": "application/json",
                    },
                )
                if resp.status_code == 200:
                    emailrep_data = resp.json()
        except Exception as e:
            logger.debug("EmailRep lookup failed for %s: %s", email, e)

        if emailrep_data:
            rep = emailrep_data.get("reputation", "unknown")
            suspicious = emailrep_data.get("suspicious", False)
            leaked = emailrep_data.get("details", {}).get("credentials_leaked", False)
            profiles = emailrep_data.get("details", {}).get("profiles", [])
            results["EmailRep Reputation"] = rep.capitalize()
            results["Suspicious"] = "Yes" if suspicious else "No"
            results["Credentials Leaked"] = "Yes" if leaked else "No"
            if profiles:
                results["EmailRep Profiles"] = ", ".join(profiles[:8])
                profiles_found.extend(profiles)

        # --- PART 2: Gravatar lookup ---
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                resp = await client.get(
                    f"https://www.gravatar.com/{md5_hash}.json",
                    headers={"User-Agent": "TRINETRA-OSINT/1.0"},
                )
                if resp.status_code == 200:
                    data = resp.json()
                    entry = data.get("entry", [{}])[0]
                    display_name = entry.get("displayName", "")
                    location = entry.get("currentLocation", "")
                    photos = entry.get("photos", [])
                    avatar_url = photos[0].get("value", "") if photos else ""
                    if display_name:
                        results["Gravatar Name"] = display_name
                    if location:
                        results["Gravatar Location"] = location
                    profiles_found.append("Gravatar")
        except Exception as e:
            logger.debug("Gravatar lookup failed for %s: %s", email, e)

        # --- PART 3: Service registration checks ---
        services_found = []
        services_not_found = []
        services_error = []

        for check in self.REGISTRATION_CHECKS:
            name, url, method, payload, check_fn = check
            try:
                async with httpx.AsyncClient(timeout=5) as client:
                    processed_url = url.replace("{email}", email).replace("{md5}", md5_hash)
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                        "Accept": "application/json, text/plain, */*",
                    }
                    if payload:
                        processed_payload = {k: v.replace("{email}", email) for k, v in payload.items()}
                        if method == "POST":
                            resp = await client.post(processed_url, json=processed_payload, headers=headers, follow_redirects=True)
                        else:
                            resp = await client.get(processed_url, params=processed_payload, headers=headers, follow_redirects=True)
                    else:
                        if method == "POST":
                            resp = await client.post(processed_url, headers=headers, follow_redirects=True)
                        else:
                            resp = await client.get(processed_url, headers=headers, follow_redirects=True)

                    try:
                        is_found = check_fn(resp)
                    except Exception as e:
                        logger.debug("Service check %s failed for %s: %s", name, email, e)
                        is_found = False

                    if is_found:
                        services_found.append(name)
                        profiles_found.append(name)
                    else:
                        services_not_found.append(name)
            except Exception as e:
                logger.debug("Service %s request failed for %s: %s", name, email, e)
                services_error.append(name)

        profiles_found = list(dict.fromkeys(profiles_found))  # deduplicate

        # --- Build GUI data ---
        gui_data = {
            "Email": email,
            "Domain": domain,
            "Profiles Found": len(profiles_found),
            "Profile List": ", ".join(profiles_found[:12]) if profiles_found else "None detected",
        }

        if emailrep_data:
            gui_data["EmailRep Reputation"] = results.get("EmailRep Reputation", "Unknown")
            gui_data["Credentials Leaked"] = results.get("Credentials Leaked", "Unknown")
        if "Gravatar Name" in results:
            gui_data["Gravatar Name"] = results["Gravatar Name"]
        if "Gravatar Location" in results:
            gui_data["Gravatar Location"] = results["Gravatar Location"]

        gui_data["Services Found"] = len(services_found)
        if services_found:
            gui_data["Registered On"] = ", ".join(services_found[:10])
        gui_data["Services Checked"] = len(self.REGISTRATION_CHECKS) + 2  # REGISTRATION_CHECKS + EmailRep + Gravatar
        gui_data["Status"] = "Profile scan complete"

        # --- Build terminal output ---
        terminal = f"""[+] Email intelligence for: {email}
[+] Domain: {domain}
[+] Profiles Found: {len(profiles_found)}
"""
        if profiles_found:
            terminal += "[+] Profile list:\n"
            for p in profiles_found[:12]:
                terminal += f"    ├ {p}\n"
        if emailrep_data:
            rep = emailrep_data.get("reputation", "unknown")
            leaked = emailrep_data.get("details", {}).get("credentials_leaked", False)
            terminal += f"[+] EmailRep reputation: {rep}\n"
            terminal += f"[+] Credentials leaked: {'YES' if leaked else 'No'}\n"
        if services_found:
            terminal += f"[!] Registered on {len(services_found)} service(s): {', '.join(services_found[:10])}\n"
        if services_not_found:
            terminal += f"[i] Not found on {len(services_not_found)} service(s)\n"
        if services_error:
            terminal += f"[!] {len(services_error)} service(s) could not be checked (timeout/blocked)\n"

        return PluginResult(
            plugin_id=self.plugin_id,
            plugin_name=self.name,
            category=self.category,
            target=target,
            gui_data=gui_data,
            terminal_data=terminal,
        )
