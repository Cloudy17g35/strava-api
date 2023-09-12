import pandas as pd


def preprocess_data(data:dict) -> pd.DataFrame:

    return pd.json_normalize(data)

