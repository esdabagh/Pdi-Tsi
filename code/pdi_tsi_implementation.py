import numpy as np
import pandas as pd
import os

def calculate_pdi_tsi(series):
    """
    Calculate PDI, TSI, SCP, TTI, and ATSI for a given time series.
    
    Parameters:
    series (numpy array): Input time series data
    
    Returns:
    dict: Dictionary containing PDI, TSI, MPDI, SCP, TTI, and ATSI values
    """
    n = len(series)
    if n < 3:
        raise ValueError("Series length must be at least 3 for PDI/TSI calculation.")
    
    pdi = np.zeros(n - 2)
    tsi = np.zeros(n - 2)
    atsi = np.zeros(n - 2)
    
    for t in range(n - 2):
        # PDI calculation
        pdi[t] = abs((series[t] + series[t + 2]) / 2 - series[t + 1])
        
        # TSI calculation
        segment = series[t:t + 3]
        mean_segment = np.mean(segment)
        sigma_t = np.sqrt(np.sum((segment - mean_segment) ** 2) / 3)
        tsi[t] = pdi[t] - sigma_t
        
        # ATSI calculation
        alpha = sigma_t / (sigma_t + 1)
        atsi[t] = alpha * pdi[t] + (1 - alpha) * tsi[t]
    
    # Calculate MPDI
    mpdi = np.mean(pdi)
    
    # Calculate SCP (Series Cyclability Percentage)
    scp = (np.sum(tsi > 0) / (n - 2)) * 100
    
    # Calculate TTI (Total Trend Separation Index)
    tti = np.sum(tsi)
    
    return {
        "PDI": pdi,
        "TSI": tsi,
        "MPDI": mpdi,
        "SCP": scp,
        "TTI": tti,
        "ATSI": atsi
    }

def load_data(file_path, column_name):
    """
    Load time series data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file
    column_name (str): Name of the column containing the time series data
    
    Returns:
    numpy array: Time series data
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")
    
    df = pd.read_csv(file_path)
    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} not found in {file_path}.")
    
    return df[column_name].values

def save_results(results, output_file):
    """
    Save the results to a text file.
    
    Parameters:
    results (dict): Dictionary containing PDI, TSI, MPDI, SCP, TTI, and ATSI
    output_file (str): Path to the output file
    """
    with open(output_file, 'w') as f:
        f.write("Time Series Analysis Results\n")
        f.write("===========================\n")
        f.write(f"MPDI: {results['MPDI']:.4f}\n")
        f.write(f"SCP: {results['SCP']:.2f}%\n")
        f.write(f"TTI: {results['TTI']:.4f}\n")
        f.write("\nPDI Values:\n")
        f.write(np.array2string(results['PDI'], precision=4) + "\n")
        f.write("\nTSI Values:\n")
        f.write(np.array2string(results['TSI'], precision=4) + "\n")
        f.write("\nATSI Values:\n")
        f.write(np.array2string(results['ATSI'], precision=4) + "\n")

def main():
    # Define paths to the datasets (relative to the script location)
    data_dir = "../data/small_datasets/"
    datasets = {
        "NOAA Temperature": ("noaa_temp_2020_2021csv_250320_143200.csv", "TMAX_Celsius"),
        "NYC Traffic": ("madison-avenue-bridge-traffic-nov2023-5dayscsv_250321_020326.csv", "Vol"),
        "USGS Seismic": ("southern_california_earthquakes_2024jancsv.csv", "mag")
    }
    
    # Create a directory for results if it doesn't exist
    results_dir = "results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    # Process each dataset
    for dataset_name, (file_name, column_name) in datasets.items():
        print(f"\nProcessing {dataset_name}...")
        try:
            # Load data
            file_path = os.path.join(data_dir, file_name)
            series = load_data(file_path, column_name)
            
            # Calculate indices
            results = calculate_pdi_tsi(series)
            
            # Print summary
            print(f"Dataset: {dataset_name}")
            print(f"MPDI: {results['MPDI']:.4f}")
            print(f"SCP: {results['SCP']:.2f}%")
            print(f"TTI: {results['TTI']:.4f}")
            
            # Save results
            output_file = os.path.join(results_dir, f"{dataset_name.lower().replace(' ', '_')}_results.txt")
            save_results(results, output_file)
            print(f"Results saved to {output_file}")
            
        except Exception as e:
            print(f"Error processing {dataset_name}: {str(e)}")

if __name__ == "__main__":
    main()
