## This is for Question e e) Perform select, filter, rename, mutate, arrange ## and summarize with group by operations (or their equivalent operations in python) ##on this dataset. (4 points)  


import pandas as pd
import numpy as np

# Read the data from the provided CSV file
data = pd.read_csv("/content/Clean_Modified_trains_data.csv")

# Step 1: Rename columns for better readability
data.rename(columns={'Location': 'Location_City'}, inplace=True)

# Step 2: Mutate - Calculate the age of the car
data['Car_Age'] = pd.Timestamp.now().year - data['Year']

# Step 3: Arrange the data by the year of manufacture (Year) in descending order
data = data.sort_values(by='Year', ascending=False)

# Step 4: Summarize - Group by Location and summarize the data
summary_data = data.groupby('Location_City').agg(
    Total_Cars=('ID', 'count'),
    Average_Kilometers=('Kilometers_Driven', 'mean'),
    Average_Price=('Price', 'mean'),
    Oldest_Car_Year=('Year', 'min'),
    Newest_Car_Year=('Year', 'max')
).reset_index()

# Add a new column Oldest_Car_Status based on the condition
summary_data['Oldest_Car_Status'] = np.where(summary_data['Oldest_Car_Year'] < 2000, 'Old', 'Recent')

# Round the numeric columns to 2 decimal places
summary_data = summary_data.round({'Average_Kilometers': 2, 'Average_Price': 2})

# Write the summarized data to a new CSV file
summary_data.to_csv("Summarized_trains_data.csv", index=False)

# Display the head of the modified DataFrame
print(summary_data.head())