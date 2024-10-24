from datetime import datetime
from pathlib import Path
import pandas as pd

from src.api_methods import get_methods
from src.api_methods import authorize
from src.data_preprocessing import main as data_prep


def main():
    token:str = authorize.get_acces_token()
    dfs_to_concat = []
    page_number = 1
    while True:
        data:dict = get_methods.access_activity_data(token, params={
            'per_page': 200,
            'page': page_number,
        })
        page_number += 1
        cur_df = data_prep.preprocess_data(data)
        dfs_to_concat.append(cur_df)
        if len(data) == 0:
            break
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    df = pd.concat(dfs_to_concat, ignore_index=True)
    df.to_csv(Path('data', f'my_activity_data={timestamp}.csv'), index=False)


if __name__ == '__main__':
    main()