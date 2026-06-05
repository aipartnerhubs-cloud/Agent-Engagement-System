"""
============================================================
🎨 POSTERS LIBRARY
============================================================
30 ready-to-use AI prompts for marketing posters
- 6 categories × 5 prompts each
- For Ideogram, Microsoft Designer, Bing
- Easy categorization and search
============================================================
"""

import random

# ============================================================
# 📚 30 POSTERS LIBRARY
# ============================================================
POSTERS_LIBRARY = [
    # 🚗 CAR INSURANCE (5)
    {
        "id": 1,
        "category": "Car Insurance",
        "category_id": "car",
        "title": "Premium Sedan Protection",
        "style": "Professional",
        "tool": "Ideogram",
        "prompt": "A professional WhatsApp marketing poster, vertical 9:16 format, premium red sedan car protected by a transparent blue shield umbrella, modern minimalist design, navy blue gradient background with gold accents, bold headline 'PROTECT YOUR CAR PROTECT YOUR DREAMS' in white text at top, 'Starting ₹2,499/year' badge in gold, 'Car Insurance Made Simple' subtitle, space at bottom for agent name and contact, professional photography style, 8K quality, ultra-detailed",
        "icon": "🚗",
        "color": "blue"
    },
    {
        "id": 2,
        "category": "Car Insurance",
        "category_id": "car",
        "title": "Diwali Festival Special",
        "style": "Festival",
        "tool": "Ideogram",
        "prompt": "Festive Diwali themed car insurance poster, vertical format, luxury car with diyas and golden bokeh lights, 'DIWALI SPECIAL CAR INSURANCE' big bold text, festive red and gold color scheme, traditional Indian patterns border, 'Save up to 80%' callout, modern professional design, leave bottom 20% white space for agent details",
        "icon": "🪔",
        "color": "red"
    },
    {
        "id": 3,
        "category": "Car Insurance",
        "category_id": "car",
        "title": "Minimalist SUV",
        "style": "Minimal",
        "tool": "Microsoft Designer",
        "prompt": "Minimalist white background poster for car insurance, single sleek black SUV in center, geometric shapes, clean modern typography, 'DRIVE WORRY-FREE' headline in black, blue accent color, 'Get instant quote' CTA, Swiss design style, lots of white space, professional",
        "icon": "🚙",
        "color": "white"
    },
    {
        "id": 4,
        "category": "Car Insurance",
        "category_id": "car",
        "title": "Family Car Safety",
        "style": "Family",
        "tool": "Ideogram",
        "prompt": "Happy Indian family with car in background, warm golden hour lighting, smiling parents with two kids, 'FAMILY KI SURAKSHA, GAADI KI BHI' Hindi-English mix headline, soft warm tones, professional poster design, vertical layout, emotional appeal",
        "icon": "👨‍👩‍👧",
        "color": "orange"
    },
    {
        "id": 5,
        "category": "Car Insurance",
        "category_id": "car",
        "title": "85% Discount Offer",
        "style": "Discount",
        "tool": "Microsoft Designer",
        "prompt": "Bold sale poster for car insurance with red modern car, 'UP TO 85% OFF' huge text, urgency design, lightning bolts, 'Limited time' stamp, bright colors red and yellow, modern advertising style, professional marketing poster",
        "icon": "💰",
        "color": "red"
    },
    
    # 🏍️ BIKE INSURANCE (5)
    {
        "id": 6,
        "category": "Bike Insurance",
        "category_id": "bike",
        "title": "Mountain Adventure Ride",
        "style": "Adventure",
        "tool": "Ideogram",
        "prompt": "Vertical poster, sporty motorcycle on mountain road, sunset background, motion blur showing speed, 'RIDE FREE, RIDE SAFE' bold text in white, orange gradient overlay, 'Bike Insurance ₹699/year' badge, adventure photography style, professional marketing poster, leave space at bottom",
        "icon": "🏍️",
        "color": "orange"
    },
    {
        "id": 7,
        "category": "Bike Insurance",
        "category_id": "bike",
        "title": "Urban Monsoon",
        "style": "Urban",
        "tool": "Ideogram",
        "prompt": "Modern scooter parked in Indian city street, monsoon rain scene, person in raincoat, 'MONSOON READY?' big text, blue and grey color scheme, water droplets effect, 'Rainproof your ride' tagline, lifestyle photography",
        "icon": "🛵",
        "color": "blue"
    },
    {
        "id": 8,
        "category": "Bike Insurance",
        "category_id": "bike",
        "title": "Premium Superbike",
        "style": "Premium",
        "tool": "Ideogram",
        "prompt": "Black premium superbike (like Royal Enfield or Ninja) on dark background, dramatic side lighting, gold accents, 'FOR THOSE WHO LIVE TO RIDE' elegant text, luxury feel, premium marketing poster, vertical 9:16 format",
        "icon": "🏍️",
        "color": "black"
    },
    {
        "id": 9,
        "category": "Bike Insurance",
        "category_id": "bike",
        "title": "All Bikes Combo",
        "style": "Combo",
        "tool": "Microsoft Designer",
        "prompt": "Split design poster showing scooter and motorcycle side by side, 'ALL BIKES COVERED' headline, modern infographic style, blue and white scheme, icons showing benefits, professional marketing design",
        "icon": "🛵",
        "color": "blue"
    },
    {
        "id": 10,
        "category": "Bike Insurance",
        "category_id": "bike",
        "title": "Republic Day Special",
        "style": "Festive",
        "tool": "Ideogram",
        "prompt": "Patriotic themed bike insurance poster, tricolor (saffron, white, green) accents, 'INDEPENDENCE FOR YOUR RIDE' headline, modern bike with Indian flag bokeh, 'Special 26 January Offer', professional festive design",
        "icon": "🇮🇳",
        "color": "tricolor"
    },
    
    # ❤️ HEALTH INSURANCE (5)
    {
        "id": 11,
        "category": "Health Insurance",
        "category_id": "health",
        "title": "Modern Hospital",
        "style": "Hospital",
        "tool": "Ideogram",
        "prompt": "Modern hospital corridor with doctor and patient, soft natural lighting, 'HEALTH IS WEALTH' bold text, green gradient overlay, '₹5 Lakh cover @ ₹500/month' pricing badge, '10,000+ Cashless Hospitals' feature highlights, professional healthcare poster, trustworthy design",
        "icon": "🏥",
        "color": "green"
    },
    {
        "id": 12,
        "category": "Health Insurance",
        "category_id": "health",
        "title": "Mediclaim Peace",
        "style": "Mediclaim",
        "tool": "Ideogram",
        "prompt": "Stethoscope on family photo, soft warm tones, 'MEDICLAIM = PEACE OF MIND' headline, blue and white color scheme, modern minimalist design, hospital benefits list, '24x7 Claim Support' badge, professional layout",
        "icon": "🩺",
        "color": "blue"
    },
    {
        "id": 13,
        "category": "Health Insurance",
        "category_id": "health",
        "title": "Senior Citizen Care",
        "style": "Senior",
        "tool": "Ideogram",
        "prompt": "Elderly Indian couple smiling, warm golden lighting, 'AAPKE BUZURGON KA SAHARA' Hindi headline, respectful warm design, soft tones, 'Senior Citizen Health Plan' tagline, 'No medical test up to 65 years' feature, emotional appeal poster",
        "icon": "👴",
        "color": "gold"
    },
    {
        "id": 14,
        "category": "Health Insurance",
        "category_id": "health",
        "title": "Critical Illness Cover",
        "style": "Critical",
        "tool": "Microsoft Designer",
        "prompt": "Medical icons (heart, cross, shield) arrangement, 'PROTECT FROM 35+ CRITICAL ILLNESSES' bold headline, red and white color scheme, scientific clean design, modern healthcare marketing poster, list of covered diseases stylish layout",
        "icon": "🛡️",
        "color": "red"
    },
    {
        "id": 15,
        "category": "Health Insurance",
        "category_id": "health",
        "title": "Cashless Hospitalization",
        "style": "Cashless",
        "tool": "Microsoft Designer",
        "prompt": "Wallet with cash and medical card, 'CASHLESS HOSPITALIZATION' big text, green check marks, modern flat design illustration, 'Pay ₹0 at hospital' callout, infographic poster style, professional",
        "icon": "💳",
        "color": "green"
    },
    
    # 👨‍👩‍👧‍👦 FAMILY HEALTH BUNDLE (5)
    {
        "id": 16,
        "category": "Family Health",
        "category_id": "family",
        "title": "Happy Family Hero",
        "style": "Family",
        "tool": "Ideogram",
        "prompt": "Joyful Indian family of 4 - parents, son, daughter - hugging together in modern home, natural lighting, 'PURE PARIVAAR KA HEALTH KAVACH' Hindi headline, warm tones, 'Cover entire family @ ₹999/month' pricing, professional family lifestyle poster, leave space for agent details at bottom",
        "icon": "👨‍👩‍👧‍👦",
        "color": "warm"
    },
    {
        "id": 17,
        "category": "Family Health",
        "category_id": "family",
        "title": "Floater Umbrella",
        "style": "Floater",
        "tool": "Microsoft Designer",
        "prompt": "Umbrella protecting family figures (papa, mama, kids, grandparents), modern flat illustration style, 'ONE POLICY FOR WHOLE FAMILY' headline, blue and orange palette, infographic showing coverage, professional insurance marketing poster",
        "icon": "☂️",
        "color": "blue"
    },
    {
        "id": 18,
        "category": "Family Health",
        "category_id": "family",
        "title": "Maternity Care",
        "style": "Maternity",
        "tool": "Ideogram",
        "prompt": "Happy expecting couple, soft pink and blue gradient, 'MATERNITY COVERAGE INCLUDED' headline, baby shoes prop, 'Pregnancy + Newborn Care' features, warm emotional design, healthcare marketing poster",
        "icon": "👶",
        "color": "pink"
    },
    {
        "id": 19,
        "category": "Family Health",
        "category_id": "family",
        "title": "Three Generations",
        "style": "Multi-gen",
        "tool": "Ideogram",
        "prompt": "3 generations Indian family - dada-dadi, parents, kids - sitting together on couch laughing, 'TEEN PEERHIYAN, EK HEALTH PLAN' Hindi headline, warm home setting, multigenerational family insurance poster, professional",
        "icon": "👵",
        "color": "warm"
    },
    {
        "id": 20,
        "category": "Family Health",
        "category_id": "family",
        "title": "Less Than Tea Cost",
        "style": "Affordable",
        "tool": "Microsoft Designer",
        "prompt": "Coin stack and family icons combo, 'FAMILY PROTECTION @ ₹33/DAY' big bold pricing, 'Less than a tea ☕' comparison, smart marketing poster design, savings emphasis, professional",
        "icon": "☕",
        "color": "gold"
    },
    
    # ✈️ TRAVEL INSURANCE (5)
    {
        "id": 21,
        "category": "Travel Insurance",
        "category_id": "travel",
        "title": "World Explorer",
        "style": "International",
        "tool": "Ideogram",
        "prompt": "Vibrant world map with airplane, passport and tickets in foreground, 'TRAVEL THE WORLD WORRY-FREE' headline, sky blue and white scheme, 'Coverage in 200+ countries' badge, professional travel insurance poster, lifestyle photography",
        "icon": "🌍",
        "color": "blue"
    },
    {
        "id": 22,
        "category": "Travel Insurance",
        "category_id": "travel",
        "title": "Honeymoon Special",
        "style": "Honeymoon",
        "tool": "Ideogram",
        "prompt": "Romantic couple at beach sunset, 'HONEYMOON INSURANCE' elegant text, soft warm romantic colors, heart icons, 'Cover medical emergencies, lost baggage, cancellations', luxury feel, professional honeymoon travel marketing poster",
        "icon": "💑",
        "color": "pink"
    },
    {
        "id": 23,
        "category": "Travel Insurance",
        "category_id": "travel",
        "title": "Family Vacation",
        "style": "Family",
        "tool": "Ideogram",
        "prompt": "Family at airport with luggage, kids excited, parents smiling, 'FAMILY VACATION SECURED' headline, bright cheerful colors, 'Trip cancellation, baggage loss, medical - all covered', lifestyle photography, professional marketing",
        "icon": "🧳",
        "color": "bright"
    },
    {
        "id": 24,
        "category": "Travel Insurance",
        "category_id": "travel",
        "title": "Student Visa",
        "style": "Student",
        "tool": "Microsoft Designer",
        "prompt": "Young student with backpack at international university, 'STUDENT VISA INSURANCE' headline, modern blue and white design, 'Mandatory for visa approval' badge, professional education-focused insurance poster",
        "icon": "🎓",
        "color": "blue"
    },
    {
        "id": 25,
        "category": "Travel Insurance",
        "category_id": "travel",
        "title": "Explore India",
        "style": "Domestic",
        "tool": "Ideogram",
        "prompt": "Iconic Indian destinations collage (Taj Mahal, Goa beach, Kerala backwaters), 'EXPLORE INDIA SAFELY' headline, vibrant Indian colors, 'Domestic Travel Insurance @ ₹49 only' pricing, professional Indian tourism poster style",
        "icon": "🕌",
        "color": "vibrant"
    },
    
    # 🛡️ TERM LIFE INSURANCE (5)
    {
        "id": 26,
        "category": "Term Life",
        "category_id": "term",
        "title": "Family Shield",
        "style": "Emotional",
        "tool": "Ideogram",
        "prompt": "Father hugging children, protective shield around them with soft glow, 'AAPKE BAAD BHI, PARIVAAR SURAKSHIT' Hindi emotional headline, warm blue and gold tones, '1 Crore cover @ ₹500/month' pricing, professional emotional insurance poster",
        "icon": "🛡️",
        "color": "blue"
    },
    {
        "id": 27,
        "category": "Term Life",
        "category_id": "term",
        "title": "Future Path",
        "style": "Future",
        "tool": "Ideogram",
        "prompt": "Path leading to bright future with family silhouettes walking, sunrise lighting, 'BUILD A SECURE FUTURE' headline, hopeful inspiring design, blue gradient, 'Term Insurance' badge, professional life insurance marketing poster",
        "icon": "🌅",
        "color": "gradient"
    },
    {
        "id": 28,
        "category": "Term Life",
        "category_id": "term",
        "title": "Young Professional",
        "style": "Young Pro",
        "tool": "Ideogram",
        "prompt": "Young Indian professional couple in modern apartment looking at laptop, 'PLAN TODAY, SECURE TOMORROW' headline, contemporary lifestyle setting, 'Term Plan for under 30' pricing, modern professional insurance poster",
        "icon": "💼",
        "color": "modern"
    },
    {
        "id": 29,
        "category": "Term Life",
        "category_id": "term",
        "title": "Tax Saving Combo",
        "style": "Tax",
        "tool": "Microsoft Designer",
        "prompt": "Calculator, tax forms, and money savings illustration, 'SAVE TAX + PROTECT FAMILY' dual headline, green and gold color scheme, 'Section 80C benefits' badge, professional tax-saving insurance poster, infographic style",
        "icon": "💰",
        "color": "green"
    },
    {
        "id": 30,
        "category": "Term Life",
        "category_id": "term",
        "title": "With vs Without",
        "style": "Comparison",
        "tool": "Microsoft Designer",
        "prompt": "Before-after comparison style poster: 'WITHOUT INSURANCE' vs 'WITH INSURANCE' split design, family stress vs family secure, 'Just ₹500/month difference' caption, smart marketing poster, professional comparison layout",
        "icon": "⚖️",
        "color": "split"
    }
]


# ============================================================
# 🔧 HELPER FUNCTIONS
# ============================================================
def get_random_poster():
    """Get a random poster (for daily rotation)"""
    return random.choice(POSTERS_LIBRARY)


def get_poster_by_id(poster_id):
    """Get specific poster by ID"""
    for poster in POSTERS_LIBRARY:
        if poster['id'] == poster_id:
            return poster
    return None


def get_posters_by_category(category_id):
    """Get all posters in a category"""
    return [p for p in POSTERS_LIBRARY if p['category_id'] == category_id]


def get_categories():
    """Get unique categories"""
    seen = set()
    categories = []
    for p in POSTERS_LIBRARY:
        if p['category_id'] not in seen:
            seen.add(p['category_id'])
            categories.append({
                "id": p['category_id'],
                "name": p['category'],
                "icon": p['icon']
            })
    return categories
