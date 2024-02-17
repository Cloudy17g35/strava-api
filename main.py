from datetime import datetime
from pathlib import Path


from src.api_methods import get_methods
from src.api_methods import authorize
from src.data_preprocessing import main as data_prep

# used to f.e set the limit of fetched activities (default - 30)
ACTIVITIES_PER_PAGE = 200
# current page number with activities
PAGE_NUMBER = 1


GET_ALL_ACTIVITIES_PARAMS = {
    'per_page': ACTIVITIES_PER_PAGE,
    'page': PAGE_NUMBER
}


def main():
    token:str = authorize.get_acces_token()
    data:dict = get_methods.access_activity_data(token, params=GET_ALL_ACTIVITIES_PARAMS)
    df = data_prep.preprocess_data(data)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    df.to_csv(Path('data', f'my_activity_data={timestamp}.csv'), index=False)


if __name__ == '__main__':
    main()