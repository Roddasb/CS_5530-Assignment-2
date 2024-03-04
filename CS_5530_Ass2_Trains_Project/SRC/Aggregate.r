## Question E This is equivalent of the Python code 


library(dplyr)

# Read the data from the provided CSV file
data <- read.csv("C:/Users/roban/Documents/UMKC Courses/Semister IV/Princip_DataScience_5530/Assignment/Assignment 2/CS_5530_Ass2_Trains_Project/Trains_Clean/Clean_Modified_trains_data.csv")

# Step 1: Rename columns for better readability
data <- data %>%
  rename(Location_City = Location)

# Step 2: Mutate - Calculate the age of the car
data <- data %>%
  mutate(Car_Age = as.numeric(format(Sys.Date(), "%Y")) - Year)

# Step 3: Arrange the data by the year of manufacture (Year) in descending order
data <- data %>%
  arrange(desc(Year))

# Step 4: Summarize - Group by Location and summarize the data
summary_data <- data %>%
  group_by(Location_City) %>%
  summarise(
    Total_Cars = n(),
    Average_Kilometers = mean(Kilometers_Driven),
    Average_Price = mean(Price),
    Oldest_Car_Year = min(Year),
    Newest_Car_Year = max(Year)
  ) %>%
  mutate(Oldest_Car_Status = ifelse(Oldest_Car_Year < 2000, "Old", "Recent"))

# Round the numeric columns to 2 decimal places
summary_data$Average_Kilometers <- round(summary_data$Average_Kilometers, 2)
summary_data$Average_Price <- round(summary_data$Average_Price, 2)

# Write the summarized data to a new CSV file
write.csv(summary_data, "Summarized_trains_data.csv", row.names = FALSE)

# Display the head of the modified DataFrame
print(head(summary_data))

