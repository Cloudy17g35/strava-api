import requests

from src.api_methods import endpoints
from src.env_handler import env_variables


def get_acces_token():
    # these params needs to be passed to get access
    # token used for retrieveing actual data
    payload:dict = {
    'client_id': env_variables['CLIENT_ID'],
    'client_secret': env_variables['CLIENT_SECRET'],
    'refresh_token': env_variables['REFRESH_TOKEN'],
    'grant_type': "refresh_token",
    'f': 'json'
    }
    res = requests.post(endpoints.auth_endpoint, data=payload, verify=False)
    access_token = res.json()['access_token']
    return access_token


