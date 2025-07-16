import pandas as pd

def preprocess_accidents(df):
    print("Accident DataFrame columns:", df.columns.tolist())

    # Try to find the correct date and time columns (including names with spaces)
    date_col = None
    time_col = None
    for candidate in ['CRASH_DATE', 'DATE', 'Crash Date', 'CRASH DATE']:
        if candidate in df.columns:
            date_col = candidate
            break
    for candidate in ['CRASH_TIME', 'TIME', 'Crash Time', 'CRASH TIME']:
        if candidate in df.columns:
            time_col = candidate
            break

    # Latitude and longitude columns
    lat_col = None
    lon_col = None
    for candidate in ['LATITUDE', 'Latitude']:
        if candidate in df.columns:
            lat_col = candidate
            break
    for candidate in ['LONGITUDE', 'Longitude']:
        if candidate in df.columns:
            lon_col = candidate
            break

    # If any required column is missing, print a helpful error and stop
    missing = []
    if not date_col:
        missing.append('date column (tried: CRASH_DATE, DATE, Crash Date, CRASH DATE)')
    if not time_col:
        missing.append('time column (tried: CRASH_TIME, TIME, Crash Time, CRASH TIME)')
    if not lat_col:
        missing.append('latitude column (tried: LATITUDE, Latitude)')
    if not lon_col:
        missing.append('longitude column (tried: LONGITUDE, Longitude)')
    if missing:
        raise KeyError(f"Missing required columns: {missing}\nAvailable columns: {df.columns.tolist()}")

    # Drop rows with missing values in required columns
    df = df.dropna(subset=[date_col, time_col, lat_col, lon_col])

    # Combine date and time into datetime
    df['datetime'] = pd.to_datetime(df[date_col].astype(str) + ' ' + df[time_col].astype(str), errors='coerce')
    df = df.dropna(subset=['datetime'])

    return df

def preprocess_weather(df):
    print("Weather DataFrame columns:", df.columns.tolist())

    # Try to find the correct datetime column
    datetime_col = None
    for candidate in ['time', 'datetime', 'date', 'DATE', 'Time', 'Date']:
        if candidate in df.columns:
            datetime_col = candidate
            break

    if not datetime_col:
        raise KeyError(f"Missing datetime column (tried: time, datetime, date, DATE, Time, Date)\nAvailable columns: {df.columns.tolist()}")

    df['datetime'] = pd.to_datetime(df[datetime_col], errors='coerce')
    df = df.dropna(subset=['datetime'])

    return df