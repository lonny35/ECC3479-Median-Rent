import pandas as pd

# Load datasets
rent = pd.read_csv("data/raw/median_rent.csv")
population = pd.read_csv("data/raw/lga_population.csv")
distance = pd.read_csv("data/clean/lga_distance_data.csv")

# Merge datasets
merged = (
    rent
    .merge(population, on="lga_code", how="left")
    .merge(distance, on="lga_code", how="left")
)

# Clean column names
merged.columns = [c.lower().replace(" ", "_") for c in merged.columns]

# Save output
merged.to_csv("data/clean/merged_data.csv", index=False)

print("✓ Cleaned + merged dataset saved: data/clean/merged_data.csv")