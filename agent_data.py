"""
============================================================
👥 AGENT DATA MODULE
============================================================
Phase 1: Prashant only (self-test) ✅
Phase 2: 5 active agents (add later)
============================================================
"""

PHASE_1_AGENTS = [
    {
        "ip_code": "IP000000",
        "name": "Prashant Chandratre",
        "phone": "917709446589",
        "language": "marathi",
        "city": "Pune",
        "status": "active",
        "notes": "Owner - Self Test"
    },
]

PHASE_2_AGENTS = [
    {
        "ip_code": "IP000000",
        "name": "Prashant Chandratre",
        "phone": "917709446589",
        "language": "marathi",
        "city": "Pune",
        "status": "active",
        "notes": "Owner - Self Test"
    },
    # ADD 4 MORE AGENTS LATER:
    # {
    #     "ip_code": "IP_XXX",
    #     "name": "Agent Name",
    #     "phone": "91XXXXXXXXXX",
    #     "language": "marathi",  # or "hindi"
    #     "city": "Nashik",
    #     "status": "active"
    # },
]

FULL_AGENTS = PHASE_2_AGENTS


def get_test_agents(phase="1"):
    """Get agents list based on phase"""
    phase_map = {
        "1": PHASE_1_AGENTS,
        "2": PHASE_2_AGENTS,
        "full": FULL_AGENTS
    }
    return phase_map.get(str(phase), PHASE_1_AGENTS)


def get_agent_by_phone(phone):
    """Find agent by phone number"""
    clean_phone = str(phone).replace(" ", "").replace("-", "").replace("+", "")
    
    for agent in FULL_AGENTS:
        agent_phone = str(agent['phone']).replace(" ", "").replace("-", "").replace("+", "")
        
        if agent_phone == clean_phone:
            return agent
        if agent_phone.endswith(clean_phone) or clean_phone.endswith(agent_phone):
            return agent
    
    return None


def get_active_agents():
    return [a for a in FULL_AGENTS if a.get('status', '').lower() == 'active']
