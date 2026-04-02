# Raw Data Documentation

This folder contains the raw datasets used in the analysis. These files are sourced from Victorian Government open data portals and downloaded manually. No cleaning or transformation has been applied.

## Files

### `median_rent_by_lga.csv`
- Source: Victorian rental data
- Contains median weekly rent by LGA and year.
- Key variables: `lga_name`, `year`, `median_rent`

### `schools_by_lga.csv`
- Source: Department of Education
- Contains number of schools per LGA.
- Key variables: `lga_name`, `year`, `num_schools`

### `health_by_lga.csv`
- Source: Victorian health statistics
- Contains health indicators aggregated by LGA.
- Key variables: `lga_name`, `year`, `health_index`

### `crime_by_lga.csv`
- Source: Crime Statistics Agency Victoria
- Contains crime rates per LGA.
- Key variables: `lga_name`, `year`, `crime_rate`

## Notes
- These files remain unmodified.
- Cleaning and merging occur in the `code/` folder.