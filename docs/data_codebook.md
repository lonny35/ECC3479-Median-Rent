# Data Codebook  
This document describes all variables contained in the final merged dataset used for analysis:  
`data/clean/final_panel.csv`.

The dataset is structured at the **LGA–year** level. Each row represents one Local Government Area (LGA) in a given year, combining rental prices, crime, education, health service availability, and distance to the Melbourne CBD.

All raw data is stored in `data/raw/` and remains unmodified.  
All cleaning and merging steps are performed by scripts in the `code/` directory.

---

# 1. Identification Variables

### **`lga_name`**
- **Type:** string  
- **Description:** Name of the Local Government Area.  
- **Purpose:** Primary geographic identifier used for merging datasets.

### **`year`**
- **Type:** integer  
- **Description:** Calendar year of observation.  
- **Purpose:** Temporal merge key across datasets.

---

# 2. Rental Market Variables

### **`median_rent`**
- **Type:** numeric (AUD)  
- **Description:** Median weekly rental price for dwellings in the LGA.  
- **Source:** Victorian Rental Report (raw file: `median_rent_by_lga.xlsx`)  
- **Notes:**  
  - Represents the central tendency of rental prices.  
  - Missing values may occur for LGAs with limited rental listings.

---

# 3. Crime Variables

### **`offence_count`**
- **Type:** integer  
- **Description:** Total number of recorded criminal offences in the LGA for the given year.  
- **Source:** Crime Statistics Agency Victoria (raw file: `crime_by_lga.xlsx`)  
- **Notes:**  
  - Represents absolute counts, not rates.  
  - May reflect differences in reporting practices across LGAs.

---

# 4. Education Variables

### **`independent_schools`**
- **Type:** integer  
- **Description:** Number of independent (non‑government) schools in the LGA.  
- **Source:** Victorian Department of Education (raw file: `schools_by_lga.xlsx`)

### **`total_schools`**
- **Type:** integer  
- **Description:** Total number of schools in the LGA (government + independent).  
- **Source:** Victorian Department of Education  
- **Notes:**  
  - Captures overall education infrastructure.  
  - May influence rental demand for families.

---

# 5. Health Service Availability Variables

These variables measure access to health services per 1,000 residents.

### **`gp_clinics_per_1000`**
- **Type:** numeric  
- **Description:** Number of general practice clinics per 1,000 residents.  
- **Source:** `health_by_lga.xlsx`

### **`allied_health_per_1000`**
- **Type:** numeric  
- **Description:** Number of allied health service locations per 1,000 residents.  
- **Examples:** physiotherapy, occupational therapy, psychology  
- **Source:** `health_by_lga.xlsx`

### **`dental_sites_per_1000`**
- **Type:** numeric  
- **Description:** Number of dental service locations per 1,000 residents.  
- **Source:** `health_by_lga.xlsx`

### **`pharmacies_per_1000`**
- **Type:** numeric  
- **Description:** Number of pharmacies per 1,000 residents.  
- **Source:** `health_by_lga.xlsx`

### **`acsc_per_1000`**
- **Type:** numeric  
- **Description:** Ambulatory Care Sensitive Conditions (ACSC) hospital separations per 1,000 residents.  
- **Interpretation:** Higher values may indicate poorer access to primary care.  
- **Source:** `health_by_lga.xlsx`

---

# 6. Geographic and Distance Variables

### **`address`**
- **Type:** string  
- **Description:** Street address of the LGA council office.  
- **Source:** `distance_by_lga.xlsx`  
- **Notes:** Used as the reference point for distance calculations.

### **`suburb`**
- **Type:** string  
- **Description:** Suburb in which the LGA council office is located.

### **`latitude`**
- **Type:** numeric (decimal degrees)  
- **Description:** Latitude of the LGA council office.  
- **Purpose:** Used to calculate straight‑line distance.

### **`longitude`**
- **Type:** numeric (decimal degrees)  
- **Description:** Longitude of the LGA council office.

### **`straight_line_km`**
- **Type:** numeric (kilometres)  
- **Description:** Straight‑line (“as the crow flies”) distance from the LGA council office to the Melbourne CBD.  
- **Purpose:** Provides a simple geographic distance measure independent of road networks.

### **`driving_km`**
- **Type:** numeric (kilometres)  
- **Description:** Driving distance from the LGA council office to the Melbourne CBD (corner of Lonsdale & Elizabeth Street).  
- **Source:** `distance_by_lga.xlsx`  
- **Notes:**  
  - Calculated using routing services (e.g., Google Maps or OpenRouteService).  
  - Represents the key explanatory variable for the research question.

---

# 7. Data Quality Notes

- Missing values may occur where source datasets do not report certain LGAs or years.  
- All merges are performed using `lga_name` and `year`.  
- Raw data is never modified; all transformations are scripted for reproducibility.  
- Cleaned datasets are stored in `data/clean/`.  
- Distance variables use council office locations as proxies for LGA centroids.

---

# 8. Versioning

- **Last updated:** 2/04/2026
- **Maintainer:** Lachlan O'Neill