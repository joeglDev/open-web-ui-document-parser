import os


def get_file_name_from_path(file_path: str):
    file_name = os.path.basename(file_path).split("/")[-1]
    return file_name
