import logging
from app.plugins.base import OSINTPlugin, PluginResult
import httpx

logger = logging.getLogger(__name__)


class UsernameTrackerPlugin(OSINTPlugin):
    plugin_id = "username-tracker"
    name = "Username Tracker"
    category = "person"
    description = "Username presence on multiple platforms"
    input_types = ["username"]
    icon = "👤"

    PLATFORMS = {
        "GitHub": "https://github.com/{username}",
        "Twitter/X": "https://twitter.com/{username}",
        "Instagram": "https://www.instagram.com/{username}/",
        "Reddit": "https://www.reddit.com/user/{username}",
        "Medium": "https://medium.com/@{username}",
        "Dev.to": "https://dev.to/{username}",
        "HackerNews": "https://news.ycombinator.com/user?id={username}",
        "Keybase": "https://keybase.io/{username}",
        "Telegram": "https://t.me/{username}",
    }

    async def run(self, target: str) -> PluginResult:
        found = []

        async with httpx.AsyncClient(timeout=5, follow_redirects=True) as client:
            for platform, url_tpl in self.PLATFORMS.items():
                url = url_tpl.replace("{username}", target)
                try:
                    resp = await client.head(url, headers={"User-Agent": "Mozilla/5.0"})
                    if resp.status_code < 400:
                        found.append({"platform": platform, "url": url, "status": resp.status_code})
                except Exception as e:
                    logger.debug("Username check failed for %s on %s: %s", target, platform, e)
                    continue

        gui_data = {
            "Username": target,
            "Platforms Found": len(found),
            "Platforms Checked": len(self.PLATFORMS),
        }

        for f in found:
            gui_data[f["platform"]] = f"✓ Found — {f['url']}"

        terminal_lines = [f"Username: {target}", f"Found on {len(found)}/{len(self.PLATFORMS)} platforms", "---"]
        for f in found:
            terminal_lines.append(f"  [{f['status']}] {f['platform']}: {f['url']}")

        return PluginResult(
            plugin_id=self.plugin_id,
            plugin_name=self.name,
            category=self.category,
            target=target,
            gui_data=gui_data,
            terminal_data="\n".join(terminal_lines),
        )
