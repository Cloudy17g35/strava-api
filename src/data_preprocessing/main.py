import pandas as pd


def convert_m_per_s_to_km_per_h(meters_per_sec:float) -> float:
    # Conversion factor
    conversion_factor = 3.6
    
    # Perform the conversion
    km_per_h = meters_per_sec * conversion_factor
    
    return round(km_per_h, 2)
    

def preprocess_data(data:dict):

    df = pd.json_normalize(data)
    
    columns_selected:list[str] = [
    "name",
    "has_heartrate",
    "type",
    "sport_type",
    "start_date_local",
    "moving_time",
    "elapsed_time",
    "distance",
    "total_elevation_gain",
    "achievement_count",
    "average_speed",
    "max_speed",
    "average_heartrate",
    "max_heartrate",
    ]
    
    df = df[columns_selected]
    df[["average_speed", "max_speed",]] = df[["average_speed", "max_speed",]].apply(convert_m_per_s_to_km_per_h)
    columns_mapper:dict = {
        "average_speed": "average_speed (km/h)",
        "max_speed": "max_speed (km/h)",
        "moving_time" : "moving_time (s)",
        "elapsed_time": "elapsed_time (s)",
        "distance" : "distance (m)",
        "total_elevation_gain": "total_elevation_gain (m)",
    }
    df.rename(columns=columns_mapper, inplace=True)
    return df

