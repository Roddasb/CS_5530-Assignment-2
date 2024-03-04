
## QUESTION A TO D 

Number of missing values in each column:
ID                      0
Name                    0
Location                0
Year                    0
Kilometers_Driven       0
Fuel_Type               0
Transmission            0
Owner_Type              0
Mileage_kms             2
Engine_cc              36
Power_bhp              36
Seats                  38
New_Price_Lakh       5032
Price                   0
dtype: int64
   ID                              Name    Location  Year  Kilometers_Driven  \
0   1  Hyundai Creta 1.6 CRDi SX Option        Pune  2015              41000   
1   2                      Honda Jazz V     Chennai  2011              46000   
2   3                 Maruti Ertiga VDI     Chennai  2012              87000   
3   4   Audi A4 New 2.0 TDI Multitronic  Coimbatore  2013              40670   
4   6            Nissan Micra Diesel XV      Jaipur  2013              86999   

   Fuel_Type  Transmission Owner_Type  Mileage_kms  Engine_cc  Power_bhp  \
0          1             0      First        19.67     1582.0     126.20   
1          0             0      First        13.00     1199.0      88.70   
2          1             0      First        20.77     1248.0      88.76   
3          1             1     Second        15.20     1968.0     140.80   
4          1             0      First        23.08     1461.0      63.10   

   Seats  New_Price_Lakh  Price  Price_Difference_Lakh  
0    5.0           20.48  12.50                   7.98  
1    5.0            8.61   4.50                   4.11  
2    7.0           20.48   6.00                  14.48  
3    5.0           20.48  17.74                   2.74  
4    5.0           20.48   3.50                  16.98  




QUESTION E SAMPLE RESULTS 
import pandas as pd

# Read the data from the provided CSV file
data = pd.read_csv("/content/Clean_Modified_trains_data.csv")

# Step 1: Rename columns for better readability
data.rename(columns={'Location': 'Location_City'}, inplace=True)



# Step 3: Arrange the data by the year of manufacture (Year) in descending order
data.sort_values(by='Year', ascending=False, inplace=True)

# Step 4: Summarize - Group by Location and summarize the data
summary_data = data.groupby('Location_City').agg(
    Total_Cars=('ID', 'count'),
    Average_Kilometers=('Kilometers_Driven', 'mean'),
    Average_Price=('Price', 'mean'),
    Oldest_Car_Year=('Year', 'min'),
    Newest_Car_Year=('Year', 'max')
).reset_index()

# Round the numeric columns to 2 decimal places
summary_data = summary_data.round({'Average_Kilometers': 2, 'Average_Price': 2})



df.to_csv("Sumarize_trains_data.csv", index=False)

# Display the head of the modified DataFrame

print(df.head())
