from src.load_data import load_accidents, load_weather, load_roads
from src.preprocess import preprocess_accidents, preprocess_weather
from src.feature_engineering import engineer_features
from src.model import train_model
from src.evaluate import evaluate_model
from src.visualize import plot_predictions
import joblib
from sklearn.model_selection import train_test_split
from src.visualize import plot_predictions
import pandas as pd
import geopandas as gpd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def main():
    print("Loading data...")
    acc_df = load_accidents('data/Motor_Vehicle_Collisions_-_Crashes.csv')
    weather_df = load_weather('data/Weather_data.csv')
    road_gdf = load_roads('data/export.geojson')

    print("Preprocessing...")
    acc_df = preprocess_accidents(acc_df)
    weather_df = preprocess_weather(weather_df)

    print("Engineering features...")
    X, y, acc_df_final, neg_df = engineer_features(acc_df, weather_df, road_gdf)

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

    print("Training model...")
    model = train_model(X_train, y_train)

    print("Evaluating model...")
    evaluate_model(model, X_test, y_test)

    print("Saving model...")
    joblib.dump(model, 'models/accident_rf.pkl')

    print("Generating map...")    
    map_obj = plot_predictions(acc_df_final, neg_df)
    map_obj.save('outputs/prediction_map(2).html')
    print("Map saved: outputs/prediction_map.html")
    print("Pipeline complete!")

main()
