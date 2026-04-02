import pandas as pd

def clean_crime_data():

    # Load the correct sheet (based on your screenshot: "Table 01")
    df = pd.read_excel(
        "data/raw/crime_by_lga.xlsx",
        sheet_name="Table 01",
        engine="openpyxl",
        dtype=str
    )

    # Standardise column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Rename the columns we need
    df = df.rename(columns={
        "local_government_area": "lga_name",
        "year": "year",
        "offence_count": "offence_count"
    })

    # Keep only the three required columns
    df = df[["lga_name", "year", "offence_count"]]

    # Convert offence_count to numeric
    df["offence_count"] = (
        df["offence_count"]
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    # Convert year to integer
    df["year"] = df["year"].astype(int)

    # Drop totals or non-LGA rows
    df = df[df["lga_name"].str.lower() != "total"]

    # Save cleaned file
    df.to_csv("data/clean/crime_clean.csv", index=False)

    print("✓ Clean crime dataset saved to data/clean/crime_clean.csv")


if __name__ == "__main__":
    clean_crime_data()