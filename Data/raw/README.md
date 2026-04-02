# Raw Data Documentation

This folder contains the **original raw datasets** used in the analysis.  
All files were downloaded directly from official Victorian Government sources in **Excel (.xlsx)** format and are stored here **unchanged**.  
No manual editing, cleaning, or restructuring has been applied to these files.

Storing raw data in its original form ensures:
- full transparency,
- reproducibility,
- and a clear separation between raw and processed data.

All cleaning and transformation steps occur in the `code/` folder and produce outputs in `data/clean/`.

---

## File Descriptions

### `median_rent_by_lga.xlsx`
- **Source:** Victorian Government – Rental Report / Housing Data  
- **Access date: 26/03/2026
- **Description:** Contains median weekly rent for each Local Government Area (LGA) across multiple years.  
- **Key variables:**  
  - `LGA` – Local Government Area name  
  - `Year` – Calendar year  
  - `MedianRent` – Median weekly rent (AUD)  
- **Limitations:**  
  - Some LGAs may have missing years due to insufficient rental observations.  
  - Rental categories may differ across reporting periods.

---

### `schools_by_lga.xlsx`
- **Source:** Victorian Department of Education  
- **Access date:** 26/03/2026
- **Description:** Number of schools located within each LGA by year.  
- **Key variables:**  
  - `LGA`  
  - `Year`  
  - `NumSchools` – Count of government and non‑government schools  
- **Limitations:**  
  - School counts may reflect administrative boundaries rather than physical locations.  
  - Some LGAs may have combined or missing categories.

---

### `health_by_lga.xlsx`
- **Source:** Victorian Health Data / Public Health Indicators  
- **Access date:** 26/03/2026
- **Description:** Contains aggregated health indicators at the LGA level.  
- **Key variables:**  
  - `LGA`  
  - `Year`  
  - `HealthIndex` – Composite indicator of health outcomes  
- **Limitations:**  
  - Health indicators may be modelled estimates rather than direct measurements.  
  - Methodology may vary across years.

---

### `crime_by_lga.xlsx`
- **Source:** Crime Statistics Agency Victoria  
- **Access date:** 26/03/2026
- **Description:** Crime rates and incident counts by LGA and year.  
- **Key variables:**  
  - `LGA`  
  - `Year`  
  - `CrimeRate` – Incidents per 100,000 population  
- **Limitations:**  
  - Crime reporting practices may differ across LGAs.  
  - Population estimates used for rate calculations may introduce measurement error.

---

### `distance_by_lga.xlsx`
- **Source:** Manually compiled using LGA council office coordinates and routing data  
- **Access date:** 26/03/2026
- **Description:** Contains driving distance and/or travel time from each LGA’s council office to the Melbourne CBD (corner of Lonsdale & Elizabeth Street).  
- **Key variables:**  
  - `LGA`  
  - `Distance_km` – Driving distance in kilometres  
  - `Duration_min` – Estimated driving time in minutes  
- **Limitations:**  
  - Distances are based on council office locations, not geographic centroids.  
  - Travel times depend on routing assumptions and may vary by time of day.

---

## General Notes

- These files remain **completely unmodified** to preserve data integrity.  
- All cleaning, renaming, merging, and transformation steps are implemented through Python scripts in the `code/` directory.  
- Cleaned datasets are stored in `data/clean/`.  
- If a dataset cannot be included due to licensing restrictions, instructions for obtaining it are provided in `docs/data_access.md`.

---

## Links to Original Documentation (Optional but Recommended)
*(Replace with actual URLs if available)*

- Victorian Rental Report: https://www.dffh.vic.gov.au  
- Crime Statistics Agency Victoria: https://www.crimestatistics.vic.gov.au  
- Victorian Department of Education: https://www.education.vic.gov.au  
- Victorian Health Data: https://www.health.vic.gov.au  
