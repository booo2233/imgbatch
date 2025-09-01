from rich.console import Console
from rich.table import Table

# Create a Console object
console = Console()


# input_ext and output_ext means the input format and output format
def files_table(files, input_ext, output_ext):
    # Create a Table
    table = Table(title="files")

    # Add columns
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("format", justify="right", style="green")
    table.add_column("formated to", justify="right", style="blue")

    # Add rows
    for index, file in enumerate(files):
        table.add_row(str(index), file, input_ext, output_ext)

    return table
