import pandas as pd

xls = pd.ExcelFile("Data/raw/lga_addresses.xlsx")
print(xls.sheet_names)