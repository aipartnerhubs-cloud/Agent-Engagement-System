# 🤖 Agent Engagement System v2.0

> Complete WhatsApp + Marketing Posters System for PB Partners

**Built for:** Prashant Chandratre (RM, PB Partners)
**Brand:** Ek Rishta Bharose Ka

---

## ✨ What's New in v2.0

🎨 **Marketing Posters System Added!**
- 30 ready-to-use AI poster prompts
- 6 categories (Car, Bike, Health, Family, Travel, Term Life)
- Beautiful web portal for agents
- Daily auto-poster delivery
- FREE AI tools integration (Ideogram, Microsoft Designer)

---

## 🎯 Complete Features

1. **🌅 Daily Morning Messages** (Marathi/Hindi)
2. **🤖 AI Webhook Replies** (Priya assistant)
3. **📲 Interakt Integration**
4. **🎨 Posters Portal** (30 prompts, 6 categories)
5. **🎨 Daily Auto-Poster** (rotates daily)

---

## ⚡ Quick Deploy (Only 2 API Keys!)

### **Just Set These in Railway:**

| Variable | Where to Get |
|---|---|
| `INTERAKT_API_KEY` | Your existing Interakt dashboard |
| `OPENAI_API_KEY` | https://platform.openai.com/api-keys |

**Everything else is PRE-FILLED!**

---

## 🚀 Deployment Steps

### **Step 1: GitHub Repo**
```
github.com → New repo → "Agent-Engagement-System"
Upload all files → Commit
```

### **Step 2: Railway Deploy**
```
railway.app → New Project → Deploy from GitHub
Select repo → Wait
```

### **Step 3: Add 2 API Keys**
```
Settings → Variables → Add:
- INTERAKT_API_KEY
- OPENAI_API_KEY
```

### **Step 4: Test**
```
Visit: https://YOUR-APP/api/config-check
Both APIs should be ✅ true
```

---

## 📡 API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Health check |
| `/api/config-check` | GET | Verify env vars |
| `/webhook/interakt` | POST | Incoming messages |
| `/api/send-morning-messages` | GET | Daily 8 AM trigger |
| `/api/send-daily-poster` | GET | 🆕 Daily 9 AM poster |
| `/api/test-message` | GET | Manual test |
| `/api/test-ai-reply` | GET | AI test |
| `/posters` | GET | 🆕 Posters portal |
| `/api/posters` | GET | 🆕 Posters JSON |
| `/api/prompt/<id>` | GET | 🆕 Specific prompt |

---

## 🗓️ Cron-job.org Setup

### **Cron 1: Morning Messages (8 AM)**
```
URL: https://YOUR-APP/api/send-morning-messages?key=pbp-secure-2026&phase=1
Schedule: 0 8 * * *
Timezone: Asia/Kolkata
```

### **Cron 2: Daily Poster (9 AM)** 🆕
```
URL: https://YOUR-APP/api/send-daily-poster?key=pbp-secure-2026&phase=1
Schedule: 0 9 * * *
Timezone: Asia/Kolkata
```

---

## 🎨 Posters Portal

**Access:** `https://YOUR-APP/posters`

Features:
- ✅ Browse 30 posters by category
- ✅ View full AI prompt
- ✅ Copy to clipboard
- ✅ Direct link to AI tool
- ✅ Mobile-responsive

**Free AI Tools Used:**
- **Ideogram.ai** (best for posters with text)
- **Microsoft Designer** (unlimited free)
- **Bing Image Creator** (FREE)

---

## 📁 Project Structure

```
Agent-Engagement-System/
├── app.py                    # Main Flask app
├── config.py                 # Settings (Prashant pre-set)
├── interakt_service.py       # WhatsApp API
├── ai_replies.py             # OpenAI GPT-4
├── daily_engagement.py       # Morning messages
├── webhook_handler.py        # Incoming processor
├── agent_data.py             # Agent list
├── posters_data.py           # 🆕 30 poster prompts
├── posters_template.py       # 🆕 Portal HTML
├── requirements.txt          # Dependencies
├── Procfile                  # Railway start
├── runtime.txt               # Python 3.11.7
├── README.md                 # This file
└── .gitignore                # Git exclusions
```

---

## 📞 Support

**Prashant Chandratre**
📞 +91 7709446589
📧 prashantchandratre@pbpartners.com

---

**© 2026 PB Partners - AI Powered**
