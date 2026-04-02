import pandas as pd

def clean_crime_data():

    print("\nLoading crime_by_lga.xlsx ...")

    # Load WITHOUT specifying header so we can see everything
    df = pd.read_excel("data/raw/crime_by_lga.xlsx", header=None)

    print("\n--- FIRST 10 ROWS OF THE FILE ---")
    print(df.head(10))
    print("\n---------------------------------\n")

    print("Copy the above output and paste it into ChatGPT.")

if __name__ == "__main__":
    clean_crime_data()