from src.api_methods import get_methods
from src.api_methods import authorize

def main():
    token:str = authorize.get_acces_token()
    resp:dict = get_methods.access_activity_data(token)
    


if __name__ == '__main__':
    main()