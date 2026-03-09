"""
Agno-based advisor agent for UAE Market Expansion.
Single lead agent with all tools — most cost-efficient architecture.
"""

import os
import sys
import inspect
from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.market_tools import (
    get_location_recommendations,
    get_competitor_analysis,
    get_menu_strategy,
    get_pricing_strategy,
    get_marketing_plan,
    get_operations_info,
    get_full_expansion_brief,
)
from knowledge.uae_market import SYSTEM_PROMPT, get_knowledge_summary

# Use gpt-4o-mini for cost efficiency; upgrade to gpt-4o for more complex queries
MODEL_ID = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def _make_model():
    return OpenAIChat(
        id=MODEL_ID,
        api_key=os.environ["OPENAI_API_KEY"],
    )


LEAD_ADVISOR_INSTRUCTIONS = f"""
You are the Lead UAE Market Expansion Advisor for a Jordanian restaurant expanding into Dubai and Abu Dhabi.

{SYSTEM_PROMPT}

## Your Approach:
1. Understand what the executive is asking
2. Use your tools to get relevant grounded data
3. If the question spans multiple domains, gather data from multiple tools
4. Synthesize into a clear, structured executive-friendly response
5. Always end with 1-3 concrete "Next Steps" the team can act on immediately

## Knowledge Summary (always available):
{get_knowledge_summary()}

## Cost Efficiency Rules:
- Use tools to get structured data FIRST, then reason over it
- Don't make multiple redundant tool calls for the same data
- For broad questions, use get_full_expansion_brief() once rather than multiple specific calls
"""


def _get_supported_kwargs() -> set:
    """Inspect Agent.__init__ to find which kwargs are actually supported."""
    try:
        sig = inspect.signature(Agent.__init__)
        return set(sig.parameters.keys())
    except Exception:
        return set()


def get_advisor_team() -> Agent:
    """
    Returns the lead advisor agent with all tools.
    Detects available Agent kwargs at runtime to stay compatible across Agno versions.
    """
    supported = _get_supported_kwargs()

    # Base kwargs that are stable across versions
    kwargs = dict(
        name="UAE Expansion Lead Advisor",
        model=_make_model(),
        tools=[
            get_location_recommendations,
            get_competitor_analysis,
            get_menu_strategy,
            get_pricing_strategy,
            get_marketing_plan,
            get_operations_info,
            get_full_expansion_brief,
        ],
        instructions=LEAD_ADVISOR_INSTRUCTIONS,
        markdown=True,
    )

    # Add history kwargs only if the installed version supports them
    if "add_history_to_messages" in supported:
        kwargs["add_history_to_messages"] = True
    if "num_history_responses" in supported:
        kwargs["num_history_responses"] = 6

    lead_advisor = Agent(**kwargs)
    return lead_advisor
