import requests

from api.schemas.FileMetadata import FileMetadata
from .utils.get_env_variables import get_env_variables


def get_files() -> list[FileMetadata]:
    open_web_ui_token, base_url = get_env_variables()

    url = f"{base_url}/api/v1/files/?content=false"

    headers = {
        "Authorization": f"Bearer {open_web_ui_token}",
        "Content-Type": "application/json",
    }

    print("Getting files...")
    response = requests.get(url, headers=headers)
    return response.json()
