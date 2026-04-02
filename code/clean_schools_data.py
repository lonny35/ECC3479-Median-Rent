import pandas as pd

def clean_schools_data():

    df = pd.read_excel("data/raw/schools_by_lga.xlsx")

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    possible_lga_cols = [c for c in df.columns if "lga" in c]
    df = df.rename(columns={possible_lga_cols[0]: "lga_name"})

    possible_year_cols = [c for c in df.columns if "year" in c]
    df = df.rename(columns={possible_year_cols[0]: "year"})

    possible_school_cols = [c for c in df.columns if "school" in c]
    df = df.rename(columns={possible_school_cols[0]: "num_schools"})

    df = df[["lga_name", "year", "num_schools"]]
    df = df.dropna()

    df.to_csv("data/clean/schools_clean.csv", index=False)
    print("✓ Clean schools dataset saved to data/clean/schools_clean.csv")


if __name__ == "__main__":
    clean_schools_data()