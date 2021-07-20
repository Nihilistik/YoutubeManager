import json
from google.oauth2.credentials import Credentials

from youtube import settings


def credentials_to_dict(credentials: Credentials) -> dict:
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }


def save_credentials_to_file(credentials_as_dict: dict, path: str):
    with open(f"{path}{settings.CREDENTIALS_FILE}", "w") as file:
        json.dump(credentials_as_dict, file)


def load_credentials_from_file(path: str) -> Credentials:
    with open(f"{path}{settings.CREDENTIALS_FILE}", "r") as file:
        return Credentials(**json.load(file))
