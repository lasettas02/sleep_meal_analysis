import pandas as pd

def add_late_meal_flag(df: pd.DataFrame) -> pd.DataFrame:
    late_columns = ["8PM - 10PM", "10PM - 12AM"]
    existing = [col for col in late_columns if col in df.columns]
    if existing:
        df["late_meal"] = df[existing].sum(axis=1).apply(lambda x: 1 if x > 0 else 0)
    else:
        df["late_meal"] = 0
    return df

def add_number_of_meals(df: pd.DataFrame) -> pd.DataFrame:
    meal_columns = [
        "12AM - 2AM", "2AM - 4AM", "4AM - 6AM", "6AM - 8AM",
        "8AM - 10AM", "10AM - 12PM", "12PM - 2PM", "2PM - 4PM",
        "4PM - 6PM", "6PM - 8PM", "8PM - 10PM", "10PM - 12AM"
    ]
    existing = [col for col in meal_columns if col in df.columns]
    if existing:
        df["number_of_meals"] = df[existing].sum(axis=1)
    else:
        df["number_of_meals"] = 0
    return df

# Load full datasets
others_df = pd.read_csv("../csv files/final_sleep_meal_data.csv")
x1_df = pd.read_csv("../csv files/final_x1_sleep_meal_data.csv")

# Apply both features
others_df = add_number_of_meals(add_late_meal_flag(others_df))
x1_df = add_number_of_meals(add_late_meal_flag(x1_df))

# Save to cleaned files
others_df.to_csv("cleaned_summary_sleep_meal_others.csv", index=False)
x1_df.to_csv("cleaned_summary_sleep_meal_x1.csv", index=False)


