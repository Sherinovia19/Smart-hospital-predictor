# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 2: Set absolute file path
file_path = r"C:\Users\vinot\smart-hospital-predictor\smart-hospital-predictor\data\processed\processed.csv"

# Step 3: Check if the file exists
if not os.path.isfile(file_path):
    print(f"Error: CSV file not found at {file_path}")
    print("Make sure the file exists and the path is correct.")
    exit()  # Stops the script if file is missing

# Step 4: Load CSV into a DataFrame
df = pd.read_csv(file_path)

# Step 5: Inspect the first few rows
print("First 5 rows of data:")
print(df.head(), "\n")

# Step 6: Check column names
print("Columns in the data:")
print(df.columns, "\n")

# Step 7: Check data types
print("Data types of each column:")
print(df.dtypes, "\n")

# Step 8: Check for missing values
print("Missing values per column:")
print(df.isnull().sum(), "\n")

# Step 9: Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Step 10: Set 'date' as the index
df.set_index('date', inplace=True)

# Step 11: Plot beds and ICU occupancy
df[['beds_occupied', 'icu_occupied']].plot(marker='o')
plt.title("Hospital Bed and ICU Occupancy Over Time")
plt.ylabel("Number of Beds")
plt.xlabel("Date")
plt.grid(True)
plt.show()

# Step 12: Plot oxygen consumption
df['oxygen_consumed_liters'].plot(marker='x', color='red')
plt.title("Oxygen Consumption Over Time")
plt.ylabel("Liters")
plt.xlabel("Date")
plt.grid(True)
plt.show()
