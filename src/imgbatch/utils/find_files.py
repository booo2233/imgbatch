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
        list_of_files = [
            file
            for file in glob.glob(os.path.join(directory, pattern))
            if date == datetime.fromtimestamp(os.path.getmtime(file)).date()
        ]
        return list_of_files

    files = glob.glob(os.path.join(directory, pattern))

    if not files:
        raise FileNotFoundError(f"No '.{ext}' files found in {directory}")
    return files
