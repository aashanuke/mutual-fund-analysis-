import pandas as pd
import os

# Path to raw data folder
DATA_PATH = "../data/raw"

# Get all CSV files
csv_files = [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]

print(f"\nFound {len(csv_files)} CSV files\n")

# Loop through files
for file in csv_files:

    file_path = os.path.join(DATA_PATH, file)

    print("=" * 60)
    print(f"FILE: {file}")

    # Read CSV
    df = pd.read_csv(file_path)

    # Print shape
    print("\nShape:")
    print(df.shape)

    # Print data types
    print("\nData Types:")
    print(df.dtypes)

    # Print first 5 rows
    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")