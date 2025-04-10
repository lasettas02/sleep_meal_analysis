import pandas as pd
import json

# Load data
sleep_df = pd.read_csv(r"C:\Users\20221063\Downloads\cleaned_sleep_data.csv")
meal_df = pd.read_csv(r"C:\Users\20221063\Downloads\Merged_Meal_Data.csv")

# Reshape meal data to long format
meal_long = meal_df.melt(id_vars="Day", var_name="person", value_name="meal_pattern")

# Filter out x1
meal_long = meal_long[meal_long["person"] != "x1"].reset_index(drop=True)

# Parse meal pattern JSON into columns
meal_expanded = meal_long["meal_pattern"].apply(lambda x: json.loads(x) if pd.notna(x) else {})
meal_df_parsed = pd.json_normalize(meal_expanded)
meal_long = pd.concat([meal_long[["Day", "person"]], meal_df_parsed], axis=1)

# Add a Day index to sleep data for each person to align records
sleep_df["Day"] = sleep_df.groupby("person").cumcount() + 1

# Merge on person and Day
merged_df = pd.merge(sleep_df, meal_long, on=["person", "Day"], how="inner")

# Save final merged data
merged_df.to_csv("merged_sleep_meal_data.csv", index=False)

