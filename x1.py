import pandas as pd
import json

# Load datasets
sleep_df = pd.read_csv(r"C:\Users\20221063\Downloads\merged_sleep_data.csv")
meal_df = pd.read_csv(r"C:\Users\20221063\Downloads\Merged_Meal_Data.csv")

# Extract and parse sleep data
x1_data = sleep_df["x1"].dropna().apply(json.loads)
x1_sleep = pd.json_normalize(x1_data)
x1_sleep["person"] = "x1"
x1_sleep["Day"] = range(1, len(x1_sleep) + 1)

# Extract and parse meal data
x1_meal = meal_df[["Day", "x1"]].dropna()
x1_meal["meal_pattern"] = x1_meal["x1"].apply(json.loads)
x1_meal_parsed = pd.json_normalize(x1_meal["meal_pattern"])
x1_meal_clean = pd.concat([x1_meal[["Day"]].reset_index(drop=True), x1_meal_parsed], axis=1)
x1_meal_clean["person"] = "x1"

# Merge sleep and meal data on day and person
x1_merged = pd.merge(x1_sleep, x1_meal_clean, on=["person", "Day"], how="inner")

# Save to CSV
x1_merged.to_csv("x1_sleep_meal_data.csv", index=False)
