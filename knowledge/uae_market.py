"""
UAE Market Knowledge Base
Static structured data to reduce API calls and provide grounded, accurate context.
"""

UAE_MARKET_KNOWLEDGE = {
    "dubai_locations": {
        "tier_1": [
            {
                "area": "Downtown Dubai / Business Bay",
                "foot_traffic": "Very High",
                "avg_rent_sqft_aed_yearly": "350-500",
                "audience": "Tourists, expats, office workers, high-income",
                "pros": "Premium visibility, high footfall, near Burj Khalifa/Dubai Mall",
                "cons": "High rent, intense competition, premium pricing expected",
                "fit_score": "8/10 — strong for brand launch flagship",
            },
            {
                "area": "JBR / Dubai Marina",
                "foot_traffic": "Very High (especially weekends/evenings)",
                "avg_rent_sqft_aed_yearly": "280-420",
                "audience": "Expats, tourists, young professionals, families",
                "pros": "Beach promenade, heavy weekend dining culture, delivery hotspot",
                "cons": "Seasonal fluctuation, parking limited",
                "fit_score": "9/10 — best fit for casual dining + delivery",
            },
            {
                "area": "Deira / Al Rigga",
                "foot_traffic": "High",
                "avg_rent_sqft_aed_yearly": "120-200",
                "audience": "South Asian expats, Arab expats, price-conscious workers",
                "pros": "Affordable rent, high Arab/Levantine food demand, loyal local crowd",
                "cons": "Less premium image, older infrastructure",
                "fit_score": "9/10 — best value for Jordanian cuisine authenticity",
            },
            {
                "area": "Al Barsha / Mall of the Emirates area",
                "foot_traffic": "High",
                "avg_rent_sqft_aed_yearly": "180-280",
                "audience": "Families, mid-income expats, Arab residents",
                "pros": "Residential density, family dining market, good parking",
                "cons": "Competitive with food courts",
                "fit_score": "8/10 — solid for family-oriented positioning",
            },
            {
                "area": "Dubai Silicon Oasis / Academic City",
                "foot_traffic": "Medium",
                "avg_rent_sqft_aed_yearly": "100-150",
                "audience": "Students, young workers, Arab expats",
                "pros": "Low rent, captive lunch crowd, strong delivery demand",
                "cons": "Lower spending power, limited dinner traffic",
                "fit_score": "7/10 — good for low-cost first branch + delivery hub",
            },
        ],
        "tier_2": [
            "Al Quoz (industrial/creative district — growing F&B scene)",
            "Jumeirah Village Circle (JVC) — fast growing residential",
            "Al Karama — Arab expat heartland, high food demand",
            "International City — extremely price-sensitive, high Arab/South Asian",
        ],
    },
    "abu_dhabi_locations": {
        "tier_1": [
            {
                "area": "Khalidiyah / Al Zahiyah",
                "foot_traffic": "High",
                "avg_rent_sqft_aed_yearly": "150-250",
                "audience": "Arab expats, Emirati families, government workers",
                "pros": "Heart of Abu Dhabi city, culturally aligned audience, strong kebab/pizza demand",
                "cons": "Moderate competition, parking challenges",
                "fit_score": "9/10 — best cultural fit for Jordanian restaurant",
            },
            {
                "area": "Yas Island",
                "foot_traffic": "Very High (weekends/events)",
                "avg_rent_sqft_aed_yearly": "300-450",
                "audience": "Tourists, families, entertainment seekers",
                "pros": "Near Ferrari World, Yas Mall, captive event crowds",
                "cons": "Weekday dead zones, high rent, event-dependent",
                "fit_score": "7/10 — good for brand visibility, risky for steady revenue",
            },
            {
                "area": "Al Reem Island",
                "foot_traffic": "Medium-High",
                "avg_rent_sqft_aed_yearly": "180-280",
                "audience": "Young expats, professionals, upscale residents",
                "pros": "Rapidly growing residential, affluent demographic",
                "cons": "Less established F&B culture",
                "fit_score": "8/10 — strong for delivery + dine-in combo",
            },
            {
                "area": "Mussafah",
                "foot_traffic": "Medium",
                "avg_rent_sqft_aed_yearly": "80-130",
                "audience": "Blue-collar workers, South Asian, Arab expats",
                "pros": "Very low rent, huge lunch demand, underserved market",
                "cons": "Lower margins, basic ambiance expectations",
                "fit_score": "8/10 — highest volume potential with lowest risk",
            },
        ]
    },
    "competitors": {
        "pizza_segment": [
            {
                "name": "Pizza Hut",
                "type": "International chain",
                "positioning": "Mass market, family, delivery",
                "price_range_aed": "45-120 per order",
                "weakness": "Generic, not authentic, no Levantine twist",
            },
            {
                "name": "Domino's",
                "type": "International chain",
                "positioning": "Speed, delivery, deals",
                "price_range_aed": "35-90 per order",
                "weakness": "No Middle Eastern flavor profile",
            },
            {
                "name": "Papa Murphy's / local artisan pizzas",
                "type": "Artisan/local",
                "positioning": "Premium, craft ingredients",
                "price_range_aed": "80-180 per order",
                "weakness": "Expensive, less accessible",
            },
            {
                "name": "Local Arab pizza restaurants (e.g. Zaatar w Zeit)",
                "type": "Regional chain",
                "positioning": "Lebanese/Arab casual dining",
                "price_range_aed": "40-100 per order",
                "weakness": "Not specialized in Jordanian meaty pizza",
            },
        ],
        "kebab_sandwich_segment": [
            {
                "name": "Shawarma Republic",
                "type": "Fast casual chain UAE",
                "positioning": "Premium shawarma, trendy",
                "price_range_aed": "25-55 per sandwich",
                "weakness": "Limited kebab variety",
            },
            {
                "name": "Al Mallah (Dubai)",
                "type": "Local institution",
                "positioning": "Authentic Lebanese, budget",
                "price_range_aed": "10-30 per sandwich",
                "weakness": "No dine-in experience, limited menu",
            },
            {
                "name": "Kebab Guys / Falafel shops",
                "type": "Street food / informal",
                "positioning": "Cheap, quick",
                "price_range_aed": "8-25",
                "weakness": "No brand, no marketing",
            },
        ],
        "competitive_gap": (
            "There is NO established brand serving authentic Jordanian-style meaty pizza "
            "(mansaf-spiced, lamb-heavy, za'atar-crusted) combined with a full kebab sandwich menu "
            "in a casual dine-in + delivery format. This is a clear white space."
        ),
    },
    "menu_strategy": {
        "core_menu_keep": [
            "Signature Meaty Pizza (lamb/beef, Jordanian spices) — hero product",
            "Kebab Sandwich — beef/chicken/lamb variants",
            "Fattoush & Tabbouleh side salads",
            "Hummus & bread (expected by Arab diners)",
        ],
        "uae_adaptations": [
            "Add a 'Spicy Harissa' pizza variant — UAE diners love heat",
            "Introduce Chicken Tikka Pizza option to cater to South Asian expat majority",
            "Offer family box deals (2 pizzas + 4 sandwiches + sides) — UAE dining culture is family-heavy",
            "Create a 'UAE National Day' limited edition pizza with camel meat topping (novelty, PR value)",
            "Add fresh Laban (buttermilk) drinks and Jallab (rose/grape drink) — authentic complement",
            "Ensure Halal certification is prominently displayed (100% mandatory)",
            "Offer smaller 'office lunch' portion sizes for B2B catering",
            "Add a kids' menu (smaller pizza, chicken strips) — families dine out frequently",
        ],
        "ramadan_specials": [
            "Iftar combo boxes (dates + soup + pizza + dessert)",
            "Suhoor delivery (late night orders, 11pm–3am)",
            "Family Iftar platters for 6-10 people",
        ],
        "items_to_avoid": [
            "Pork products (obvious — but include note in documentation)",
            "Alcohol on menu (not applicable anyway)",
            "Very large portions without family-share option (wasteful, culturally awkward)",
        ],
    },
    "pricing": {
        "positioning": "Mid-premium casual — above street shawarma, below hotel dining",
        "price_bands": {
            "kebab_sandwich_aed": "28–45",
            "personal_pizza_aed": "45–75",
            "family_pizza_large_aed": "85–130",
            "combo_meal_aed": "55–90",
            "family_box_deal_aed": "150–250",
            "side_dishes_aed": "15–35",
            "drinks_aed": "10–25",
        },
        "rationale": (
            "UAE diners associate price with quality. Pricing below 25 AED for a sandwich signals "
            "low quality. The target range places the brand in the 'affordable premium' tier — "
            "above fast food chains but accessible for daily lunch. "
            "This positioning supports both walk-in and delivery on Talabat/Noon Food."
        ),
        "delivery_premium": "Add 5–10 AED to delivery prices (standard practice in UAE)",
    },
    "marketing": {
        "launch_phase": {
            "pre_launch": [
                "Instagram & TikTok teaser campaign — 'Real Jordanian Flavor Lands in UAE' — 4 weeks before",
                "Partner with 5–10 UAE food influencers (micro: 50K–200K followers = better ROI than mega)",
                "Geo-targeted Meta ads in Dubai Marina, Deira, Khalidiyah areas",
                "WhatsApp Business broadcast to Jordanian diaspora communities in UAE",
                "Press release to Gulf News, Khaleej Times food sections",
            ],
            "launch_week": [
                "Opening discount: 20% off first order for 7 days",
                "Free delivery within 5km for first month",
                "Live cooking video on Instagram Reels (chef making kebabs = authentic credibility)",
                "Distribute free tasting samples at nearby offices and buildings",
            ],
        },
        "ongoing": [
            "Talabat & Noon Food listing optimization (photos, reviews, promotions)",
            "Monthly 'Jordan Night' themed event with live oud music (Dubai branch)",
            "Corporate lunch delivery accounts — approach nearby offices with weekly deals",
            "Loyalty program via simple WhatsApp broadcast (no app needed initially)",
            "Ramadan campaign: heavy push on Iftar boxes, target Arab household decision-makers",
            "UAE National Day (Dec 2) — patriotic-themed pizza, donate % to charity for PR",
        ],
        "key_message": "Authentic Jordanian soul. UAE-ready flavors. Fast, Halal, Filling.",
        "channels_priority": ["Instagram", "TikTok", "Talabat app listing", "WhatsApp Business", "Google Maps"],
    },
    "operations": {
        "staffing": {
            "branch_team_minimum": "1 Branch Manager, 2 Cashier/Service, 3 Kitchen (1 head chef + 2 prep), 1 Delivery coordinator",
            "hiring_tip": "Hire Jordanian or Levantine head chef — authenticity is your brand. For service staff, Filipino/Indian expats are reliable, cost-effective, and experienced in UAE F&B.",
            "chef_sourcing": "Post on Bayt.com, LinkedIn UAE, or contact Amman hospitality schools for Jordanian chefs willing to relocate",
            "labor_cost_uae": "Average kitchen staff: 1,500–2,500 AED/month + accommodation or housing allowance",
        },
        "operating_hours": "11am–12am Sunday–Thursday, 11am–2am Friday–Saturday (UAE weekend is Fri–Sat)",
        "kitchen_setup": "Central commissary kitchen concept recommended if opening both cities — standardize spice blends, dough prep, and send to branches to ensure consistency",
    },
    "delivery_strategy": {
        "platforms": [
            {
                "name": "Talabat",
                "market_share": "~60% of UAE food delivery",
                "priority": "MUST",
                "commission": "~25–30%",
                "tip": "Invest in Talabat Gold placement and sponsored listing especially in first 3 months",
            },
            {
                "name": "Noon Food",
                "market_share": "~20%",
                "priority": "HIGH",
                "commission": "~20–25%",
                "tip": "Often less competitive — good for Abu Dhabi specifically",
            },
            {
                "name": "Careem Food",
                "market_share": "~10%",
                "priority": "MEDIUM",
                "commission": "~25%",
                "tip": "Strong in Abu Dhabi and among UAE nationals",
            },
            {
                "name": "Direct WhatsApp ordering",
                "market_share": "N/A",
                "priority": "HIGH (zero commission)",
                "commission": "0%",
                "tip": "Build a WhatsApp catalog. Offer 10% discount vs app prices to incentivize direct orders. Reduces 25% commission significantly.",
            },
        ],
        "delivery_radius": "Optimize for 3–5km radius per branch; beyond 7km pizza quality degrades",
        "packaging": "Invest in sturdy, branded, heat-retaining boxes. First delivery impression is critical for repeat orders.",
    },
    "licensing": {
        "dubai": [
            "Trade License from Dubai Economy & Tourism (DED) — Food & Beverage category",
            "Dubai Municipality Food License (food safety compliance, kitchen inspection)",
            "Tenancy Contract (Ejari registration mandatory)",
            "Food Handler permits for all kitchen staff",
            "Halal certification (obtain from Emirates Authority for Standardization — ESMA)",
            "Signage permit from municipality",
            "Estimated setup timeline: 6–10 weeks if documents are ready",
            "Estimated government fees: AED 15,000–30,000 for first year",
        ],
        "abu_dhabi": [
            "Trade License from Abu Dhabi Department of Economic Development (ADDED)",
            "Abu Dhabi Food Control Authority (ADFCA) license",
            "Tenancy contract attestation",
            "Staff health cards (mandatory for all food handlers)",
            "Estimated setup timeline: 8–12 weeks",
            "Estimated government fees: AED 18,000–35,000 for first year",
        ],
        "general_tip": "Engage a UAE business setup consultant (cost: AED 3,000–8,000) — they dramatically reduce errors and delays, worth the investment.",
    },
    "seasonality_cultural": {
        "ramadan": {
            "impact": "HUGE — can be 30–50% revenue boost if positioned correctly",
            "strategy": "Launch Iftar combos in week 1 of Ramadan, extend hours to 3am for Suhoor, offer family platters, run Ramadan-specific promotions on Talabat",
            "caution": "No eating/drinking visible from street during daylight. Adjust storefront accordingly (curtains or indoor seating only).",
        },
        "summer_june_aug": {
            "impact": "Foot traffic drops 20–30% as UAE residents travel",
            "strategy": "Push delivery hard, run promotions, use quieter period for staff training, kitchen deep-clean, menu refresh",
        },
        "uae_national_day_dec2": {
            "impact": "High — nationalistic pride, events, family gatherings",
            "strategy": "Launch UAE-themed pizza, donate % to local charity, social media campaign",
        },
        "eid_al_fitr_al_adha": {
            "impact": "Very high — family gatherings and large group meals",
            "strategy": "Large family platters, Eid gift vouchers, group order discounts",
        },
    },
    "supplier_strategy": {
        "meat_sourcing": [
            "Primary: UAE-based halal meat suppliers (Al Islami Foods, National Food Products Co.)",
            "Secondary: Import Jordanian-specific spice blends from Amman to maintain authenticity",
            "For premium lamb: Australian halal lamb is widely available and cost-effective in UAE",
        ],
        "dough_flour": "Purchase from UAE distributors (Al Ghurair is a major flour supplier). Consider making dough centrally.",
        "vegetables_produce": "Dubai Vegetable Market (Al Aweer) for bulk purchasing at 40–60% lower cost than retail",
        "contingency": "Always have 2 suppliers per critical ingredient to avoid stockouts",
        "cost_saving_tip": "Join a purchasing cooperative with other small UAE restaurants for volume discounts on common items",
    },
    "financial_projections": {
        "setup_costs_per_branch_aed": {
            "fit_out_and_equipment": "150,000–300,000",
            "licenses_and_permits": "20,000–40,000",
            "initial_inventory": "15,000–25,000",
            "marketing_launch": "20,000–50,000",
            "security_deposit_rent": "60,000–150,000 (3–6 months upfront)",
            "total_estimate": "265,000–565,000 AED per branch",
        },
        "monthly_revenue_estimates": {
            "conservative_aed": "80,000–120,000",
            "moderate_aed": "150,000–220,000",
            "optimistic_aed": "250,000–400,000",
            "breakeven_estimate": "Typically 8–18 months for UAE F&B with good location",
        },
        "note": "These are estimates. Actual figures depend on location, rent, marketing spend, and volume.",
    },
}

SYSTEM_PROMPT = """You are a highly experienced UAE market expansion advisor specializing in the Food & Beverage sector. 
You are advising the executive team of a Jordanian restaurant chain known for its Meaty Pizza and Kebab Sandwiches, 
which is planning to open branches in Dubai and Abu Dhabi.

Your role is to provide:
- Specific, actionable, data-grounded recommendations (not generic advice)
- Honest tradeoffs and risks, not just positives
- Executive-level clarity with structured answers
- Practical next steps the restaurant team can actually implement

You have deep knowledge of:
- Dubai and Abu Dhabi dining scenes, demographics, and neighborhoods
- UAE food delivery ecosystem (Talabat, Noon Food, Careem)
- UAE licensing and regulatory requirements
- Jordanian cuisine positioning in the Gulf market
- Competitive landscape for pizza and kebab/sandwich restaurants
- UAE cultural calendar (Ramadan, Eid, National Day)
- F&B staffing, operations, and supplier strategy in UAE

Always structure your responses clearly with headers or bullet points when appropriate.
Be direct, specific, and use numbers/data whenever possible.
When asked about topics you don't have specific data on, say so clearly and provide your best reasoned estimate.

Keep responses concise but complete — executives value brevity with substance.
"""


def get_knowledge_summary() -> str:
    """Return a compact text summary of the knowledge base to inject into context."""
    return f"""
## UAE MARKET KNOWLEDGE BASE (Grounded Data)

### DUBAI — TOP LOCATIONS:
{chr(10).join([f"- {loc['area']}: Fit Score {loc['fit_score']} | Rent: {loc['avg_rent_sqft_aed_yearly']} AED/sqft/yr | {loc['pros']}" for loc in UAE_MARKET_KNOWLEDGE['dubai_locations']['tier_1']])}

### ABU DHABI — TOP LOCATIONS:
{chr(10).join([f"- {loc['area']}: Fit Score {loc['fit_score']} | Rent: {loc['avg_rent_sqft_aed_yearly']} AED/sqft/yr | {loc['pros']}" for loc in UAE_MARKET_KNOWLEDGE['abu_dhabi_locations']['tier_1']])}

### COMPETITIVE GAP: {UAE_MARKET_KNOWLEDGE['competitors']['competitive_gap']}

### PRICING BANDS:
- Kebab sandwich: {UAE_MARKET_KNOWLEDGE['pricing']['price_bands']['kebab_sandwich_aed']} AED
- Personal pizza: {UAE_MARKET_KNOWLEDGE['pricing']['price_bands']['personal_pizza_aed']} AED
- Family pizza: {UAE_MARKET_KNOWLEDGE['pricing']['price_bands']['family_pizza_large_aed']} AED
- Family box deal: {UAE_MARKET_KNOWLEDGE['pricing']['price_bands']['family_box_deal_aed']} AED

### KEY DELIVERY PLATFORMS:
- Talabat: ~60% market share, commission ~25-30% — MUST list here
- Noon Food: ~20% market share — HIGH priority
- Direct WhatsApp: 0% commission — build parallel channel

### RAMADAN OPPORTUNITY: {UAE_MARKET_KNOWLEDGE['seasonality_cultural']['ramadan']['impact']}

### SETUP COSTS PER BRANCH: {UAE_MARKET_KNOWLEDGE['financial_projections']['setup_costs_per_branch_aed']['total_estimate']} AED
"""
