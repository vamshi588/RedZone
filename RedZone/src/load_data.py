import pandas as pd
import geopandas as gpd

def load_accidents(filepath):
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} accident records.")
    return df

def load_weather(filepath):
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} weather records.")
    return df

def load_roads(osm_file):
    gdf = gpd.read_file(osm_file)
    print(f"Loaded {len(gdf)} road segments.")
    return gdf
