# PDI-TSI Repository

## Overview
This repository accompanies the article *"A Simple Statistical Method for Assessing Trend Linearity and Separating Periodic Patterns in Time Series"* by Esmail Dabbaghsaz and Alireza Mohebalhojeh, submitted to a peer-reviewed journal on February 27, 2025. The proposed method introduces novel statistical indices—namely PDI (Pattern Deviation Index), TSI (Trend Stability Index), SCP (Seasonal Component Parameter), TTI (Trend Transition Index), and ATSI (Adjusted Trend Stability Index)—for analyzing time series data. The method has been applied to real-world datasets in meteorology, traffic, and seismology, demonstrating a 10-18% reduction in RMSE compared to classical methods such as linear regression and STL decomposition, while offering competitive performance against advanced techniques like ARIMA and Wavelet-Neural Network hybrids.

The Python implementation provided in this repository (`pdi_tsi_implementation.py`) extends beyond the version presented in the article (Section 3.5) by including the computation of additional indices such as ATSI, making it a more comprehensive tool for time series analysis.

## Repository Structure
- **`code/`**: Contains the Python implementation of the proposed method.
  - `pdi_tsi_implementation.py`: A Python script that computes PDI, TSI, SCP, TTI, ATSI, and MPDI (Mean Pattern Deviation Index) for time series data.
- **`data/`**: Contains the datasets used in the article and larger reference datasets for transparency.
  - **`large_datasets/`**: Larger datasets to demonstrate the origin of the article datasets.
    - `large_noaa_temperature.csv`: A broader dataset of NOAA temperature records.
    - `large_nyc_traffic.csv`: A broader dataset of NYC traffic records.
  - **`small_datasets/`**: Datasets directly used in the article (Section 4: Numerical Examples).
    - `noaa_temperature_2020_2021.csv`: Daily maximum temperatures in New York (Jan 1, 2020–Dec 31, 2021).
    - `nyc_traffic_madison_2023.csv`: Hourly vehicle counts at Madison Avenue Bridge, Manhattan (Nov 1–5, 2023).
    - `usgs_seismic_2024.csv`: Hourly seismic amplitudes near Calexico, CA (Jan 1–31, 2024).
- **`README.md`**: This documentation file.

## Datasets Description
### Article Datasets (Small Datasets)
These datasets were directly used in the article for numerical analysis (Section 4: Numerical Examples):
- **NOAA Temperature Data (`noaa_temperature_2020_2021.csv`)**: Daily maximum temperatures recorded at Station USW00094728 (Central Park, New York) from January 1, 2020, to December 31, 2021. The dataset contains 731 records after preprocessing, which involved removing 2% missing data and applying linear interpolation. Source: NOAA Global Historical Climatology Network (GHCN).
- **NYC Traffic Data (`nyc_traffic_madison_2023.csv`)**: Hourly vehicle counts at Madison Avenue Bridge, Manhattan, from November 1 to November 5, 2023 (120 hours). The dataset includes 16 real records, extended to 120 hours by reconstructing realistic patterns (see Section 4.2 of the article for details). Source: NYC Open Data.
- **USGS Seismic Data (`usgs_seismic_2024.csv`)**: Hourly seismic amplitudes near Calexico, CA, from January 1 to January 31, 2024 (744 hours), capturing 13 seismic events with magnitudes ranging from 1.2 to 4.4. Source: USGS Earthquake Hazards Program.

### Large Datasets (For Reference)
These datasets are provided for transparency, showing the origin of the article datasets:
- **Large NOAA Temperature Data (`large_noaa_temperature.csv`)**: A broader dataset from NOAA’s Global Historical Climatology Network (GHCN), from which the article’s temperature data was sampled.
- **Large NYC Traffic Data (`large_nyc_traffic.csv`)**: A larger dataset from NYC Open Data, from which the article’s traffic data was sampled.
- **Note on Seismic Data**: No large dataset is provided for the USGS seismic data, as the article dataset was directly sourced from 13 events recorded by the USGS Earthquake Hazards Program.

## How to Use the Code
1. **Prerequisites**: Ensure you have Python 3.x installed along with the required libraries: `numpy` and `pandas`. You can install them using:
   ```bash
   pip install numpy pandas
