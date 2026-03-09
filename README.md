#  Intelligent Market Expansion Advisor (UAE)
### Jordanian Restaurant — Dubai & Abu Dhabi Entry Strategy

An **agentic AI advisory system** built with [Agno](https://github.com/agno-agi/agno) and Python, providing executive-level market expansion guidance for a Jordanian Meaty Pizza & Kebab restaurant entering the UAE market.

---

##  What It Does

Ask real business questions like an executive and get structured, actionable answers:

-  **Best locations** to open in Dubai and Abu Dhabi
-  **Competitor analysis** and differentiation strategy
- ️ **Menu adaptations** for the UAE market
-  **Pricing strategy** with specific AED price bands
-  **Marketing launch plan** (digital, influencer, delivery platforms)
- ️ **Operations & staffing** guidance
-  **Delivery platform strategy** (Talabat, Noon Food, WhatsApp)
-  **Licensing & compliance** for Dubai and Abu Dhabi
-  **Ramadan & seasonal strategy**
-  **Supplier & supply chain** recommendations
-  **Financial projections** and setup cost estimates

---

## ️ Architecture Overview

```
┌─────────────────────────────────────────────────┐
│                  main.py (CLI)                   │
│           Rich-powered chat interface            │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│           Lead Advisor Agent (Agno)              │
│         Model: gpt-4o-mini (cost-aware)          │
│         Multi-turn conversation memory           │
└─────────────────┬───────────────────────────────┘
                  │  calls
          ┌───────┴────────┐
          ▼                ▼
┌─────────────────┐  ┌──────────────────────────────┐
│  Market Tools   │  │   UAE Knowledge Base          │
│  (Python funcs) │  │   (static structured data)    │
│                 │  │                               │
│ • get_locations │  │ • Dubai/Abu Dhabi locations   │
│ • competitors   │  │ • Competitors                 │
│ • menu_strategy │  │ • Menu & pricing data         │
│ • pricing       │  │ • Marketing plans             │
│ • marketing     │  │ • Licensing requirements      │
│ • operations    │  │ • Financial projections       │
│ • full_brief    │  │ • Seasonal calendar           │
└─────────────────┘  └──────────────────────────────┘
```

### Key Design Decisions

1. **Single Lead Agent (not multi-agent team)** — A team of specialist agents would multiply API costs (each sub-agent makes its own LLM calls). Instead, one capable lead agent with all tools is more cost-efficient and equally effective for this use case.

2. **Static Knowledge Base** — Core market data (locations, pricing, competitors, licensing) is stored as Python dictionaries. The LLM reads this data via tools, then reasons over it — dramatically reducing hallucination and cost vs. asking the LLM to generate this from training data.

3. **gpt-4o-mini by default** — Provides excellent reasoning at ~10x lower cost than gpt-4o. Can be overridden via environment variable for higher-stakes queries.

4. **Conversation history** — The agent retains the last 6 exchanges, enabling natural multi-turn conversations without re-explaining context.

5. **Tools as data fetchers** — Tools return structured JSON from the knowledge base. The LLM synthesizes and presents this data in executive-friendly format. This pattern avoids unnecessary LLM calls for data retrieval.

---

##  Quick Start

### Prerequisites
- Python 3.10+
- OpenAI API key

### Installation

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd uae-advisor

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# 5. Run the advisor
python main.py
```

### Example Session

```
You: Where should we open our first Dubai branch?

Advisor: Based on your brand profile (Jordanian meaty pizza + kebab, 
mid-premium positioning), here are my top 2 recommendations...

## 1. Deira / Al Rigga ⭐ Top Pick
- Rent: 120–200 AED/sqft/year (most affordable prime area)
- Audience: Arab expats, Levantine diaspora — YOUR natural customer
- Fit Score: 9/10
...

You: What about pricing for the kebab sandwiches?

Advisor: For kebab sandwiches in UAE, I recommend pricing at 28–45 AED...
```

---

##  Cost Control Strategy

| Strategy | Implementation |
|----------|----------------|
| **gpt-4o-mini default** | 10x cheaper than gpt-4o, excellent for structured advisory |
| **Static knowledge base** | Tools return pre-written data, not LLM-generated |
| **Limited conversation history** | Only last 6 exchanges kept (not unlimited) |
| **Single agent vs team** | Avoids 4-5x API cost multiplication from multi-agent |
| **One tool call per query** | Instructions guide agent to call `get_full_expansion_brief()` for broad questions rather than 5 separate calls |

**Estimated cost per question:** $0.002–0.008 (gpt-4o-mini)  
**Full evaluation run (10 questions):** ~$0.05–0.10

---

##  Project Structure

```
uae-advisor/
├── main.py                  # CLI entry point
├── requirements.txt
├── .env.example
├── README.md
├── agents/
│   ├── __init__.py
│   └── advisor.py           # Agno agent definitions
├── tools/
│   ├── __init__.py
│   └── market_tools.py      # Tool functions (data fetchers)
├── knowledge/
│   ├── __init__.py
│   └── uae_market.py        # Static UAE market knowledge base
├── tests/
│   ├── __init__.py
│   ├── evaluate.py          # Evaluation script
│   └── evaluation_results.md  # Auto-generated after running eval
└── docs/
    └── architecture.md      # Detailed architecture notes
```

---

##  Evaluation

Run the automated evaluation with 10 pre-defined executive questions:

```bash
python tests/evaluate.py
```

Results are saved to `tests/evaluation_results.md` and `tests/evaluation_results.json`.

### Test Questions Covered

| # | Category | Question Summary |
|---|----------|-----------------|
| 1 | Location | Top 2 Dubai branch locations with pros/cons |
| 2 | Location | Deira vs Dubai Marina comparison |
| 3 | Competitors | Main competitors and competitive advantage |
| 4 | Menu | UAE menu adaptations |
| 5 | Pricing | Kebab and pizza price recommendations |
| 6 | Marketing | 30-day Dubai launch plan |
| 7 | Operations | Abu Dhabi licensing requirements |
| 8 | Delivery | Talabat strategy and commission reduction |
| 9 | Seasonality | Ramadan preparation strategy |
| 10 | Financial | Investment estimate and break-even |

---

##  What Works Well

- **Location recommendations** — Very specific, grounded in real UAE neighborhoods with accurate rent ranges
- **Competitor analysis** — Identifies genuine white space (no authentic Jordanian pizza+kebab brand in UAE)
- **Pricing** — Specific AED figures with rationale, not vague ranges
- **Ramadan strategy** — Detailed and culturally aware
- **Multi-turn context** — Remembers earlier parts of conversation

## ️ Limitations

- **Market data is static** — Knowledge base was built from research up to early 2025. Rent prices and competitor landscape evolve. In production, connect to live data sources.
- **No real-time competitor tracking** — Can't detect new entrants. Add web search tool for live data.
- **Financial projections are estimates** — Break-even estimates are rough. A real engagement would use actual lease quotes and operational cost data.
- **No multi-language support** — Advisor responds in English only. Adding Arabic would significantly expand executive usability.

##  How to Improve

1. **Add web search tool** — Connect to Talabat API, Google Maps, or web search for real-time competitor and rent data
2. **Add memory/persistence** — Store conversation history across sessions (currently resets on restart)
3. **Build web UI** — Replace CLI with a Streamlit or React frontend for non-technical executives
4. **Add PDF report generation** — "Generate a full expansion report" → download PDF
5. **Connect real financial models** — Excel/Google Sheets integration for live financial modeling
6. **Arabic language support** — Critical for Emirati and Arab executive users

---

##  AI Tool Usage Disclosure

| Tool | Usage |
|------|-------|
| **Claude (Anthropic)** | Used to help scaffold initial project structure, refine system prompts, and review code logic |
| **GPT-4o-mini (OpenAI)** | Runtime model powering advisor responses in production |

**Personally implemented:**
- All agent architecture decisions and tradeoffs
- Complete knowledge base content (researched and structured)
- Tool design pattern (tools as data fetchers, not LLM calls)
- Cost control strategy
- Evaluation framework design

---

##  License

MIT License — feel free to adapt for other market expansion use cases.