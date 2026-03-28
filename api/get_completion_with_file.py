import requests

from api.utils.get_env_variables import get_env_variables


def get_completion_with_file(prompt: str, file_id: str):
    open_web_ui_token, base_url = get_env_variables()
    url = f"{base_url}/api/chat/completions"

    headers = {
        "Authorization": f"Bearer {open_web_ui_token}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "mistral:latest",
        "messages": [{"role": "user", "content": prompt}],
        "files": [{"type": "file", "id": file_id}],
    }

    print("Getting completion...")
    response = requests.post(url, headers=headers, json=payload)
    res = response.json()

    return res["choices"][0]["message"]["content"]
