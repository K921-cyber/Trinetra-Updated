from app.plugins.base import OSINTPlugin, PluginResult
import asyncio


class ReverseDNSPlugin(OSINTPlugin):
    plugin_id = "reverse-dns"
    name = "Reverse DNS"
    category = "infrastructure"
    description = "PTR records, reverse lookups"
    input_types = ["ip"]
    icon = "🔄"

    async def run(self, target: str) -> PluginResult:
        try:
            import socket
            loop = asyncio.get_event_loop()
            hostname = await loop.run_in_executor(None, lambda: socket.gethostbyaddr(target))
            ptr_name = hostname[0] if hostname else "N/A"

            gui_data = {
                "IP": target,
                "PTR Record": ptr_name,
                "Hostname": ptr_name,
                "Aliases": ", ".join(hostname[1]) if hostname and len(hostname) > 1 else "None",
            }

            terminal = f"""IP: {target}
PTR: {ptr_name}
Aliases: {', '.join(hostname[1]) if hostname and len(hostname) > 1 else 'None'}"""

            return PluginResult(
                plugin_id=self.plugin_id,
                plugin_name=self.name,
                category=self.category,
                target=target,
                gui_data=gui_data,
                terminal_data=terminal,
            )
        except Exception as e:
            return PluginResult(
                plugin_id=self.plugin_id,
                plugin_name=self.name,
                category=self.category,
                target=target,
                gui_data={"IP": target, "PTR Record": "Not found"},
                terminal_data=f"IP: {target}\nPTR: Not found\nError: {e}",
            )
