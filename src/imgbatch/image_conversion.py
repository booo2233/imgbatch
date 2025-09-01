from PIL import Image
import os
from rich import console


# Convert one image format to another image format
def convert(input_ext: str, output_ext: str, file_names: list, delete: bool):
    if not file_names:
        raise FileNotFoundError(f"No {input_ext!r} files found")

        # Otherwise do the conversions

    img = Image.open(file_names)

    base = file_names.rsplit(input_ext, 1)[0]  # remove only the last occurrence
    new_filename = base + output_ext

    img.save(new_filename)

    if delete:
        os.remove(file_names)
    return new_filename


if __name__ == "__main__":
    convert()
