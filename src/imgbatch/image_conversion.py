from PIL import Image
import zipfile
from datetime import datetime
import os
import time


now = datetime.now()


# Convert one image format to another image format
def convert_file(input_ext: str, output_ext: str, file_name: str, delete: bool):
    if not file_name:
        raise FileNotFoundError(f"No {input_ext!r} files found")
    img = Image.open(file_name)

    base, _ = os.path.splitext(file_name)
    new_filename = base + "." + output_ext

    # Skip if already exists
    if os.path.exists(new_filename):
        return new_filename
    time.sleep(2)
    img.save(new_filename)

    # Delete original if requested

    if delete:
        os.remove(file_name)

    return new_filename


def zip_conversion(zip_name: str, files: list):
    # name of the new zip file
    if zip_name is None:
        zip_name = now.strftime("%H-%M-%S_%d-%m-%Y.zip")
    if not zip_name.endswith(".zip"):
        zip_name = zip_name + ".zip"

    # create the zip and add the files
    with zipfile.ZipFile(zip_name, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, arcname=os.path.basename(f))

    return zip_name


if __name__ == "__main__":
    zip_conversion()
    convert_file()
