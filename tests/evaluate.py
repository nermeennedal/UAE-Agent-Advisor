"""
Evaluation script — runs 10 executive-style questions and logs results.
Usage: python tests/evaluate.py
Outputs: tests/evaluation_results.md
"""

import os
import sys
import time
import json
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()

TEST_QUESTIONS = [
    {
        "id": 1,
        "category": "Location Strategy",
        "question": "Where should we open our first branch in Dubai, and why? Give me your top 2 recommendations with pros and cons.",
    },
    {
        "id": 2,
        "category": "Location Strategy",
        "question": "Compare opening in Deira vs Dubai Marina. Which is better for us as a Jordanian meaty pizza brand?",
    },
    {
        "id": 3,
        "category": "Competitor Analysis",
        "question": "Who are our main competitors in Dubai for pizza and kebab? What's our competitive advantage?",
    },
    {
        "id": 4,
        "category": "Menu Strategy",
        "question": "What changes should we make to our menu for the UAE market? What should we add, keep, or remove?",
    },
    {
        "id": 5,
        "category": "Pricing",
        "question": "What prices should we charge for our kebab sandwiches and pizzas in Dubai? How should we position vs competitors?",
    },
    {
        "id": 6,
        "category": "Marketing",
        "question": "Give me a 30-day launch marketing plan for our Dubai opening. Include digital and offline channels.",
    },
    {
        "id": 7,
        "category": "Operations",
        "question": "What licenses do we need to open a restaurant in Abu Dhabi? What are the main steps and costs?",
    },
    {
        "id": 8,
        "category": "Delivery Strategy",
        "question": "Should we list on Talabat? What about other delivery apps? How do we reduce commission costs?",
    },
    {
        "id": 9,
        "category": "Seasonality",
        "question": "How should we prepare for Ramadan? What special offers and operational changes do you recommend?",
    },
    {
        "id": 10,
        "category": "Financial",
        "question": "What's the estimated total investment to open one branch in Dubai? And when can we expect to break even?",
    },
]


def run_evaluation():
    """Run all test questions and save results."""
    from agents.advisor import get_advisor_team

    print("=" * 60)
    print("UAE Market Expansion Advisor — Evaluation Run")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    advisor = get_advisor_team()
    results = []

    for test in TEST_QUESTIONS:
        print(f"\n[{test['id']}/10] Category: {test['category']}")
        print(f"Question: {test['question'][:80]}...")

        start_time = time.time()
        try:
            response = advisor.run(test["question"])
            elapsed = time.time() - start_time

            if hasattr(response, "content"):
                answer = response.content
            else:
                answer = str(response)

            results.append({
                "id": test["id"],
                "category": test["category"],
                "question": test["question"],
                "answer": answer,
                "elapsed_seconds": round(elapsed, 2),
                "status": "success",
                "answer_length_chars": len(answer),
            })
            print(f"  ✓ Answered in {elapsed:.1f}s ({len(answer)} chars)")

        except Exception as e:
            elapsed = time.time() - start_time
            results.append({
                "id": test["id"],
                "category": test["category"],
                "question": test["question"],
                "answer": f"ERROR: {str(e)}",
                "elapsed_seconds": round(elapsed, 2),
                "status": "error",
            })
            print(f"  ✗ Error: {e}")

        # Small delay to be respectful of rate limits
        time.sleep(1)

    # Save results as markdown
    _save_results_markdown(results)
    # Also save raw JSON
    _save_results_json(results)

    print("\n" + "=" * 60)
    successes = sum(1 for r in results if r["status"] == "success")
    print(f"Evaluation complete: {successes}/{len(results)} questions answered successfully")
    print("Results saved to: tests/evaluation_results.md")


def _save_results_markdown(results: list):
    """Save results as a readable markdown file."""
    output_path = Path(__file__).parent / "evaluation_results.md"

    lines = [
        "# Evaluation Results — UAE Market Expansion Advisor\n",
        f"**Run Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        f"**Total Questions:** {len(results)}\n",
        f"**Success Rate:** {sum(1 for r in results if r['status'] == 'success')}/{len(results)}\n\n",
        "---\n",
    ]

    for r in results:
        lines.append(f"## Q{r['id']}: {r['category']}\n")
        lines.append(f"**Question:** {r['question']}\n\n")
        lines.append(f"**Status:** {r['status']} | **Time:** {r['elapsed_seconds']}s\n\n")
        lines.append(f"**Answer:**\n\n{r['answer']}\n\n")
        lines.append("---\n\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def _save_results_json(results: list):
    """Save raw results as JSON."""
    output_path = Path(__file__).parent / "evaluation_results.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    run_evaluation()
