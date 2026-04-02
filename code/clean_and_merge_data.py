import pandas as pd

def standardise_lga_column(df):
    """
    Detects the LGA column in any dataset and renames it to lga_name.
    """
    possible_cols = [
        "lga_name",
        "local_government_area",
        "local_government",
        "lga",
        "lga_code",
        "area_name",
        "council",
        "local government area",
        "Local Government Area",
    ]

    df_cols_lower = {c.lower(): c for c in df.columns}

    for col in possible_cols:
        if col.lower() in df_cols_lower:
            df = df.rename(columns={df_cols_lower[col.lower()]: "lga_name"})
            return df

    raise KeyError(f"No LGA column found. Columns were: {df.columns.tolist()}")


def expand_cross_section(df, years):
    """
    Expands a cross-sectional dataset (no year column) across all years.
    """
    expanded = []
    for y in years:
        temp = df.copy()
        temp["year"] = y
        expanded.append(temp)
    return pd.concat(expanded, ignore_index=True)


def clean_and_merge():

    # -----------------------------------
    # 1. Load cleaned datasets
    # -----------------------------------
    rent = pd.read_csv("Data/clean/median_rent_clean.csv")
    crime = pd.read_csv("Data/clean/crime_clean.csv")
    schools = pd.read_csv("Data/clean/schools_clean.csv")
    health = pd.read_csv("Data/clean/health_clean.csv")
    distance = pd.read_csv("Data/clean/distance_clean.csv")

    print("RENT COLUMNS:", rent.columns.tolist())
    print("CRIME COLUMNS:", crime.columns.tolist())
    print("SCHOOLS COLUMNS:", schools.columns.tolist())
    print("HEALTH COLUMNS:", health.columns.tolist())
    print("DISTANCE COLUMNS:", distance.columns.tolist())

    # -----------------------------------
    # 2. Expand cross-sectional datasets
    # -----------------------------------
    years = rent["year"].unique()

    # Schools has no year column → expand
    if "year" not in schools.columns:
        schools = expand_cross_section(schools, years)

    # Health has no year column → expand
    if "year" not in health.columns:
        health = expand_cross_section(health, years)

    # -----------------------------------
    # 3. Standardise LGA column names
    # -----------------------------------
    rent = standardise_lga_column(rent)
    crime = standardise_lga_column(crime)
    schools = standardise_lga_column(schools)
    health = standardise_lga_column(health)
    distance = standardise_lga_column(distance)

    # -----------------------------------
    # 4. Standardise LGA formatting
    # -----------------------------------
    for df in [rent, crime, schools, health, distance]:
        df["lga_name"] = (
            df["lga_name"]
            .astype(str)
            .str.strip()
            .str.upper()
            .str.replace(" CITY COUNCIL", "")
            .str.replace(" CITY", "")
            .str.replace(" SHIRE COUNCIL", "")
            .str.replace(" SHIRE", "")
            .str.replace(" BOROUGH", "")
            .str.replace(" COUNCIL", "")
        )

    # -----------------------------------
    # 5. Merge datasets
    # -----------------------------------
    merged = rent.merge(crime, on=["lga_name", "year"], how="left")
    merged = merged.merge(schools, on=["lga_name", "year"], how="left")
    merged = merged.merge(health, on=["lga_name", "year"], how="left")
    merged = merged.merge(distance, on="lga_name", how="left")

    # -----------------------------------
    # 6. Sort and save
    # -----------------------------------
    merged = merged.sort_values(["lga_name", "year"]).reset_index(drop=True)
    merged.to_csv("Data/clean/final_panel.csv", index=False)

    print("\n✓ Final merged dataset saved to Data/clean/final_panel.csv")


if __name__ == "__main__":
    clean_and_merge()