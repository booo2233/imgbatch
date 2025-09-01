import typer
from typing_extensions import Annotated
from rich.console import Console
from pathlib import Path
from typing import Optional
from .image_conversion import convert
from .utils.find_files import find_files
from .utils.tables import files_table
import concurrent.futures
import itertools

console = Console()
app = typer.Typer(no_args_is_help=True)


def normalize_path(p: Optional[str]) -> Path:
    return Path(p).expanduser().resolve(strict=False) if p else Path.cwd()


@app.command("convert")
def main(
    input_format: Annotated[
        str, typer.Option(..., "--input", "-i", help="Input format (e.g., webp)")
    ],
    output_format: Annotated[
        str, typer.Option(..., "--output", "-o", help="Output format (e.g., png)")
    ],
    image_directory: Optional[str] = typer.Option(
        None, "--directory", "-f", help="Folder to look in (default: current directory)"
    ),
    recurse: bool = typer.Option(
        False, "--recurse", "-r", help="Also search subdirectories recursively"
    ),
    delete: Optional[bool] = typer.Option(
        False, "--delete", "-d", help="delete the image after convertion"
    ),
):
    directory_path = normalize_path(image_directory)

    if not directory_path.exists() or not directory_path.is_dir():
        console.print(f"[red]Directory not found:[/red] {directory_path}")
        raise typer.Exit(code=1)

    try:
        files = find_files(input_format, directory_path, recurse)

        with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
            try:
                results = list(
                    executor.map(
                        convert,
                        itertools.repeat(input_format),
                        itertools.repeat(output_format),
                        files,
                        itertools.repeat(delete),
                    )
                )
                console.print(files_table(results, output_format, input_format))
            except ValueError:
                console.print(f"Unknown format {output_format}", style="red")

    except FileNotFoundError as e:
        console.print(str(e), style="red")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
