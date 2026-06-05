"""
============================================================
🔄 WEBHOOK HANDLER
============================================================
Processes incoming WhatsApp messages from Interakt
============================================================
"""

from datetime import datetime
from agent_data import get_agent_by_phone


class WebhookHandler:
    """Handles incoming WhatsApp webhooks"""
    
    def __init__(self, interakt_service, ai_engine):
        self.interakt = interakt_service
        self.ai = ai_engine
    
    def handle_incoming_message(self, data):
        try:
            if not data:
                return {"status": "ignored", "reason": "Empty payload"}
            
            message_data = self._extract_message(data)
            
            if not message_data:
                return {
                    "status": "ignored",
                    "reason": "Not a message event",
                    "received_keys": list(data.keys()) if isinstance(data, dict) else "non-dict"
                }
            
            phone = message_data['phone']
            user_message = message_data['message']
            
            print(f"📨 From: {phone}")
            print(f"💬 Message: {user_message[:100]}")
            
            agent = get_agent_by_phone(phone)
            agent_name = agent['name'] if agent else "Friend"
            language = agent['language'] if agent else "marathi"
            
            print(f"👤 Agent: {agent_name} | Language: {language}")
            
            reply = self.ai.generate_reply(
                user_message=user_message,
                agent_name=agent_name,
                language=language
            )
            
            print(f"🤖 AI Reply: {reply[:100]}...")
            
            send_result = self.interakt.send_text_message(phone, reply)
            
            return {
                "status": "✅ replied",
                "from": phone,
                "agent": agent_name,
                "language": language,
                "reply_preview": reply[:150] + "...",
                "send_result": send_result
            }
            
        except Exception as e:
            print(f"❌ Webhook handler error: {e}")
            import traceback
            traceback.print_exc()
            return {"status": "error", "error": str(e)}
    
    def _extract_message(self, data):
        try:
            event_type = (
                data.get('type', '') or
                data.get('event', '') or
                data.get('event_type', '')
            ).lower()
            
            valid_events = ['message_received', 'message', 'incoming_message']
            is_message = event_type in valid_events or 'message' in event_type
            
            if not is_message and event_type:
                return None
            
            # Format 1: Standard Interakt
            customer = data.get('data', {}).get('customer', {})
            message_obj = data.get('data', {}).get('message', {})
            
            if customer:
                country_code = customer.get('country_code', '+91').replace('+', '')
                phone_number = customer.get('phone_number', '')
                full_phone = f"{country_code}{phone_number}"
                message_text = message_obj.get('message', '')
                
                if phone_number and message_text:
                    return {
                        "phone": full_phone,
                        "message": message_text,
                        "timestamp": datetime.now().isoformat()
                    }
            
            # Format 2: Alternative
            phone_number = (
                data.get('phone_number', '') or
                data.get('phone', '') or
                data.get('from', '')
            )
            message_text = (
                data.get('message', '') or
                data.get('text', '') or
                data.get('body', '')
            )
            
            if phone_number and message_text:
                return {
                    "phone": str(phone_number),
                    "message": message_text,
                    "timestamp": datetime.now().isoformat()
                }
            
            return None
            
        except Exception as e:
            print(f"⚠️ Error extracting: {e}")
            return None
