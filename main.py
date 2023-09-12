from datetime import datetime
from pathlib import Path


from src.api_methods import get_methods
from src.api_methods import authorize
from src.data_preprocessing import main as data_prep


def main():
    token:str = authorize.get_acces_token()
    data:dict = get_methods.access_activity_data(token)
    df = data_prep.preprocess_data(data)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    df.to_csv(Path('data', f'my_activity_data={timestamp}.csv'), index=False)


if __name__ == '__main__':
    main()