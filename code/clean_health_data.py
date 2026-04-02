import pandas as pd

def clean_health_data():

    df = pd.read_excel("data/raw/health_by_lga.xlsx")

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    possible_lga_cols = [c for c in df.columns if "lga" in c]
    df = df.rename(columns={possible_lga_cols[0]: "lga_name"})

    possible_year_cols = [c for c in df.columns if "year" in c]
    df = df.rename(columns={possible_year_cols[0]: "year"})

    possible_health_cols = [c for c in df.columns if "health" in c or "index" in c]
    df = df.rename(columns={possible_health_cols[0]: "health_index"})

    df = df[["lga_name", "year", "health_index"]]
    df = df.dropna()

    df.to_csv("data/clean/health_clean.csv", index=False)
    print("✓ Clean health dataset saved to data/clean/health_clean.csv")


if __name__ == "__main__":
    clean_health_data()