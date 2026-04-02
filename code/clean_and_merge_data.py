import pandas as pd

def clean_and_merge():

    # -----------------------------
    # 1. Load all cleaned datasets
    # -----------------------------
    rent = pd.read_csv("Data/clean/median_rent_clean.csv")
    crime = pd.read_csv("Data/clean/crime_clean.csv")
    schools = pd.read_csv("Data/clean/schools_clean.csv")
    health = pd.read_csv("Data/clean/health_clean.csv")
    distance = pd.read_csv("Data/clean/distance_clean.csv")

    # -----------------------------
    # 2. Standardise LGA names
    # -----------------------------
    for df in [rent, crime, schools, health, distance]:
        df["lga_name"] = (
            df["lga_name"]
            .str.strip()
            .str.upper()
            .str.replace(" CITY COUNCIL", "")
            .str.replace(" CITY", "")
            .str.replace(" SHIRE COUNCIL", "")
            .str.replace(" SHIRE", "")
            .str.replace(" BOROUGH", "")
            .str.replace(" COUNCIL", "")
        )

    # -----------------------------
    # 3. Merge datasets step-by-step
    # -----------------------------
    merged = rent.merge(crime, on=["lga_name", "year"], how="left")
    merged = merged.merge(schools, on=["lga_name", "year"], how="left")
    merged = merged.merge(health, on=["lga_name", "year"], how="left")
    merged = merged.merge(distance, on="lga_name", how="left")

    # -----------------------------
    # 4. Sort and clean final panel
    # -----------------------------
    merged = merged.sort_values(["lga_name", "year"]).reset_index(drop=True)

    # -----------------------------
    # 5. Save final dataset
    # -----------------------------
    merged.to_csv("Data/clean/final_panel.csv", index=False)
    print("✓ Final merged dataset saved to Data/clean/final_panel.csv")


if __name__ == "__main__":
    clean_and_merge()