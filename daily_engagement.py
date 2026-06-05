"""
============================================================
🌅 DAILY ENGAGEMENT MODULE
============================================================
Day-themed Marathi + Hindi morning messages
============================================================
"""

from datetime import datetime
from config import Config


MORNING_MESSAGES_MARATHI = {
    "Monday": """🌅 शुभ सकाळ {name} जी!

नवीन आठवडा, नवीन goals! 💪

आजचे challenge:
✅ कमीत कमी ३ quotes generate करा
✅ १ pending renewal ला call करा
✅ एक नवीन customer पर्यंत पोहोचा

PBPartners मध्ये Partner Contest मधून up to 3.50% extra reward मिळतो.

- {rm_name}
📞 {rm_phone}""",

    "Tuesday": """🌞 शुभ सकाळ {name} जी!

आज Renewal Tuesday! 🔄

तुमच्या pending renewals पैकी ३ ला आज call करा. Renewal Contest मधून up to 2% extra commission मिळतो.

💡 Tip: "Renewal call मध्ये आधी 'गाडी कशी चालू आहे?' विचारा — मग insurance बद्दल बोला."

- {rm_name}
📞 {rm_phone}""",

    "Wednesday": """🌅 शुभ सकाळ {name} जी!

आज Cross-Sell Wednesday! 💼

तुमच्या motor customers पैकी 70% कडे family health insurance नाही!

📱 Script: "Sir, गाडीचा insurance झाला — कुटुंबाचा health insurance आहे का? १ लाखाचा cover फक्त ₹500/month पासून."

आज २ cross-sell try करा!

- {rm_name}
📞 {rm_phone}""",

    "Thursday": """🌅 शुभ सकाळ {name} जी!

आज Customer Care Thursday! ❤️

५ जुन्या customers ना एक voice note पाठवा. हे FREE आहे, पण effect मोठा:
✅ Customer retention 2x
✅ Referrals आपोआप

- {rm_name}
📞 {rm_phone}""",

    "Friday": """🌅 शुभ सकाळ {name} जी!

Friday! 🚀 आज ३ नवीन leads generate करा!

💡 Formula:
1. Local garage owner शी बोला
2. Petrol pump जवळ २ cars चे owners
3. WhatsApp status वर quote sticker

- {rm_name}
📞 {rm_phone}""",

    "Saturday": """🌅 Saturday energy {name} जी! ⚡

Weekend = High-conversion time!

आजचा focus:
🎯 २ face-to-face meetings
🎯 ५ follow-ups close करा
🎯 १ family insurance pitch

- {rm_name}
📞 {rm_phone}""",

    "Sunday": """🌸 शुभ सकाळ {name} जी!

Sunday — smart planning चा दिवस!

💡 आज हे करा:
1. Top 5 leads ची list
2. ३ renewals scripts ready
3. १ cross-sell opportunity

PBPartners ecosystem मध्ये Grow Together, Succeed Together. 💪

- {rm_name}
📞 {rm_phone}"""
}


MORNING_MESSAGES_HINDI = {
    "Monday": """🌅 Suprabhat {name} ji!

Naya hafta, naye goals! 💪

Aaj ka challenge:
✅ Kam se kam 3 quotes generate karo
✅ 1 pending renewal ko call karo
✅ Ek naya customer reach karo

PBPartners mein Partner Contest se up to 3.50% extra reward milta hai.

- {rm_name}
📞 {rm_phone}""",

    "Tuesday": """🌞 Suprabhat {name} ji!

Aaj Renewal Tuesday! 🔄

Pending renewals mein se 3 ko aaj call karo. Renewal Contest se up to 2% extra commission.

💡 Tip: "Renewal call mein pehle 'Sir, gaadi kaisi chal rahi hai?' puchho."

- {rm_name}
📞 {rm_phone}""",

    "Wednesday": """🌅 Suprabhat {name} ji!

Aaj Cross-Sell Wednesday! 💼

Motor customers mein se 70% ke paas family health insurance NAHI hai!

📱 Script: "Sir, gaadi ka insurance ho gaya — family ka health insurance? 1 lakh cover ₹500/month se."

Aaj 2 cross-sell try karo!

- {rm_name}
📞 {rm_phone}""",

    "Thursday": """🌅 Suprabhat {name} ji!

Aaj Customer Care Thursday! ❤️

5 purane customers ko voice note bhejo. FREE hai, par effect bada:
✅ Retention 2x
✅ Referrals automatic

- {rm_name}
📞 {rm_phone}""",

    "Friday": """🌅 Suprabhat {name} ji!

Friday! 🚀 Aaj 3 naye leads generate karo!

💡 Formula:
1. Local garage owner se baat
2. Petrol pump ke pass 2 cars
3. WhatsApp status pe quote sticker

- {rm_name}
📞 {rm_phone}""",

    "Saturday": """🌅 Saturday energy {name} ji! ⚡

Weekend = High-conversion time!

Aaj ka focus:
🎯 2 face-to-face meetings
🎯 5 follow-ups close
🎯 1 family insurance pitch

- {rm_name}
📞 {rm_phone}""",

    "Sunday": """🌸 Suprabhat {name} ji!

Sunday — smart planning ka din!

💡 Aaj yeh karo:
1. Top 5 leads ki list
2. 3 renewals scripts ready
3. 1 cross-sell opportunity

Grow Together, Succeed Together. 💪

- {rm_name}
📞 {rm_phone}"""
}


def get_morning_message(agent_name, language="marathi"):
    today = datetime.now().strftime("%A")
    first_name = agent_name.split()[0] if agent_name else "Sir"
    
    if language.lower() == "hindi":
        templates = MORNING_MESSAGES_HINDI
    else:
        templates = MORNING_MESSAGES_MARATHI
    
    template = templates.get(today, templates["Monday"])
    
    return template.format(
        name=first_name,
        rm_name=Config.RM_NAME,
        rm_phone=Config.RM_PHONE
    )
