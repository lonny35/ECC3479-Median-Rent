"""
clean_and_merge_data.py

Cleans and merges:
- median_rent_by_lga.csv
- schools_by_lga.csv
- health_by_lga.csv
- crime_by_lga.csv
- lga_distances.csv

Outputs:
    data/clean/analysis_data.csv
with one row per LGA-year (or LGA-time unit) containing:
    median_rent, distance_km, controls (schools, health, crime).
"""

import os
import pandas as pd

RAW_DIR = "data/raw"
CLEAN_DIR = "data/clean"

def load_and_clean_rent():
    path = os.path.join(RAW_DIR, "median_rent_by_lga.csv")
    df = pd.read_csv(path)

    # Example cleaning – adjust to your actual column names
    df = df.rename(columns={
        "LGA": "lga_name",
        "Year": "year",
        "MedianRent": "median_rent"
    })

    # Keep only needed columns
    df = df[["lga_name", "year", "median_rent"]]

    return df


def load_and_clean_schools():
    path = os.path.join(RAW_DIR, "schools_by_lga.csv")
    df = pd.read_csv(path)

    df = df.rename(columns={
        "LGA": "lga_name",
        "Year": "year",
        "NumSchools": "num_schools"
    })

    df = df[["lga_name", "year", "num_schools"]]

    return df


def load_and_clean_health():
    path = os.path.join(RAW_DIR, "health_by_lga.csv")
    df = pd.read_csv(path)

    # Example: rename and select
    df = df.rename(columns={
        "LGA": "lga_name",
        "Year": "year",
        # Replace with your actual health variable names
        "HealthIndex": "health_index"
    })

    df = df[["lga_name", "year", "health_index"]]

    return df


def load_and_clean_crime():
    path = os.path.join(RAW_DIR, "crime_by_lga.csv")
    df = pd.read_csv(path)

    df = df.rename(columns={
        "LGA": "lga_name",
        "Year": "year",
        "CrimeRate": "crime_rate"
    })

    df = df[["lga_name", "year", "crime_rate"]]

    return df


def load_distances():
    path = os.path.join(CLEAN_DIR, "lga_distances.csv")
    df = pd.read_csv(path)

    # Just ensure consistent name
    df = df[["lga_name", "distance_km", "duration_minutes"]]

    return df


def main():
    rent = load_and_clean_rent()
    schools = load_and_clean_schools()
    health = load_and_clean_health()
    crime = load_and_clean_crime()
    dist = load_distances()

    # Merge step by step on lga_name and year
    df = rent.merge(schools, on=["lga_name", "year"], how="left")
    df = df.merge(health, on=["lga_name", "year"], how="left")
    df = df.merge(crime, on=["lga_name", "year"], how="left")
    df = df.merge(dist, on="lga_name", how="left")

    # Handle obvious data issues (example: drop rows with missing median_rent or distance)
    df = df.dropna(subset=["median_rent", "distance_km"])

    os.makedirs(CLEAN_DIR, exist_ok=True)
    out_path = os.path.join(CLEAN_DIR, "analysis_data.csv")
    df.to_csv(out_path, index=False)

    print(f"Saved cleaned analysis dataset to {out_path}")


if __name__ == "__main__":
    main()