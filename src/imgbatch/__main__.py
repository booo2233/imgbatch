import typer
from typing_extensions import Annotated
from rich.console import Console
from pathlib import Path
from typing import Optional
from .image_conversion import convert_file, zip_conversion
from .utils.find_files import find_files
from .utils.tables import files_table
import concurrent.futures
import itertools
import os
from yaspin import yaspin

console = Console()
app = typer.Typer(no_args_is_help=True)

spinner = yaspin()


def normalize_path(p: Optional[str]) -> Path:
    return Path(p).expanduser().resolve(strict=False) if p else Path.cwd()


def _process_and_convert_files(input_format, output_format, directory, recurse, delete):
    spinner.start()

    files = find_files(input_format, directory, recurse)
    with concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        results = list(
            executor.map(
                convert_file,
                itertools.repeat(input_format),
                itertools.repeat(output_format),
                files,
                itertools.repeat(delete),
            )
        )
    spinner.stop()
    return results


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
        results = _process_and_convert_files(
            input_format, output_format, directory_path, recurse, delete
        )
        console.print(files_table(results, output_format, input_format))
    except FileNotFoundError as e:
        console.print(str(e), style="red")
        raise typer.Exit(code=1)


@app.command("zip")
def process_images_to_zip(
    input_format: Annotated[
        str, typer.Option(..., "--input", "-i", help="Input format (e.g., webp)")
    ],
    output_format: Annotated[
        str, typer.Option(..., "--output", "-o", help="Output format (e.g., png)")
    ],
    file_name: Optional[str] = typer.Option(
        None,
        "--zipname",
        "-zn",
        help="name of the zip file (default: time date format eg:12:45:15-3-9-2025.zip)",
    ),
    image_directory: Optional[str] = typer.Option(
        None, "--directory", "-f", help="Folder to look in (default: current directory)"
    ),
    delete: Optional[bool] = typer.Option(
        False, "--delete", "-d", help="delete the image after convertion"
    ),
    recurse: bool = typer.Option(
        False, "--recurse", "-r", help="Also search subdirectories recursively"
    ),
):
    directory_path = normalize_path(image_directory)
    if not directory_path.exists() or not directory_path.is_dir():
        console.print(f"[red]Directory not found:[/red] {directory_path}")
        raise typer.Exit(code=1)

    try:
        results = _process_and_convert_files(
            input_format, output_format, directory_path, recurse=False, delete=delete
        )
        console.print(files_table(results, output_format, input_format))
        archive = zip_conversion(file_name, results)
        console.print(f"[green]Created archive:[/green] {archive}")
    except FileNotFoundError as e:
        console.print(str(e), style="red")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
