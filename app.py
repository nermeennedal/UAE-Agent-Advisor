"""
Streamlit UI for UAE Market Expansion Advisor
"""

import os
import sys
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="UAE Market Expansion Advisor",
    page_icon="🍕",
    layout="wide",
)

# ── Styling ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0f1117; }
    .stChatMessage { border-radius: 12px; margin-bottom: 8px; }
    .advisor-header {
        background: linear-gradient(135deg, #1a1f2e, #2d3748);
        padding: 24px 32px;
        border-radius: 16px;
        border-left: 4px solid #f6ad55;
        margin-bottom: 24px;
    }
    .topic-badge {
        display: inline-block;
        background: #2d3748;
        color: #f6ad55;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 13px;
        margin: 3px;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="advisor-header">
    <h1 style="color:#f6ad55; margin:0; font-size:28px;">UAE Market Expansion Advisor</h1>
    <p style="color:#a0aec0; margin:6px 0 0 0;">Jordanian Restaurant — Dubai & Abu Dhabi Entry Strategy</p>
</div>
""", unsafe_allow_html=True)

# ── Topic badges ───────────────────────────────────────────────────────────────
topics = [
    "Locations", "Competitors", "Menu Strategy", "Pricing",
    "Marketing", "Licensing", "Delivery", "Ramadan Strategy",
    "Staffing", "Suppliers", "Financials"
]
badges = " ".join([f'<span class="topic-badge">{t}</span>' for t in topics])
st.markdown(f"<div style='margin-bottom:20px'>{badges}</div>", unsafe_allow_html=True)

# ── Initialize agent ───────────────────────────────────────────────────────────
@st.cache_resource
def load_advisor():
    from agents.advisor import get_advisor_team
    return get_advisor_team()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "advisor" not in st.session_state:
    with st.spinner("Initializing advisor..."):
        st.session_state.advisor = load_advisor()

# ── Suggested questions ────────────────────────────────────────────────────────
if not st.session_state.messages:
    st.markdown("#### Suggested Questions")
    suggested = [
        "Where should we open our first branch in Dubai?",
        "Who are our main competitors in UAE?",
        "What menu changes do we need for the UAE market?",
        "How should we prepare for Ramadan?",
        "What licenses do we need in Abu Dhabi?",
        "What's our recommended pricing strategy?",
    ]
    cols = st.columns(3)
    for i, q in enumerate(suggested):
        if cols[i % 3].button(q, key=f"sq_{i}", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": q})
            st.rerun()

# ── Chat history ───────────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🧑‍💼" if msg["role"] == "user" else "🍕"):
        st.markdown(msg["content"])

# ── Chat input ─────────────────────────────────────────────────────────────────
if prompt := st.chat_input("Ask your expansion question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💼"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🍕"):
        with st.spinner("Analyzing..."):
            try:
                response = st.session_state.advisor.run(prompt)
                answer = response.content if hasattr(response, "content") else str(response)
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error: {e}")

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### About")
    st.markdown("""
    AI-powered advisor for expanding a Jordanian Meaty Pizza & Kebab restaurant into **Dubai** and **Abu Dhabi**.

    Built with **Agno** + **GPT-4o-mini**.
    """)

    st.markdown("---")
    st.markdown("### Coverage")
    for t in topics:
        st.markdown(f"- {t}")

    st.markdown("---")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()