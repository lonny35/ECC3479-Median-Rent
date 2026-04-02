import pandas as pd
import re

def clean_rent_data():

    df = pd.read_excel(
        "data/raw/median_rent_by_lga.xlsx",
        skiprows=1,
        header=[0, 1]
    )

    df.columns = [
        f"{str(a).strip()}_{str(b).strip()}" if str(b) != "nan" else str(a).strip()
        for a, b in df.columns
    ]

    df = df.rename(columns={df.columns[0]: "lga_name"})
    df = df[df["lga_name"].notna()]
    df = df[~df["lga_name"].str.contains("Group Total", na=False)]

    median_cols = [c for c in df.columns if c.endswith("_Median")]

    df_long = df.melt(
        id_vars=["lga_name"],
        value_vars=median_cols,
        var_name="quarter",
        value_name="median_rent"
    )

    df_long["quarter"] = df_long["quarter"].str.replace("_Median", "", regex=False)
    df_long = df_long[df_long["quarter"].str.match(r"^[A-Za-z]{3}-\d{2}$", na=False)]

    df_long["median_rent"] = (
        df_long["median_rent"]
        .astype(str)
        .str.replace(r"[\$,]", "", regex=True)
        .replace("", pd.NA)
        .astype(float)
    )

    df_long["year"] = df_long["quarter"].str[-2:].astype(int)
    df_long["year"] = df_long["year"].apply(lambda x: 2000 + x if x < 50 else 1900 + x)

    df_final = df_long[["lga_name", "year", "median_rent"]].dropna()
    df_final.to_csv("data/clean/median_rent_clean.csv", index=False)

    print("✓ Clean rental dataset saved to data/clean/median_rent_clean.csv")


if __name__ == "__main__":
    clean_rent_data()