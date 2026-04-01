import pandas as pd
from geopy.distance import geodesic

# Load LGA coordinates (must be in data/raw/)
lga_coords = pd.read_csv("data/raw/lga_coordinates.csv")

# Melbourne CBD reference point
cbd_coords = (-37.8136, 144.9631)

# Calculate distance from each LGA to CBD
def calculate_distance(row):
    lga_point = (row["latitude"], row["longitude"])
    return geodesic(lga_point, cbd_coords).kilometers

lga_coords["distance_to_cbd_km"] = lga_coords.apply(calculate_distance, axis=1)

# Save output
lga_coords.to_csv("data/clean/lga_distance_data.csv", index=False)

print("✓ Distance data created: data/clean/lga_distance_data.csv")