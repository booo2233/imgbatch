import glob
import os
from datetime import datetime


def find_files(
    ext: str,
    directory: str,
    recurse_folder: bool = False,
    date: str = None,
) -> list:
    pattern = f"**/*.{ext}" if recurse_folder else f"*.{ext}"

    if date is not None:
        # Convert input date string (YYYY-MM-DD) to datetime.date
        try:
            target_date = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date must be in format YYYY-MM-DD")

        list_of_files = [
            file
            for file in glob.glob(
                os.path.join(directory, pattern), recursive=recurse_folder
            )
            if datetime.fromtimestamp(os.path.getmtime(file)).date() == target_date
        ]
        if not list_of_files:
            raise FileNotFoundError(f"No '.{ext}' files found in {directory} on {date}")
        return list_of_files

    # Normal search (ignore date)
    files = glob.glob(os.path.join(directory, pattern), recursive=recurse_folder)

    if not files:
        raise FileNotFoundError(f"No '.{ext}' files found in {directory}")
    return files
