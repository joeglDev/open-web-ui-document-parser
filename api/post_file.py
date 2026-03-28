import requests

from .schemas.FileMetadata import FileMetadata
from api.utils.get_env_variables import get_env_variables


def post_file(file_path: str) -> FileMetadata:
    open_web_ui_token, base_url = get_env_variables()

    url = f"{base_url}/api/v1/files/"

    headers = {
        "Authorization": f"Bearer {open_web_ui_token}",
        "Content-Type": None,  # "multipart/form-data",
        "accept": "application/json",
    }

    params = {"process": "true", "process_in_background": "true"}

    files = {
        "file": open(file_path, "rb"),
    }

    response = requests.post(url, headers=headers, params=params, files=files)
    return response.json()
