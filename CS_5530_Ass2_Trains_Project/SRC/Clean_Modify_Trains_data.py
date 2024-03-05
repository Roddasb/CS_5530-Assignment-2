import pandas as pd
import re
from datetime import datetime

# Read the data from the provided CSV file
df = pd.read_csv("/content/Raw_Trains.csv")

# Rename the 'Unnamed: 0' column to 'No.'
df = df.rename(columns={'Unnamed: 0': 'No.'})

# Remove non-numeric characters from specified columns and convert to numeric values
numeric_cols = ['Engine', 'Mileage', 'Power', 'New_Price']
for col in numeric_cols:
    df[col] = df[col].apply(lambda x: re.sub(r'[^0-9.]', '', str(x)))

# Convert columns to numeric
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Rename specified columns
df = df.rename(columns={"Mileage": "Mileage_kms",
                        "Engine": "Engine_cc",
                        "Power": "Power_bhp",
                        "Price": "Price_Lakh"})

# Replace categorical variables with numerical codes
df['Transmission'] = df['Transmission'].replace({'Manual': 0, 'Automatic': 1})
df['Fuel_Type'] = df['Fuel_Type'].replace({'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'LPG': 3, 'Electric': 4})

# Look for missing values in all the columns
missing_values = df.isnull().sum()
print("Number of missing values in each column:")
print(missing_values)

# Drop the 'New_Price' column due to a high number of missing values
df = df.drop(columns=['New_Price'])

# Impute missing values for 'Engine_cc', 'Power_bhp', and 'Seats' with mean
df['Engine_cc'] = df['Engine_cc'].fillna(df['Engine_cc'].mean())
df['Power_bhp'] = df['Power_bhp'].fillna(df['Power_bhp'].mean())
df['Seats'] = df['Seats'].fillna(df['Seats'].mean())

# Drop rows with missing values for 'Mileage_kms' because there is only 2 of them
df = df.dropna(subset=['Mileage_kms'])

# Calculate the current age of the car and create a new feature 'Car_Age'
current_year = datetime.now().year
df['Car_Age'] = current_year - df['Year']

# Write the modified DataFrame to a new CSV file
df.to_csv("Clean_Modified_trains_data.csv", index=False)

# Display the head of the modified DataFrame
print(df.head())