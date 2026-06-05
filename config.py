"""
============================================================
⚙️ CONFIGURATION MODULE v2.0
============================================================
Central configuration with posters support
============================================================
"""

import os


class Config:
    """Application configuration"""
    
    # 👤 PRASHANT SIR IDENTITY
    RM_NAME = os.getenv("RM_NAME", "Prashant Chandratre")
    RM_PHONE = os.getenv("RM_PHONE", "+91 7709446589")
    RM_EMAIL = os.getenv("RM_EMAIL", "prashantchandratre@pbpartners.com")
    RM_LOCATION = os.getenv("RM_LOCATION", "Pune/Nashik, Maharashtra")
    BRAND_TAGLINE = "Ek Rishta Bharose Ka"
    COMPANY_NAME = "PB Partners"
    TEAM_NAME = "Team Prashant"
    
    # 🔑 API KEYS (Set in Railway Variables)
    INTERAKT_API_KEY = os.getenv("INTERAKT_API_KEY", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    MORNING_API_KEY = os.getenv("MORNING_API_KEY", "pbp-secure-2026")
    
    # 🌐 Railway URL (auto-set if available)
    RAILWAY_URL = os.getenv("RAILWAY_PUBLIC_DOMAIN", "")
    if RAILWAY_URL and not RAILWAY_URL.startswith("http"):
        RAILWAY_URL = f"https://{RAILWAY_URL}"
    
    # 📲 INTERAKT
    INTERAKT_BASE_URL = "https://api.interakt.ai/v1/public"
    INTERAKT_MESSAGE_URL = f"{INTERAKT_BASE_URL}/message/"
    
    # 🤖 AI
    AI_MODEL = "gpt-4o-mini"
    AI_MAX_TOKENS = 300
    AI_TEMPERATURE = 0.7
    
    # ⚙️ APP
    RATE_LIMIT_SECONDS = 2
    DEFAULT_LANGUAGE = "marathi"
    
    # 📚 PB PARTNERS FACTS (For AI replies)
    PB_FACTS = """
PB PARTNERS OFFICIAL FACTS:

CREDENTIALS:
- Policybazaar group (NSE/BSE listed)
- IRDAI Composite Broker License No. 742
- 2.5 lakh+ active partners across 100+ cities
- 51+ insurance companies

REWARDS (UP TO 7.73% over base payout):
- Partner Contest: up to 3.50%
- Loyalty Quarterly Clubs: up to 0.50%
- Loyalty Yearly Clubs (Trip Rewards): up to 1.73%
- Renewal Contest: up to 2.00%

EXCLUSIVE FEATURES:
- On-Demand Payout (ODP) - NO COST
- Aggressive Payout Grid
- Monthly Portfolio Scheme
- LMC Coins, Renewal Protection
- VRM Support, 24x7 Support

ONBOARDING (100% FREE):
7 Documents: PAN, Aadhar, Bank Details,
10th Pass, Mobile, Email, Selfie
"""
