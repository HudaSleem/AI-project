import pandas as pd
import os

def load_unemployment_data(file_name):
    """
    Data Ingestion Pipeline Component
    Loads unemployment data based on gender and age.
    """
    try:
        # Resolve the file path: assuming the file is inside the 'data' folder
        file_path = os.path.join('data', file_name)
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully: {file_name}")
        return df
    except Exception as e:
        print(f" Error during data loading: {e}")
        return None

if __name__ == "__main__":
    # IMPORTANT: Ensure this matches the exact name of the CSV file you uploaded
    FILE_NAME = 'unemployment_data.csv' 
    
    data = load_unemployment_data(FILE_NAME)
    
    if data is not None:
        print("--- Preview of Loaded Data ---")
        print(data.head())
