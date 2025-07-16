import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import Point

def generate_negative_samples(road_gdf, num_samples=500, time_range=None):
    samples = []
    bounds = road_gdf.total_bounds
    for _ in range(num_samples):
        x = np.random.uniform(bounds[0], bounds[2])
        y = np.random.uniform(bounds[1], bounds[3])
        if time_range:
            time = pd.to_datetime(np.random.choice(pd.date_range(time_range[0], time_range[1], freq='H')))
        else:
            time = pd.Timestamp.now()
        samples.append({'geometry': Point(x, y), 'datetime': time})
    gdf = gpd.GeoDataFrame(samples, crs=road_gdf.crs)
    return gdf

def engineer_features(acc_df, weather_df, road_gdf):
    acc_df['hour'] = acc_df['datetime'].dt.hour
    acc_df['day_of_week'] = acc_df['datetime'].dt.dayofweek
    acc_df['label'] = 1

    neg_gdf = generate_negative_samples(road_gdf, num_samples=len(acc_df),
                                        time_range=(acc_df['datetime'].min(), acc_df['datetime'].max()))
    neg_gdf['hour'] = neg_gdf['datetime'].dt.hour
    neg_gdf['day_of_week'] = neg_gdf['datetime'].dt.dayofweek
    neg_gdf['label'] = 0

    acc_df = pd.merge_asof(acc_df.sort_values('datetime'), weather_df.sort_values('datetime'),
                           on='datetime', direction='nearest', tolerance=pd.Timedelta('1H'))
    neg_df = pd.merge_asof(neg_gdf.sort_values('datetime'), weather_df.sort_values('datetime'),
                           on='datetime', direction='nearest', tolerance=pd.Timedelta('1H'))

    pos_X = acc_df[['hour', 'day_of_week']].copy()
    neg_X = neg_df[['hour', 'day_of_week']].copy()

    if 'precipitation' in acc_df.columns:
        pos_X['precipitation'] = acc_df['precipitation']
        neg_X['precipitation'] = neg_df['precipitation'].fillna(0)
    else:
        pos_X['precipitation'] = 0
        neg_X['precipitation'] = 0

    X = pd.concat([pos_X, neg_X], ignore_index=True)
    y = pd.concat([acc_df['label'], neg_df['label']], ignore_index=True)

    return X, y, acc_df, neg_gdf