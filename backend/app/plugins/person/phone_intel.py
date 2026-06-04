import logging
from app.plugins.base import OSINTPlugin, PluginResult
import re

logger = logging.getLogger(__name__)


class PhoneIntelPlugin(OSINTPlugin):
    plugin_id = "phone-intel"
    name = "Phone Intel"
    category = "person"
    description = "Carrier info, location, line type"
    input_types = ["phone"]
    icon = "📱"

    # Indian mobile carrier prefixes (first 2 digits after removing country code).
    # Based on original GSM allocation by DoT. Note: Mobile Number Portability (MNP)
    # means the actual carrier may differ — this is the best estimate without an API.
    CARRIER_PREFIXES: dict[str, list[str]] = {
        "Airtel": ["99", "88", "89", "90", "91", "92", "93"],
        "Jio":     ["98", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87"],
        "Vi":      ["63", "64", "65", "66", "67", "68", "69", "60", "61", "62"],
        "BSNL":    ["94", "95", "97"],
        "Others":  ["96"],  # 96-series was allocated to multiple operators
    }

    # Indian state/UT codes (first 2 digits of STD code) → approximate mapping
    LOCATION_MAP: dict[str, str] = {
        "11": "Delhi",
        "12": "Uttar Pradesh",
        "13": "Uttar Pradesh",
        "14": "Rajasthan",
        "15": "Rajasthan",
        "16": "Punjab, Haryana",
        "17": "Himachal, Punjab",
        "18": "Punjab, Jammu",
        "19": "Jammu & Kashmir",
        "20": "Maharashtra",
        "21": "Maharashtra",
        "22": "Maharashtra",
        "23": "Maharashtra",
        "24": "Maharashtra",
        "25": "Maharashtra",
        "26": "Gujarat",
        "27": "Gujarat",
        "28": "Gujarat",
        "29": "Rajasthan",
        "30": "Rajasthan, MP",
        "31": "Uttarakhand",
        "32": "Uttarakhand",
        "33": "West Bengal",
        "34": "West Bengal",
        "35": "West Bengal",
        "36": "Assam, Northeast",
        "37": "Assam, Northeast",
        "38": "Assam, Northeast",
        "39": "Assam, Northeast",
        "40": "Telangana",
        "41": "Tamil Nadu",
        "42": "Tamil Nadu",
        "43": "Tamil Nadu",
        "44": "Tamil Nadu (Chennai)",
        "45": "Tamil Nadu",
        "46": "Tamil Nadu",
        "47": "Kerala",
        "48": "Kerala",
        "49": "Kerala",
        "50": "Andhra Pradesh",
        "51": "Andhra Pradesh",
        "52": "Andhra Pradesh",
        "53": "Andhra Pradesh",
        "54": "Madhya Pradesh",
        "55": "Madhya Pradesh",
        "56": "Madhya Pradesh",
        "57": "Madhya Pradesh",
        "58": "Madhya Pradesh",
        "59": "Madhya Pradesh",
        "60": "Karnataka",
        "61": "Karnataka",
        "62": "Karnataka",
        "63": "Karnataka",
        "64": "Karnataka",
        "65": "Karnataka",
        "66": "Karnataka",
        "67": "Karnataka",
        "68": "Karnataka",
        "69": "Karnataka",
        "70": "Maharashtra",
        "71": "Maharashtra",
        "72": "Maharashtra",
        "73": "Maharashtra",
        "74": "Maharashtra",
        "75": "Madhya Pradesh",
        "76": "Madhya Pradesh",
        "77": "Chhattisgarh",
        "78": "Chhattisgarh",
        "79": "Gujarat",
        "80": "Karnataka",
        "81": "Karnataka",
        "82": "Karnataka",
        "83": "Karnataka, Goa",
        "84": "Andhra Pradesh",
        "85": "Andhra Pradesh",
        "86": "Andhra Pradesh",
        "87": "Punjab, Haryana",
        "88": "West Bengal",
        "89": "West Bengal",
    }

    def _infer_carrier(self, cleaned: str) -> str:
        """Infer Indian mobile carrier from number prefix."""
        # Remove country code
        local = cleaned
        if local.startswith("+91"):
            local = local[3:]
        elif local.startswith("91"):
            local = local[2:]
        elif local.startswith("0"):
            local = local[1:]

        # Take first 2 digits after STD/operator code
        prefix = local[:2] if len(local) >= 2 else ""

        for carrier, prefixes in self.CARRIER_PREFIXES.items():
            if prefix in prefixes:
                return carrier

        # Check by length — valid mobile numbers in India are 10 digits
        if len(local) == 10:
            return "Unknown Indian Carrier"

        return "Unknown"

    def _infer_location(self, cleaned: str) -> str:
        """Infer approximate location from number."""
        local = cleaned
        if local.startswith("+91"):
            local = local[3:]
        elif local.startswith("91"):
            local = local[2:]
        elif local.startswith("0"):
            local = local[1:]

        # Use first 2 digits as STD code proxy
        std_code = local[:2]
        return self.LOCATION_MAP.get(std_code, "India")

    async def run(self, target: str) -> PluginResult:
        # Clean phone number — keep digits and leading +
        phone = re.sub(r"[^\d+]", "", target)

        # Determine country
        country_code = "Unknown"
        if phone.startswith("+91") or phone.startswith("91"):
            country_code = "+91 (India)"
        elif phone.startswith("+1"):
            country_code = "+1 (US/Canada)"
        elif phone.startswith("+44"):
            country_code = "+44 (UK)"
        elif phone.startswith("+61"):
            country_code = "+61 (Australia)"
        elif phone.startswith("+"):
            # Extract any country code
            match = re.match(r"\+(\d{1,3})", phone)
            if match:
                country_code = f"+{match.group(1)}"
        else:
            # Assume Indian if it's a 10-digit number
            digits_only = re.sub(r"\D", "", phone)
            if len(digits_only) == 10:
                country_code = "+91 (India — local format)"
                phone = "+91" + digits_only

        # Infer carrier and location
        carrier = self._infer_carrier(phone)
        location = self._infer_location(phone)
        line_type = "Mobile" if len(re.sub(r"\D", "", phone)) >= 10 else "Unknown"

        # Try online API as bonus enrichment (non-blocking if it fails)
        try:
            import httpx
            async with httpx.AsyncClient(timeout=5) as client:
                resp = await client.get(
                    f"https://api.numlookupapi.com/v1/validate/{phone}",
                    params={"apikey": "demo"},
                    headers={"User-Agent": "TRINETRA-OSINT/1.0"},
                )
                if resp.status_code == 200:
                    data = resp.json()
                    api_carrier = data.get("carrier")
                    api_location = data.get("location")
                    api_line_type = data.get("line_type")
                    if api_carrier and api_carrier != "Unknown":
                        carrier = api_carrier
                    if api_location:
                        country = data.get("country_name", "")
                        location = f"{api_location}, {country}" if country else api_location
                    if api_line_type and api_line_type != "Unknown":
                        line_type = api_line_type
        except Exception as e:
            logger.debug("NumLookup API failed for %s: %s", phone, e)

        formatted_number = phone
        if len(phone) >= 12 and phone.startswith("+91"):
            # Format as +91 XXXXX XXXXX
            local = phone[3:]
            if len(local) == 10:
                formatted_number = f"+91 {local[:5]} {local[5:]}"

        gui_data = {
            "Phone": formatted_number,
            "Country Code": country_code,
            "Carrier": carrier,
            "Location": location,
            "Line Type": line_type,
        }

        terminal = f"""Phone Intel Report
═══════════════════
Phone: {formatted_number}
Country: {country_code}
Carrier: {carrier}
Location: {location}
Line Type: {line_type}
═══════════════════
Inferred from number pattern (online lookup unavailable)"""

        return PluginResult(
            plugin_id=self.plugin_id,
            plugin_name=self.name,
            category=self.category,
            target=target,
            gui_data=gui_data,
            terminal_data=terminal,
        )
