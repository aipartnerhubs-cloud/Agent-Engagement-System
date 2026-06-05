"""
============================================================
🤖 AI REPLY ENGINE (Priya Assistant)
============================================================
GPT-4o-mini powered intelligent WhatsApp replies
============================================================
"""

from openai import OpenAI
from config import Config


class AIReplyEngine:
    """Generates intelligent WhatsApp replies"""
    
    def __init__(self, api_key):
        self.api_key = api_key
        if api_key:
            try:
                self.client = OpenAI(api_key=api_key)
                print("✅ OpenAI client initialized")
            except Exception as e:
                print(f"❌ OpenAI init failed: {e}")
                self.client = None
        else:
            self.client = None
            print("⚠️ OpenAI API key not set")
    
    def generate_reply(self, user_message, agent_name="Friend",
                       language="marathi", conversation_history=None):
        """Generate AI reply with Professional + Warm tone"""
        if not self.client:
            return self._fallback_reply(language, agent_name)
        
        try:
            system_prompt = self._build_system_prompt(agent_name, language)
            messages = [{"role": "system", "content": system_prompt}]
            
            if conversation_history:
                messages.extend(conversation_history)
            
            messages.append({"role": "user", "content": user_message})
            
            response = self.client.chat.completions.create(
                model=Config.AI_MODEL,
                messages=messages,
                max_tokens=Config.AI_MAX_TOKENS,
                temperature=Config.AI_TEMPERATURE
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"❌ AI Reply Error: {e}")
            return self._fallback_reply(language, agent_name)
    
    def _build_system_prompt(self, agent_name, language):
        language_instruction = {
            "marathi": "Respond in Marathi-Hindi MIX. Use BOTH Devanagari (मराठी) AND Roman script (Hinglish).",
            "hindi": "Respond in Hindi using Roman/English script (Hinglish).",
            "english": "Respond in simple English with occasional Hindi greetings."
        }.get(language.lower(), "Respond in Hindi/Hinglish.")
        
        return f"""You are Priya, the personal AI assistant of {Config.RM_NAME},
a Relationship Manager at {Config.COMPANY_NAME} (Policybazaar B2B platform).

🎯 YOUR ROLE:
- Assist Prashant Sir's agent partners on WhatsApp
- Brand tagline: "{Config.BRAND_TAGLINE}"
- You're warm yet professional

👤 CURRENT USER: {agent_name}

🗣️ LANGUAGE: {language_instruction}

📚 KEY KNOWLEDGE:
{Config.PB_FACTS}

✨ TONE: Professional + Warm
- Use "ji", "sir" - respectful
- Confident in knowledge
- Mention Prashant Sir warmly
- Solution-oriented

📋 RESPONSE RULES:
1. Short replies (3-5 sentences for WhatsApp)
2. Always mention Prashant Sir when relevant
3. Use exact facts from knowledge base
4. End with: "- Priya, {Config.RM_NAME} ji ki Assistant"
5. Use 1-2 emojis max
6. Never make up information

🚨 ESCALATION TRIGGERS (Tell agent to call Prashant Sir):
- Buying intent → Call {Config.RM_PHONE}
- Legal questions → Call {Config.RM_PHONE}
- Claim disputes → Call {Config.RM_PHONE}
- Account issues → Call {Config.RM_PHONE}
- Payment problems → Call {Config.RM_PHONE}

Remember: Represent PB Partners and Prashant Sir's brand.
Reinforce TRUST and PROFESSIONALISM."""
    
    def _fallback_reply(self, language, agent_name="Friend"):
        if language.lower() == "marathi":
            return f"""नमस्कार {agent_name} जी! 🙏

मी Priya, प्रशांत सरांची assistant आहे.
तुमचा message मिळाला आहे - प्रशांत सर लवकरच contact करतील.

Urgent असेल तर direct call करा: {Config.RM_PHONE}

- Priya, {Config.RM_NAME} जी ची Assistant"""
        elif language.lower() == "hindi":
            return f"""Namaste {agent_name} ji! 🙏

Main Priya, Prashant Sir ki assistant hu.
Aapka message mil gaya hai - Prashant Sir jaldi contact karenge.

Urgent ho to direct call karo: {Config.RM_PHONE}

- Priya, {Config.RM_NAME} ji ki Assistant"""
        else:
            return f"""Hello {agent_name}! 🙏

I'm Priya, assistant to {Config.RM_NAME}.
Your message received. Prashant Sir will contact you shortly.

For urgent: {Config.RM_PHONE}

- Priya, Assistant to {Config.RM_NAME}"""
