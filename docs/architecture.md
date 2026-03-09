# Architecture Deep Dive — UAE Market Expansion Advisor

## System Design Philosophy

The advisor is built on three principles:

### 1. Ground Truth First, LLM Second
Rather than asking the LLM to "know" about UAE restaurant markets from training data (which may be outdated or hallucinated), we:
- Pre-build a structured knowledge base with researched, accurate data
- Expose this data through Python tool functions
- Let the LLM's job be **synthesis and communication**, not data generation

This results in more accurate, consistent answers and dramatically lower API costs.

### 2. Cost-Aware by Design
Every architectural decision was evaluated for cost impact:

```
Option A: Multi-agent team (5 specialists)
  → Each question spawns 3-5 agent calls
  → Cost: ~$0.03-0.15 per question

Option B: Single agent with tools (chosen)
  → Each question = 1 LLM call + tool lookups
  → Tools are free Python functions (no LLM calls)
  → Cost: ~$0.002-0.008 per question
  
Cost reduction: ~10-20x
```

### 3. Executive-Ready Output
The system is designed for time-pressed restaurant executives, not developers:
- Responses are structured with headers and bullet points
- Always include specific numbers (AED prices, timelines, percentages)
- Always end with actionable "Next Steps"
- No technical jargon or hedging

---

## Agent Design

### Lead Advisor Agent
- **Model:** gpt-4o-mini (overridable to gpt-4o via env var)
- **Memory:** Last 6 conversation turns (balances context vs cost)
- **Tools:** All 7 market data tools
- **Instructions:** 
  - Grounded system prompt with knowledge summary injected at startup
  - Explicit guidance on when to call which tool
  - Cost efficiency rules (avoid redundant tool calls)

### Why One Agent Instead of a Team?
Agno supports multi-agent teams where a lead agent delegates to specialists. We evaluated this but chose a single agent because:

1. **Cost:** Each sub-agent delegation = additional API call
2. **Latency:** Team coordination adds 1-3 seconds per delegation
3. **Complexity:** For this use case, tool-calling achieves the same result
4. **Reliability:** Fewer failure points

The specialist agents (`location_agent`, `competitor_agent`, etc.) are defined in `agents/advisor.py` for future use if a multi-agent architecture becomes warranted (e.g., for parallel research tasks).

---

## Tool Design

Tools follow a simple pattern:
```
Tool Function → Query Knowledge Base → Return JSON String → LLM Reads + Synthesizes
```

All tools are pure Python functions with no external API calls. This means:
- Zero latency for tool execution
- No additional API costs
- Deterministic, testable behavior
- No rate limit concerns

### Tool Registry
| Tool | Purpose | Typical Use |
|------|---------|------------|
| `get_location_recommendations` | Location data by city | "Where to open in Dubai?" |
| `get_competitor_analysis` | Competitor landscape | "Who are our competitors?" |
| `get_menu_strategy` | Menu localization | "What to change on our menu?" |
| `get_pricing_strategy` | Price bands + rationale | "How should we price?" |
| `get_marketing_plan` | Launch + ongoing marketing | "How to market our launch?" |
| `get_operations_info` | Ops, licensing, delivery, seasonal | "What licenses do we need?" |
| `get_full_expansion_brief` | Complete knowledge dump | "Give me a full overview" |

---

## Data Flow

```
User Input
    │
    ▼
Lead Advisor (Agno Agent)
    │
    ├─── Determine topic(s) from question
    │
    ├─── Call relevant tool(s) → Get JSON data
    │
    ├─── Reason over data in context
    │
    └─── Generate structured executive response
              │
              ▼
         Rich-formatted CLI output
```

---

## Knowledge Base Structure

The knowledge base (`knowledge/uae_market.py`) is organized as a Python dictionary with these sections:

```python
UAE_MARKET_KNOWLEDGE = {
    "dubai_locations": { "tier_1": [...], "tier_2": [...] },
    "abu_dhabi_locations": { "tier_1": [...] },
    "competitors": { "pizza_segment": [...], "kebab_sandwich_segment": [...] },
    "menu_strategy": { "core_menu_keep": [...], "uae_adaptations": [...] },
    "pricing": { "price_bands": {...}, "rationale": "..." },
    "marketing": { "launch_phase": {...}, "ongoing": [...] },
    "operations": { "staffing": {...}, "operating_hours": "..." },
    "delivery_strategy": { "platforms": [...] },
    "licensing": { "dubai": [...], "abu_dhabi": [...] },
    "seasonality_cultural": { "ramadan": {...}, "summer": {...} },
    "supplier_strategy": { "meat_sourcing": [...] },
    "financial_projections": { "setup_costs": {...}, "revenue_estimates": {...} },
}
```

---

## Conversation Memory

Agno's built-in conversation memory is used with `add_history_to_messages=True` and `num_history_responses=6`.

This means:
- Multi-turn conversations work naturally ("you mentioned Deira earlier...")
- Memory resets on process restart (stateless by design for simplicity)
- Keeping only 6 exchanges prevents context window bloat and cost inflation

For production: would add persistent storage (SQLite or Redis) to maintain sessions across restarts.

---

## Testing Strategy

The evaluation script (`tests/evaluate.py`) runs 10 pre-defined executive questions covering all major topics. For each question it measures:
- Response success/failure
- Response time
- Answer length (proxy for completeness)

Manual evaluation criteria:
1. **Specificity** — Does it give actual AED figures, area names, platform names?
2. **Accuracy** — Does it match the knowledge base data?
3. **Actionability** — Can the executive team act on this advice today?
4. **Coherence** — Does the response follow a logical structure?
