import os
from environs import Env


def _load_env_variables() -> dict:
    # Load environment variables from .env file
    env = Env()
    env.read_env()

    # Get environment variables from .env file
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    REFRESH_TOKEN = os.environ.get('REFRESH_TOKEN')

    env_variables:dict = {
        'CLIENT_ID': CLIENT_ID,
        'CLIENT_SECRET': CLIENT_SECRET,
        'REFRESH_TOKEN': REFRESH_TOKEN
    }

    return env_variables


env_variables = _load_env_variables()

# Function to check if environment variables are set
def check_env_variables(env_variables_list: list) -> [None, ValueError]:
    if None in env_variables_list:
        raise ValueError("Environment variables weren't retrieved properly")


CLIENT_ID = env_variables['CLIENT_ID']
CLIENT_SECRET = env_variables['CLIENT_SECRET']
REFRESH_TOKEN = env_variables['REFRESH_TOKEN']


env_variables_to_check = [
    CLIENT_ID or None,
    CLIENT_SECRET or None,
    REFRESH_TOKEN or None
]


check_env_variables(env_variables_to_check)