import requests

def get_github_user(username):
    url = f"https://github.com/GreenBandYt"
    response = requests.get(url)
    if response.status_code == 200:
        user = response.json()
        return user
    else:
        return None