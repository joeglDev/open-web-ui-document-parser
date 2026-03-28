import requests
from api.utils.get_env_variables import get_env_variables


def get_completion(prompt: str):
    open_web_ui_token, base_url = get_env_variables()

    url = f"{base_url}/api/chat/completions"

    headers = {
        "Authorization": f"Bearer {open_web_ui_token}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "mistral:latest",
        "messages": [{"role": "user", "content": f"{prompt}"}],
    }

    print("Getting completion...")
    response = requests.post(url, headers=headers, json=data)
    return response.json()
