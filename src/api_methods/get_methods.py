import requests

from src.api_methods import endpoints


def access_activity_data(access_token:str) -> dict:
    headers:dict = {'Authorization': f'Authorization: Bearer {access_token}'}
    my_dataset:dict = requests.get(endpoints.activites_endpoint, headers=headers).json()
    return my_dataset