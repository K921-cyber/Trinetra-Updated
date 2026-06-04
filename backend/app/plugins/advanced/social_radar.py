import logging
from app.plugins.base import OSINTPlugin, PluginResult
import httpx

logger = logging.getLogger(__name__)


class SocialRadarPlugin(OSINTPlugin):
    plugin_id = "social-radar"
    name = "Social Radar"
    category = "advanced"
    description = "Social media footprint, cross-platform presence"
    input_types = ["username", "name", "email"]
    icon = "📊"

    SOCIAL_SITES = {
        "LinkedIn": "https://www.linkedin.com/in/{username}",
        "Twitter/X": "https://twitter.com/{username}",
        "Facebook": "https://www.facebook.com/{username}",
        "Instagram": "https://www.instagram.com/{username}/",
        "YouTube": "https://www.youtube.com/@{username}",
        "Reddit": "https://www.reddit.com/user/{username}",
        "GitHub": "https://github.com/{username}",
        "Medium": "https://medium.com/@{username}",
    }

    async def run(self, target: str) -> PluginResult:
        found = []
        not_found = []

        async with httpx.AsyncClient(timeout=5, follow_redirects=True) as client:
            for site, url_tpl in self.SOCIAL_SITES.items():
                url = url_tpl.replace("{username}", target)
                try:
                    resp = await client.head(url, headers={"User-Agent": "Mozilla/5.0"})
                    if resp.status_code < 400:
                        found.append(site)
                    else:
                        not_found.append(site)
                except Exception as e:
                    logger.debug("Social check failed for %s on %s: %s", target, site, e)
                    not_found.append(site)

        score = round((len(found) / len(self.SOCIAL_SITES)) * 100)

        gui_data = {
            "Target": target,
            "Profiles Found": len(found),
            "Social Score": f"{score}%",
            "Platforms Checked": len(self.SOCIAL_SITES),
            "Found On": ", ".join(found) if found else "None",
        }

        terminal = f"""Social Radar Report — {target}
Profiles Found: {len(found)}/{len(self.SOCIAL_SITES)}
Social Score: {score}%
---
Found: {', '.join(found) if found else 'None'}
Not found: {', '.join(not_found) if not_found else 'None'}"""

        return PluginResult(
            plugin_id=self.plugin_id,
            plugin_name=self.name,
            category=self.category,
            target=target,
            gui_data=gui_data,
            terminal_data=terminal,
        )
