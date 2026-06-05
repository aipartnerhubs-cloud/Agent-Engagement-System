"""
============================================================
🤖 AGENT ENGAGEMENT SYSTEM v2.0
============================================================
Complete WhatsApp + Marketing Posters System for PB Partners
Built for: Prashant Chandratre (RM, PBPartners)

Features:
- Daily morning messages (Marathi + Hindi)
- AI-powered webhook replies (Priya assistant)
- Interakt WhatsApp integration
- 🎨 NEW: Marketing Posters Portal
- 🎨 NEW: Daily Auto-Poster Delivery
- 🎨 NEW: AI Prompts Library

API Endpoints:
- GET  /                          → Health check
- GET  /api/config-check          → Verify env vars
- POST /webhook/interakt          → Incoming messages
- GET  /api/send-morning-messages → Daily 8 AM trigger
- GET  /api/send-daily-poster     → 🆕 Daily 9 AM poster
- GET  /api/test-message          → Manual test
- GET  /api/test-ai-reply         → AI test only
- GET  /posters                   → 🆕 Posters portal
- GET  /api/posters               → 🆕 Get poster list (JSON)
- GET  /api/prompt/<id>           → 🆕 Get AI prompt by ID
============================================================
"""

from flask import Flask, request, jsonify, render_template_string
import os
import time
import random
import traceback
from datetime import datetime

# Import our modules
from config import Config
from interakt_service import InteraktService
from daily_engagement import get_morning_message
from ai_replies import AIReplyEngine
from webhook_handler import WebhookHandler
from agent_data import get_test_agents, get_agent_by_phone
from posters_data import POSTERS_LIBRARY, get_random_poster, get_poster_by_id, get_posters_by_category
from posters_template import POSTERS_PORTAL_HTML

# ============================================================
# APP INITIALIZATION
# ============================================================
app = Flask(__name__)
config = Config()

# Initialize services
interakt = InteraktService(api_key=config.INTERAKT_API_KEY)
ai_engine = AIReplyEngine(api_key=config.OPENAI_API_KEY)
webhook_handler = WebhookHandler(interakt_service=interakt, ai_engine=ai_engine)

print(f"🚀 Agent Engagement System v2.0 Starting...")
print(f"👤 RM: {config.RM_NAME}")
print(f"📞 Phone: {config.RM_PHONE}")
print(f"🔑 Interakt: {'✅' if config.INTERAKT_API_KEY else '❌'}")
print(f"🔑 OpenAI: {'✅' if config.OPENAI_API_KEY else '❌'}")
print(f"🎨 Posters Library: {len(POSTERS_LIBRARY)} prompts loaded")


# ============================================================
# ROOT ENDPOINT - Health Check
# ============================================================
@app.route("/", methods=["GET"])
def home():
    """System health check"""
    return jsonify({
        "status": "✅ Active",
        "system": "Agent Engagement System v2.0",
        "version": "2.0.0",
        "rm": {
            "name": config.RM_NAME,
            "phone": config.RM_PHONE
        },
        "timestamp": datetime.now().isoformat(),
        "features": {
            "daily_messages": "✅ Marathi + Hindi",
            "ai_replies": "✅ Priya assistant",
            "posters_library": f"✅ {len(POSTERS_LIBRARY)} prompts",
            "auto_delivery": "✅ Daily morning + poster"
        },
        "endpoints": {
            "health": "GET /",
            "config_check": "GET /api/config-check",
            "send_morning": "GET /api/send-morning-messages?key=YOUR_KEY",
            "send_daily_poster": "GET /api/send-daily-poster?key=YOUR_KEY",
            "webhook": "POST /webhook/interakt",
            "test_message": "GET /api/test-message?key=YOUR_KEY",
            "test_ai": "GET /api/test-ai-reply?key=YOUR_KEY&text=hello",
            "posters_portal": "GET /posters",
            "posters_list": "GET /api/posters"
        }
    }), 200


# ============================================================
# CONFIG CHECK
# ============================================================
@app.route("/api/config-check", methods=["GET"])
def config_check():
    """Verify all environment variables are set"""
    interakt_set = bool(config.INTERAKT_API_KEY)
    openai_set = bool(config.OPENAI_API_KEY)
    all_ok = interakt_set and openai_set
    
    return jsonify({
        "status": "✅ Ready" if all_ok else "⚠️ Missing keys",
        "config": {
            "interakt_api_set": interakt_set,
            "openai_api_set": openai_set,
            "rm_name": config.RM_NAME,
            "rm_phone": config.RM_PHONE,
            "morning_api_key_set": bool(config.MORNING_API_KEY),
            "phase_1_agents": len(get_test_agents("1")),
            "posters_count": len(POSTERS_LIBRARY)
        },
        "instructions": "All keys must be ✅ to deploy"
    }), 200


# ============================================================
# WEBHOOK - Incoming WhatsApp messages
# ============================================================
@app.route("/webhook/interakt", methods=["POST"])
def interakt_webhook():
    """Receives incoming WhatsApp messages via Interakt"""
    try:
        data = request.get_json()
        print(f"\n📥 Webhook: {datetime.now()}")
        
        result = webhook_handler.handle_incoming_message(data)
        print(f"✅ Result: {result.get('status')}")
        return jsonify(result), 200
        
    except Exception as e:
        print(f"❌ Webhook error: {e}")
        traceback.print_exc()
        return jsonify({"status": "error", "message": str(e)}), 200


# ============================================================
# DAILY MORNING MESSAGES - Cron-triggered
# ============================================================
@app.route("/api/send-morning-messages", methods=["GET", "POST"])
def send_morning_messages():
    """Daily 8 AM cron trigger - morning messages"""
    secret_key = request.headers.get("X-API-Key") or request.args.get("key")
    if secret_key != config.MORNING_API_KEY:
        return jsonify({"status": "error", "message": "Invalid API key"}), 401
    
    phase = request.args.get("phase", "1")
    agents = get_test_agents(phase=phase)
    
    if not agents:
        return jsonify({"status": "warning", "message": "No agents"}), 200
    
    results = []
    sent_count = 0
    failed_count = 0
    
    print(f"\n🌅 Morning job: Phase {phase} | {len(agents)} agents")
    
    for agent in agents:
        try:
            message = get_morning_message(
                agent_name=agent['name'],
                language=agent.get('language', 'marathi')
            )
            response = interakt.send_text_message(
                phone=agent['phone'],
                message=message
            )
            
            if response.get('result'):
                results.append({"phone": agent['phone'], "name": agent['name'], "status": "✅ sent"})
                sent_count += 1
            else:
                raise Exception(response.get('message', 'Send failed'))
            
            time.sleep(2)
        except Exception as e:
            results.append({
                "phone": agent['phone'], "name": agent['name'],
                "status": "❌ failed", "error": str(e)
            })
            failed_count += 1
    
    return jsonify({
        "timestamp": datetime.now().isoformat(),
        "phase": phase,
        "total": len(agents),
        "sent": sent_count,
        "failed": failed_count,
        "results": results
    }), 200


# ============================================================
# 🆕 DAILY POSTER SHARING - New endpoint
# ============================================================
@app.route("/api/send-daily-poster", methods=["GET", "POST"])
def send_daily_poster():
    """
    Daily 9 AM cron trigger - sends today's marketing poster
    Sends prompt + portal link to agents
    """
    secret_key = request.headers.get("X-API-Key") or request.args.get("key")
    if secret_key != config.MORNING_API_KEY:
        return jsonify({"status": "error", "message": "Invalid API key"}), 401
    
    phase = request.args.get("phase", "1")
    agents = get_test_agents(phase=phase)
    
    # Get today's poster (rotates daily)
    poster = get_random_poster()
    
    # Build poster message
    portal_url = config.RAILWAY_URL or "https://your-app.up.railway.app"
    
    results = []
    sent_count = 0
    failed_count = 0
    
    print(f"\n🎨 Poster job: {poster['title']}")
    
    for agent in agents:
        try:
            # Personalized message based on language
            if agent.get('language', 'marathi') == 'marathi':
                message = f"""🎨 आजचा Marketing Poster!

📌 *{poster['title']}*
💡 Category: {poster['category']}

✨ कसे वापरायचे:
1. हा prompt copy करा 👇
2. {poster['tool']} वर paste करा (FREE)
3. Image generate होईल
4. आपलं नाव + फोटो edit करा
5. Customers ला share करा!

📋 *PROMPT:*
{poster['prompt']}

🌐 More posters: {portal_url}/posters

- {config.RM_NAME}
📞 {config.RM_PHONE}"""
            else:
                message = f"""🎨 Aaj Ka Marketing Poster!

📌 *{poster['title']}*
💡 Category: {poster['category']}

✨ Kaise use karna:
1. Yeh prompt copy karo 👇
2. {poster['tool']} pe paste karo (FREE)
3. Image generate hoga
4. Apna naam + photo edit karo
5. Customers ko share karo!

📋 *PROMPT:*
{poster['prompt']}

🌐 More posters: {portal_url}/posters

- {config.RM_NAME}
📞 {config.RM_PHONE}"""
            
            response = interakt.send_text_message(
                phone=agent['phone'],
                message=message
            )
            
            if response.get('result'):
                results.append({"phone": agent['phone'], "status": "✅ sent"})
                sent_count += 1
            else:
                raise Exception(response.get('message', 'Failed'))
            
            time.sleep(2)
        except Exception as e:
            results.append({"phone": agent['phone'], "status": "❌ failed", "error": str(e)})
            failed_count += 1
    
    return jsonify({
        "timestamp": datetime.now().isoformat(),
        "poster_sent": poster['title'],
        "category": poster['category'],
        "total": len(agents),
        "sent": sent_count,
        "failed": failed_count,
        "results": results
    }), 200


# ============================================================
# 🆕 POSTERS PORTAL - Web interface
# ============================================================
@app.route("/posters", methods=["GET"])
def posters_portal():
    """Beautiful posters browsing portal for agents"""
    return render_template_string(
        POSTERS_PORTAL_HTML,
        rm_name=config.RM_NAME,
        rm_phone=config.RM_PHONE,
        posters=POSTERS_LIBRARY,
        total=len(POSTERS_LIBRARY)
    )


# ============================================================
# 🆕 POSTERS API - JSON list
# ============================================================
@app.route("/api/posters", methods=["GET"])
def posters_api():
    """Get all posters as JSON (for mobile apps or integration)"""
    category = request.args.get("category", "all")
    
    if category == "all":
        posters = POSTERS_LIBRARY
    else:
        posters = get_posters_by_category(category)
    
    return jsonify({
        "total": len(posters),
        "category": category,
        "posters": posters
    }), 200


# ============================================================
# 🆕 GET SPECIFIC PROMPT
# ============================================================
@app.route("/api/prompt/<int:poster_id>", methods=["GET"])
def get_prompt(poster_id):
    """Get specific poster prompt by ID"""
    poster = get_poster_by_id(poster_id)
    if not poster:
        return jsonify({"status": "error", "message": "Not found"}), 404
    
    return jsonify({
        "status": "success",
        "poster": poster
    }), 200


# ============================================================
# TEST ENDPOINTS
# ============================================================
@app.route("/api/test-message", methods=["GET", "POST"])
def test_message():
    """Send single test message"""
    secret_key = request.headers.get("X-API-Key") or request.args.get("key")
    if secret_key != config.MORNING_API_KEY:
        return jsonify({"status": "error", "message": "Invalid key"}), 401
    
    phone = request.args.get("phone", "917709446589")
    name = request.args.get("name", "Prashant")
    language = request.args.get("lang", "marathi")
    
    try:
        message = get_morning_message(name, language)
        response = interakt.send_text_message(phone, message)
        return jsonify({
            "status": "✅ success" if response.get('result') else "❌ failed",
            "phone": phone, "name": name, "language": language,
            "message_preview": message[:200] + "...",
            "interakt_response": response
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500


@app.route("/api/test-ai-reply", methods=["GET", "POST"])
def test_ai_reply():
    """Test AI engine without sending message"""
    secret_key = request.headers.get("X-API-Key") or request.args.get("key")
    if secret_key != config.MORNING_API_KEY:
        return jsonify({"status": "error", "message": "Invalid key"}), 401
    
    text = request.args.get("text", "Hello")
    language = request.args.get("lang", "marathi")
    name = request.args.get("name", "Agent")
    
    try:
        reply = ai_engine.generate_reply(
            user_message=text, agent_name=name, language=language
        )
        return jsonify({
            "status": "✅ success", "input": text,
            "language": language, "ai_reply": reply
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500


# ============================================================
# ERROR HANDLERS
# ============================================================
@app.errorhandler(404)
def not_found(e):
    return jsonify({"status": "error", "message": "Not found. Visit / for endpoints"}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"status": "error", "message": "Server error"}), 500


# ============================================================
# RUN APP
# ============================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🌐 Server starting on port {port}")
    app.run(host="0.0.0.0", port=port, debug=False)
