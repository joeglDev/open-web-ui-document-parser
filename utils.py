import os
from typing import Tuple
from dotenv import load_dotenv


def get_env_variables() -> Tuple[str]:
    load_dotenv()

    open_web_ui_token =  os.getenv("OPEN_WEB_UI_TOKEN")
    base_url =  os.getenv("BASE_URL")

    if open_web_ui_token is None or open_web_ui_token is '':
        raise Exception("OPEN_WEB_UI_TOKEN environment variable is not set")

    if base_url is None or base_url is '':
        raise Exception("BASE_URL environment variable is not set")

    return open_web_ui_token, base_url