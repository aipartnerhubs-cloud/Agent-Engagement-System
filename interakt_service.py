"""
============================================================
📲 INTERAKT WHATSAPP SERVICE
============================================================
Clean wrapper for Interakt API
============================================================
"""

import requests


class InteraktService:
    """Handles all Interakt WhatsApp API interactions"""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.interakt.ai/v1/public"
        
        if not api_key:
            self.auth_header = None
            print("⚠️ WARNING: Interakt API key not set")
        else:
            self.auth_header = f"Basic {api_key}"
    
    def send_text_message(self, phone, message, country_code="+91"):
        """Send free-text WhatsApp message"""
        if not self.auth_header:
            return {"result": False, "message": "❌ Interakt API key not configured"}
        
        clean_phone = self._clean_phone(phone)
        
        if clean_phone.startswith("91") and len(clean_phone) > 10:
            phone_number = clean_phone[2:]
            country_code = "+91"
        else:
            phone_number = clean_phone
        
        url = f"{self.base_url}/message/"
        
        payload = {
            "countryCode": country_code,
            "phoneNumber": phone_number,
            "type": "Text",
            "data": {"message": message}
        }
        
        headers = {
            "Authorization": self.auth_header,
            "Content-Type": "application/json"
        }
        
        try:
            print(f"📤 Sending to {country_code}{phone_number}...")
            response = requests.post(url, headers=headers, json=payload, timeout=15)
            response_data = response.json() if response.text else {}
            
            if response.status_code in [200, 201]:
                print(f"✅ Sent: {response.status_code}")
                return {
                    "result": True,
                    "status_code": response.status_code,
                    "response": response_data
                }
            else:
                print(f"❌ Failed: {response.status_code} - {response_data}")
                return {
                    "result": False,
                    "status_code": response.status_code,
                    "message": str(response_data),
                    "response": response_data
                }
            
        except requests.exceptions.Timeout:
            return {"result": False, "message": "⏱️ Timeout"}
        except Exception as e:
            return {"result": False, "message": f"❌ Error: {str(e)}"}
    
    def send_template_message(self, phone, template_name, language_code="en",
                              header_values=None, body_values=None, country_code="+91"):
        """Send approved template message"""
        if not self.auth_header:
            return {"result": False, "message": "API key not set"}
        
        clean_phone = self._clean_phone(phone)
        if clean_phone.startswith("91") and len(clean_phone) > 10:
            phone_number = clean_phone[2:]
        else:
            phone_number = clean_phone
        
        url = f"{self.base_url}/message/"
        
        payload = {
            "countryCode": country_code,
            "phoneNumber": phone_number,
            "type": "Template",
            "template": {
                "name": template_name,
                "languageCode": language_code,
                "headerValues": header_values or [],
                "bodyValues": body_values or []
            }
        }
        
        headers = {
            "Authorization": self.auth_header,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=15)
            response_data = response.json() if response.text else {}
            return {
                "result": response.status_code in [200, 201],
                "status_code": response.status_code,
                "response": response_data
            }
        except Exception as e:
            return {"result": False, "message": str(e)}
    
    def _clean_phone(self, phone):
        return str(phone).replace(" ", "").replace("-", "").replace("+", "")
