import mimetypes
import os


def get_file_mime_type(file_path: str):
    mimetypes.init()
    file_name = os.path.basename(file_path).split("/")[-1]
    file_type = mimetypes.guess_type(file_name)[0]
    return file_type
