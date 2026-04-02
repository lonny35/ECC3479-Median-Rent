import pandas as pd
from geopy.geocoders import ArcGIS
from geopy.extra.rate_limiter import RateLimiter

# ---------------------------------------------------------
# 1. Load your CSV file
# ---------------------------------------------------------
df = pd.read_csv("data/raw/lga_coordinates.csv")

# Use the second Suburb column (the one with full council office addresses)
SUBURB_COLUMN = "Suburb.1"

# ---------------------------------------------------------
# 2. Set up the ArcGIS geocoder (much faster and more reliable)
# ---------------------------------------------------------
geolocator = ArcGIS(timeout=10)
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.2)

# ---------------------------------------------------------
# 3. Function to geocode each address
# ---------------------------------------------------------
def get_coordinates(address):
    try:
        location = geocode(f"{address}, Victoria, Australia")
        if location:
            return pd.Series([location.latitude, location.longitude])
        else:
            return pd.Series([None, None])
    except Exception:
        return pd.Series([None, None])

# ---------------------------------------------------------
# 4. Apply geocoding
# ---------------------------------------------------------
df[["latitude", "longitude"]] = df[SUBURB_COLUMN].apply(get_coordinates)

# ---------------------------------------------------------
# 5. Save the output
# ---------------------------------------------------------
df.to_csv("data/clean/lga_coordinates_geocoded.csv", index=False)

print("✓ Geocoding complete. Saved to data/clean/lga_coordinates_geocoded.csv")