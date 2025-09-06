from rich.prompt import IntPrompt
from rich.console import Console
from datetime import datetime


console = Console()


def ask_date():
    year = IntPrompt.ask(
        "[bold cyan]Enter year[/bold cyan]", default=datetime.now().year
    )
    month = IntPrompt.ask(
        "[bold cyan]Enter month (1-12)[/bold cyan]",
        choices=[str(i) for i in range(1, 13)],
    )
    day = IntPrompt.ask("[bold cyan]Enter day (1-31/30)[/bold cyan]")

    try:
        date = datetime(year=int(year), month=int(month), day=int(day))
        console.print(f"[green]You entered date:[/green] {date.strftime('%Y-%m-%d')}")
        return date.strftime("%Y-%m-%d")
    except ValueError as e:
        console.print(f"[red]Invalid date:[/red] {e}")
        return ask_date()  # ask again if invalid


if __name__ == "__main__":
    ask_date()
