import streamlit as st
import pandas as pd

# Example coordinates
coordinates = {
    'lat': [43.6672, 43.7709, 43.7412],  # Latitude values
    'lon': [-79.4016, -79.3365, -79.5215]  # Longitude values
}

# Create a DataFrame
df = pd.DataFrame(coordinates)

# Title
st.title("Map of Coordinates")

# Plot the coordinates on a map
st.map(df)