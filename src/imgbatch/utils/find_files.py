import glob
import os


def find_files(ext: str, directory: str, recurse_folder: bool = False) -> list:
    pattern = f"**/*.{ext}" if recurse_folder else f"*.{ext}"
    files = glob.glob(os.path.join(directory, pattern))
    if not files:
        raise FileNotFoundError(f"No '.{ext}' files found in {directory}")
    return files
