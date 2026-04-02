import pandas as pd

def clean_crime_data():

    df = pd.read_excel("data/raw/crime_by_lga.xlsx")

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    possible_lga_cols = [c for c in df.columns if "lga" in c]
    df = df.rename(columns={possible_lga_cols[0]: "lga_name"})

    possible_year_cols = [c for c in df.columns if "year" in c]
    df = df.rename(columns={possible_year_cols[0]: "year"})

    possible_rate_cols = [c for c in df.columns if "rate" in c]
    df = df.rename(columns={possible_rate_cols[0]: "crime_rate"})

    df = df[["lga_name", "year", "crime_rate"]]
    df = df.dropna()

    df.to_csv("data/clean/crime_clean.csv", index=False)
    print("✓ Clean crime dataset saved to data/clean/crime_clean.csv")


if __name__ == "__main__":
    clean_crime_data()