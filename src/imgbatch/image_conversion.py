from PIL import Image


# Convert one image format to another image format
def convert(
    input_ext: str,
    output_ext: str,
    file_names: list,
):
    if not file_names:
        raise FileNotFoundError(f"No {input_ext!r} files found")

    # Otherwise do the conversions
    for filepath in file_names:
        img = Image.open(filepath)
        base = filepath.rsplit(input_ext, 1)[0]  # remove only the last occurrence
        new_filename = base + output_ext
        img.save(new_filename)


if __name__ == "__main__":
    convert()
