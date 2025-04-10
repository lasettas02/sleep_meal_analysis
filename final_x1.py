import pandas as pd

# Load processed file
x1_df = pd.read_csv("../csv files/final_x1_sleep_meal_data.csv")

# Define meal slot columns
meal_slots = ["12AM - 2AM", "2AM - 4AM", "4AM - 6AM", "6AM - 8AM", "8AM - 10AM",
              "10AM - 12PM", "12PM - 2PM", "2PM - 4PM", "4PM - 6PM", "6PM - 8PM",
              "8PM - 10PM", "10PM - 12AM"]

# Count number of meals per day
x1_df["number_of_meals"] = x1_df[meal_slots].sum(axis=1)

# Use available date or fallback to Day
date_col = "date" if "date" in x1_df.columns else "Day"

# Select final columns
summary_x1 = x1_df[["person", date_col, "custom_sleep_score", "number_of_meals", "avg_meal_interval", "workout"]]

# Save to CSV
summary_x1.to_csv("summary_sleep_meal_x1.csv", index=False)

