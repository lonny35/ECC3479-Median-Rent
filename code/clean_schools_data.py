import pandas as pd

def clean_schools_data():

    # Load sheet with correct header row (row 10)
    df = pd.read_excel(
        "data/raw/schools_by_lga.xlsx",
        sheet_name="LGA Data",
        engine="openpyxl",
        header=10,
        dtype=str
    )

    # Rename columns explicitly based on detected names
    df = df.rename(columns={
        "Row Labels": "lga_name",
        "Sum of No Of Schools.2": "independent_schools",
        "Unnamed: 8": "total_schools"
    })

    # Keep only the required columns
    df = df[["lga_name", "independent_schools", "total_schools"]]

    # Clean numeric columns
    df["independent_schools"] = df["independent_schools"].replace("-", "0").astype(float)
    df["total_schools"] = df["total_schools"].replace("-", "0").astype(float)

    # Drop totals or blank rows
    df = df[df["lga_name"].notna()]
    df = df[df["lga_name"].str.lower() != "total"]

    # Save cleaned file
    df.to_csv("data/clean/schools_clean.csv", index=False)

    print("✓ Clean schools dataset saved to data/clean/schools_clean.csv")


if __name__ == "__main__":
    clean_schools_data()