"""
Intelligent Market Expansion Advisor (UAE) — CLI Chatbot
Powered by Agno framework with multi-agent orchestration.
"""

import os
import sys
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.text import Text

load_dotenv()

console = Console()


def print_banner():
    banner = """
╔══════════════════════════════════════════════════════════════════╗
║             🍕 UAE Market Expansion Advisor 🥙                  ║
║       Jordanian Restaurant — Dubai & Abu Dhabi Entry             ║
╚══════════════════════════════════════════════════════════════════╝
    """
    console.print(Panel(banner.strip(), style="bold green"))
    console.print(
        "\n[bold cyan]Welcome, Executive.[/bold cyan] Ask me anything about expanding "
        "your Meaty Pizza & Kebab restaurant into Dubai or Abu Dhabi.\n"
    )
    console.print("[dim]Topics I cover:[/dim]")
    topics = [
        "📍 Best locations & areas to open branches",
        "🏆 Competitor analysis & positioning",
        "🍽️  Menu strategy & localization",
        "💰 Price ranges & positioning",
        "📣 Marketing strategies & launch plans",
        "⚙️  Operations & staffing",
        "🛵 Delivery platform strategy",
        "📜 Licensing & legal basics",
        "🌙 Cultural seasonality (Ramadan, etc.)",
        "🔗 Supplier & supply chain strategy",
        "💡 General UAE market insights",
    ]
    for t in topics:
        console.print(f"  {t}")
    console.print("\n[dim]Type 'exit' or 'quit' to end the session.[/dim]\n")


def run_advisor():
    """Main CLI loop."""
    from agents.advisor import get_advisor_team

    print_banner()

    advisor = get_advisor_team()

    console.print("[bold yellow]Initializing advisor agents...[/bold yellow]")
    console.print("[green]✓ Advisor ready.[/green]\n")

    history = []

    while True:
        try:
            user_input = Prompt.ask("[bold blue]You[/bold blue]").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\n[yellow]Session ended. Good luck with your expansion![/yellow]")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit", "bye"):
            console.print("[yellow]Session ended. Good luck with your expansion![/yellow]")
            break

        history.append(user_input)

        console.print("\n[bold green]Advisor[/bold green] [dim](thinking...)[/dim]")

        try:
            response = advisor.run(user_input)
            # Extract text from response
            if hasattr(response, "content"):
                answer = response.content
            else:
                answer = str(response)

            console.print(Panel(Markdown(answer), title="[bold green]Advisor Response[/bold green]", border_style="green"))
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
            console.print("[dim]Please try rephrasing your question.[/dim]")

        console.print()


if __name__ == "__main__":
    run_advisor()
