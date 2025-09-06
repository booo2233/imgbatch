from rich.table import Table
from pathlib import Path


def files_table(files, input_ext, output_ext, sp_files=False):
    # Title
    title = "Select Files" if sp_files else "Files"
    table = Table(title=title)

    # Columns
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Format", justify="right", style="green")
    table.add_column("Formatted To", justify="right", style="blue")

    # Rows
    for index, file in enumerate(files):
        table.add_row(
            str(index),
            Path(file).name,  # just the filename
            input_ext,  # original format
            output_ext,  # target format
        )

    return table
