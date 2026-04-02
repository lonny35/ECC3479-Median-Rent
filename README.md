# ECC3479 – Rental Prices and Distance to Melbourne CBD

## Research Question
Does proximity to the Melbourne Central Business District increase median rental prices in metropolitan Melbourne, keeping other factors constant?

---

## Repository Structure
project/ │ ├── data/ │   ├── raw/        # Original data files (saved as CSV; never edited by hand) │   └── clean/      # Cleaned and merged datasets produced by code │ ├── code/           # Python scripts for cleaning, merging, and analysis ├── docs/           # Documentation (data codebook, AI usage notes, etc.) └── outputs/        # Tables, figures, regression results


---

## Raw Data Format

The original datasets were provided as **Excel (.xlsx) files** by various government sources.  
For transparency and reproducibility:

- The Excel files are stored in `data/raw/` (e.g. `median_rent_by_lga.xlsx`, `schools_by_lga.xlsx`, `health_by_lga.xlsx`, `crime_by_lga.xlsx`, `distance_by_lga.xlsx`)
- These files are **never edited by hand**
- All cleaning and transformations occur **only through Python scripts**, which write outputs to `data/clean/`

This follows the principle that **raw data is immutable and all changes are scripted**.

---

## How to Run the Project From Scratch

### 1. Install Python and VS Code
- Install **Python 3.11+** from https://www.python.org  
- Install **VS Code** from https://code.visualstudio.com  
- Install the **Python extension** (ms-python.python) inside VS Code

---

### 2. Install Required Python Packages

Open VS Code → Terminal → run:

```bash
pip install -r requirements.txt

This installs:
- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- linearmodels
- requests

3. Ensure Raw Data Files are in place
Confirm the following files exist in data/raw/:
- median_rent_by_lga.xlsx
- schools_by_lga.xlsx
- health_by_lga.xlsx
- crime_by_lga.xlsx
- distance_by_lga.xlsx
- README.md (describing sources and variables)
If any dataset cannot be shared, instructions for obtaining it should be documented in data/raw/README.md or docs/data_access.md

Script Execution Order
Run the following scripts in this order (filenames here should match your actual code/ scripts):

1. Clean individual datasets
Example (adjust to your actual script names):
python code/clean_median_rent.py
python code/clean_schools.py
python code/clean_health.py
python code/clean_crime.py
python code/clean_distance.py

These scripts should read from data/raw/*.xlsx and write cleaned CSVs such as:
- data/clean/median_rent_clean.csv
- data/clean/schools_clean.csv
- data/clean/health_clean.csv
- data/clean/crime_clean.csv
- data/clean/distance_clean.csv
- 

2. Create final analysis panel
python code/make_final_panel.py

- This script should merge the cleaned datasets into something like:
- data/clean/final_panel.csv

3. Run the regression analysis
python code/run_regression.py

- This script should read final_panel.csv and write results to:
- outputs/regression_results.csv (and/or a text summary)

Software Information
This project uses Python with the following packages:
- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- linearmodels
- requests
Exact versions are listed in requirements.txt.

Manual Steps (Outside of Code)
- Download raw Excel datasets from official sources
- Place them unchanged into data/raw/
- Verify that the column names match those expected by the cleaning scripts
- Optionally inspect outputs in data/clean/ and outputs/ after running scripts

AI Use
Some parts of this project (e.g. code structure and debugging assistance) were supported by Microsoft Copilot. All analysis, interpretation and final decisions were made by the author. 

Contact
For questions about reproducibility, data structure, or workflow, please contact the author.
