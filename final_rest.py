import pandas as pd

# Load processed file
df = pd.read_csv("../csv files/final_sleep_meal_data.csv")

# Define meal slot columns
meal_slots = ["12AM - 2AM", "2AM - 4AM", "4AM - 6AM", "6AM - 8AM", "8AM - 10AM",
              "10AM - 12PM", "12PM - 2PM", "2PM - 4PM", "4PM - 6PM", "6PM - 8PM",
              "8PM - 10PM", "10PM - 12AM"]

# Count number of meals per day
df["number_of_meals"] = df[meal_slots].sum(axis=1)

# Select final columns
summary_df = df[["person", "Day", "custom_sleep_score", "number_of_meals", "avg_meal_interval", "workout"]]

# Save to CSV
summary_df.to_csv("summary_sleep_meal_others.csv", index=False)

