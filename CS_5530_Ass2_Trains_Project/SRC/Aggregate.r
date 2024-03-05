# library(dplyr)
# 
# # Read the data from the provided CSV file
# data <- read.csv("/content/Clean_Modified_trains_data.csv")
# 
# # Step 1: Rename columns for better readability
# names(data)[names(data) == "Location"] <- "Location_City"
# 
# # Step 2: Mutate - Calculate the age of the car
# current_year <- as.numeric(format(Sys.Date(), "%Y"))
# data$Car_Age <- current_year - data$Year
# 
# # Step 3: Arrange the data by the year of manufacture (Year) in descending order
# data <- arrange(data, desc(Year))
# 
# # Step 4: Select specific columns
# selected_cols <- c("Location_City", "No.", "Kilometers_Driven", "Price_Lakh", "Year")
# data <- select(data, selected_cols)
# 
# # Step 5: Filter rows where 'Price_Lakh' is not null
# data <- filter(!is.na(Price_Lakh))
# 
# # Step 6: Group by Location and summarize the data
# summary_data <- data %>%
#   group_by(Location_City) %>%
#   summarise(
#     Total_Cars = n(),
#     Average_Kilometers = mean(Kilometers_Driven, na.rm = TRUE),
#     Average_Price_Lakh = mean(Price_Lakh, na.rm = TRUE),
#     Oldest_Car_Year = min(Year, na.rm = TRUE),
#     Newest_Car_Year = max(Year, na.rm = TRUE)
#   ) %>%
#   ungroup()
# 
# # Step 7: Add a new column Oldest_Car_Status based on the condition
# summary_data$Oldest_Car_Status <- ifelse(summary_data$Oldest_Car_Year < 2000, "Old", "Recent")
# 
# # Step 8: Round the numeric columns to 2 decimal places
# summary_data <- mutate_at(summary_data, vars(Average_Kilometers, Average_Price_Lakh), ~ round(., 2))
# 
# # Write the summarized data to a new CSV file
# write.csv(summary_data, file = "Summarized_trains_data.csv", row.names = FALSE)
# 
# # Display the head of the modified DataFrame
# print(head(summary_data))
# # 