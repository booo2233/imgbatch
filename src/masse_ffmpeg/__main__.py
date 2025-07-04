import typer
from typing_extensions import Annotated
from rich.console import Console


console = Console()


app = typer.Typer()


@app.command()
def main(
    floder_name: Annotated[str, typer.Argument(help="name of the file")] = None,
    GPU: Annotated[bool, typer.Argument()] = False,
):
    if floder_name is not None:
        console.print("hello")
    else:
        console.rule(
            "[bold blue]welcome to mass ffmpeg",
        )
        console.print(
            "[red]Error no Argument [/red][blue bold]→[/blue bold] passed run messe-ffmpeg --help",
            justify="center",
        )


if __name__ == "__main__":
    app()
