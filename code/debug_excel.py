import pandas as pd

def inspect_excel(path):

    print(f"\nInspecting: {path}")

    # Load workbook structure
    xls = pd.ExcelFile(path)

    print("\n--- SHEETS FOUND ---")
    print(xls.sheet_names)
    print("--------------------\n")

    # Print first 20 rows of each sheet
    for sheet in xls.sheet_names:
        print(f"\n--- FIRST 20 ROWS OF SHEET: {sheet} ---")
        df = pd.read_excel(xls, sheet_name=sheet, header=None)
        print(df.head(20))
        print("----------------------------------------\n")

if __name__ == "__main__":
    inspect_excel("data/raw/median_rent_by_lga.xlsx")