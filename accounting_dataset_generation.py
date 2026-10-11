import sys
import os
import glob
import pandas as pd

def read_raw_data(input_folder: str) -> list:
    """
    Reads all raw data CSV files from the designated input folder.
    
    Parameters:
        input_folder (str): Path to the directory containing raw data files.
        
    Returns:
        list: A list of pandas DataFrames read from the CSV files.
    """
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"Input folder '{input_folder}' does not exist.")
    
    file_pattern = os.path.join(input_folder, "*.csv")
    csv_files = glob.glob(file_pattern)
    
    if not csv_files:
        print(f"Warning: No CSV files found in {input_folder}")
        return []
    
    dataframes = []
    for file in csv_files:
        df = pd.read_csv(file)
        dataframes.append(df)
        print(f"Loaded: {file}")
        
    return dataframes

def convert_to_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts and cleans raw DataFrame into a structured dataset format.
    
    Parameters:
        df (pd.DataFrame): Raw DataFrame to be processed.
        
    Returns:
        pd.DataFrame: Processed DataFrame.
    """
    # Menghapus duplikasi dan merapikan nama kolom
    processed_df = df.drop_duplicates().copy()
    processed_df.columns = processed_df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    return processed_df

def merge_dataset(dataframes: list) -> pd.DataFrame:
    """
    Merges a list of processed DataFrames into a single dataset.
    
    Parameters:
        dataframes (list): List of processed pandas DataFrames.
        
    Returns:
        pd.DataFrame: Merged single DataFrame.
    """
    if not dataframes:
        return pd.DataFrame()
    
    merged_df = pd.concat(dataframes, ignore_index=True)
    return merged_df

def main():
    """
    Main function to execute CLI commands for dataset generation.
    Usage: python3 accounting_dataset_generation.py <input_folder> <output_folder>
    """
    if len(sys.argv) != 3:
        print("Usage: python3 accounting_dataset_generation.py <input_folder> <output_folder>")
        sys.exit(1)
        
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    
    # 1. Read Raw Data
    raw_dfs = read_raw_data(input_folder)
    
    if not raw_dfs:
        print("No data to process.")
        sys.exit(0)
        
    # 2. Convert each raw dataset
    processed_dfs = [convert_to_dataset(df) for df in raw_dfs]
    
    # 3. Merge into single dataset
    final_df = merge_dataset(processed_dfs)
    
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    output_filepath = os.path.join(output_folder, "final_dataset.csv")
    
    # Save final CSV dataset
    final_df.to_csv(output_filepath, index=False)
    print(f"Successfully generated dataset at: {output_filepath}")

if __name__ == "__main__":
    main()