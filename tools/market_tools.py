"""
Custom tools for the UAE Market Expansion Advisor.
These tools provide structured data lookups to avoid unnecessary LLM calls.
"""

import json
from typing import Optional
from knowledge.uae_market import UAE_MARKET_KNOWLEDGE


def get_location_recommendations(city: str, priority: str = "all") -> str:
    """
    Get location recommendations for Dubai or Abu Dhabi.
    
    Args:
        city: 'dubai' or 'abu_dhabi'
        priority: 'tier_1', 'tier_2', or 'all'
    
    Returns:
        JSON string with location data
    """
    city_key = city.lower().replace(" ", "_").replace("-", "_")
    
    if city_key not in ("dubai", "abu_dhabi"):
        return json.dumps({"error": f"City '{city}' not supported. Use 'dubai' or 'abu_dhabi'."})
    
    locations_key = f"{city_key}_locations"
    data = UAE_MARKET_KNOWLEDGE.get(locations_key, {})
    
    if priority == "tier_1":
        return json.dumps({"city": city, "tier_1_locations": data.get("tier_1", [])}, indent=2)
    elif priority == "tier_2":
        return json.dumps({"city": city, "tier_2_locations": data.get("tier_2", [])}, indent=2)
    else:
        return json.dumps({"city": city, "locations": data}, indent=2)


def get_competitor_analysis(segment: str = "all") -> str:
    """
    Get competitor analysis data.
    
    Args:
        segment: 'pizza', 'kebab', or 'all'
    
    Returns:
        JSON string with competitor data
    """
    competitors = UAE_MARKET_KNOWLEDGE["competitors"]
    
    if segment == "pizza":
        return json.dumps({
            "segment": "pizza",
            "competitors": competitors["pizza_segment"],
            "competitive_gap": competitors["competitive_gap"]
        }, indent=2)
    elif segment == "kebab":
        return json.dumps({
            "segment": "kebab_sandwich",
            "competitors": competitors["kebab_sandwich_segment"],
            "competitive_gap": competitors["competitive_gap"]
        }, indent=2)
    else:
        return json.dumps(competitors, indent=2)


def get_menu_strategy() -> str:
    """
    Get full menu strategy and localization recommendations for UAE.
    
    Returns:
        JSON string with menu strategy
    """
    return json.dumps(UAE_MARKET_KNOWLEDGE["menu_strategy"], indent=2)


def get_pricing_strategy() -> str:
    """
    Get pricing recommendations and positioning logic for UAE market.
    
    Returns:
        JSON string with pricing data
    """
    return json.dumps(UAE_MARKET_KNOWLEDGE["pricing"], indent=2)


def get_marketing_plan(phase: str = "all") -> str:
    """
    Get marketing strategy and launch plan.
    
    Args:
        phase: 'pre_launch', 'launch', 'ongoing', or 'all'
    
    Returns:
        JSON string with marketing plan
    """
    marketing = UAE_MARKET_KNOWLEDGE["marketing"]
    
    if phase == "pre_launch":
        return json.dumps({"pre_launch": marketing["launch_phase"]["pre_launch"]}, indent=2)
    elif phase == "launch":
        return json.dumps({"launch_week": marketing["launch_phase"]["launch_week"]}, indent=2)
    elif phase == "ongoing":
        return json.dumps({"ongoing": marketing["ongoing"]}, indent=2)
    else:
        return json.dumps(marketing, indent=2)


def get_operations_info(topic: str = "all") -> str:
    """
    Get operations, staffing, and delivery platform strategy.
    
    Args:
        topic: 'staffing', 'delivery', 'licensing_dubai', 'licensing_abu_dhabi', 
               'seasonality', 'suppliers', 'financials', or 'all'
    
    Returns:
        JSON string with operations data
    """
    topic_map = {
        "staffing": UAE_MARKET_KNOWLEDGE["operations"],
        "delivery": UAE_MARKET_KNOWLEDGE["delivery_strategy"],
        "licensing_dubai": {"dubai_licensing": UAE_MARKET_KNOWLEDGE["licensing"]["dubai"]},
        "licensing_abu_dhabi": {"abu_dhabi_licensing": UAE_MARKET_KNOWLEDGE["licensing"]["abu_dhabi"]},
        "licensing": UAE_MARKET_KNOWLEDGE["licensing"],
        "seasonality": UAE_MARKET_KNOWLEDGE["seasonality_cultural"],
        "suppliers": UAE_MARKET_KNOWLEDGE["supplier_strategy"],
        "financials": UAE_MARKET_KNOWLEDGE["financial_projections"],
    }
    
    if topic in topic_map:
        return json.dumps(topic_map[topic], indent=2)
    else:
        # Return all operational data
        all_ops = {
            "operations_staffing": UAE_MARKET_KNOWLEDGE["operations"],
            "delivery_strategy": UAE_MARKET_KNOWLEDGE["delivery_strategy"],
            "licensing": UAE_MARKET_KNOWLEDGE["licensing"],
            "seasonality": UAE_MARKET_KNOWLEDGE["seasonality_cultural"],
            "suppliers": UAE_MARKET_KNOWLEDGE["supplier_strategy"],
            "financial_projections": UAE_MARKET_KNOWLEDGE["financial_projections"],
        }
        return json.dumps(all_ops, indent=2)


def get_full_expansion_brief() -> str:
    """
    Get a complete expansion brief covering all topics.
    Best used for broad 'overview' or 'full analysis' queries.
    
    Returns:
        JSON string with complete knowledge base
    """
    return json.dumps(UAE_MARKET_KNOWLEDGE, indent=2)
