#use PyMISP

from pymisp import ExpandedPyMISP, MISPEvent

class MISPIntegration:
    def __init__(self, url, api_key):
        self.url = url.rstrip("/") + "/"
        self.api_key = api_key
        self.misp = ExpandedPyMISP(self.url, self.api_key)

    def create_event(self, info, threat_level_id=2):
        event = MISPEvent()
        event.info = info
        event.threat_level_id = threat_level_id  # 1: Low, 2: Medium, 3: High
        response = self.misp.add_event(event, pythonify=True)
        if response.get("Event"):
            return response.get("Event")
        else:
            print("Error creating event:", response)
            return None

    def search_indicator(self, indicator):
        response = self.misp.search_index(indicator)
        if response.get("response"):
            return response.get("response")
        else:
            print("Error searching indicator:", response)
            return None

# Example usage:
# misp_integration = MISPIntegration("https://your-misp-instance.com", "your_api_key")
# event = misp_integration.create_event("Suspicious activity detected", threat_level_id=3)
# if event:
#     print("Event created:", event)
# indicators = misp_integration.search_indicator("123.456.789.0")
# if indicators:
#     print("Indicators found:", indicators)
