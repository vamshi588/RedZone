import folium
from folium.plugins import MarkerCluster

def plot_predictions(acc_df, neg_df, lat_col='LATITUDE', lon_col='LONGITUDE'):
    # Take first 500 points from each DataFrame
    acc_sample = acc_df.head(500)
    neg_sample = neg_df.head(500)

    # Center map on accident points
    m = folium.Map(
        location=[acc_sample[lat_col].mean(), acc_sample[lon_col].mean()],
        zoom_start=13
    )

    # Cluster for accidents (red)
    acc_cluster = MarkerCluster(name="Accidents").add_to(m)
    for _, row in acc_sample.iterrows():
        folium.CircleMarker(
            location=[row[lat_col], row[lon_col]],
            radius=3,
            color='red',
            fill=True,
            fill_opacity=0.7
        ).add_to(acc_cluster)

    # Cluster for safe points (green)
    neg_cluster = MarkerCluster(name="Safe Points").add_to(m)
    for _, row in neg_sample.iterrows():
        # If neg_df is a GeoDataFrame, use geometry; else use lat/lon columns
        if hasattr(row, 'geometry'):
            lat, lon = row.geometry.y, row.geometry.x
        else:
            lat, lon = row[lat_col], row[lon_col]
        folium.CircleMarker(
            location=[lat, lon],
            radius=3,
            color='green',
            fill=True,
            fill_opacity=0.5
        ).add_to(neg_cluster)

    folium.LayerControl().add_to(m)
    return m

"""def plot_predictions(acc_df, neg_df=None):
    # Center the map around accident points
    m = folium.Map(
        location=[acc_df['LATITUDE'].mean(), acc_df['LONGITUDE'].mean()],
        zoom_start=13
    )

    # Add clustered markers for positive points
    acc_cluster = MarkerCluster(name="Accidents").add_to(m)
    for _, row in acc_df.iterrows():
        folium.CircleMarker(
            location=[row['LATITUDE'], row['LONGITUDE']],
            radius=3,
            color='red',
            fill=True,
            fill_opacity=0.7
        ).add_to(acc_cluster)

    # Add clustered markers for negative points if provided
    if neg_df is not None:
        neg_cluster = MarkerCluster(name="Safe Points").add_to(m)
        for _, row in neg_df.iterrows():
            folium.CircleMarker(
                location=[row.geometry.y, row.geometry.x],
                radius=3,
                color='green',
                fill=True,
                fill_opacity=0.5
            ).add_to(neg_cluster)

    folium.LayerControl().add_to(m)

    return m"""
