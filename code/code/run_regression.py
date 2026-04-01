import pandas as pd
import statsmodels.api as sm

# Load merged dataset
df = pd.read_csv("data/clean/merged_data.csv")

# Define variables
y = df["median_rent"]
X = df[["distance_to_cbd_km", "population"]]

# Add constant term
X = sm.add_constant(X)

# Run regression
model = sm.OLS(y, X).fit()

# Save results to text file
with open("data/clean/regression_results.txt", "w") as f:
    f.write(model.summary().as_text())

print("✓ Regression complete. Results saved to data/clean/regression_results.txt")