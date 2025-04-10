import pandas as pd

def clean_sleep_meal_others(file_path: str, output_path: str = "cleaned_summary_sleep_meal_others.csv") -> pd.DataFrame:
    df = pd.read_csv(file_path)

    # Drop duplicates
    df = df.drop_duplicates()

    # Convert types
    df["Day"] = df["Day"].astype(int)
    df["workout"] = df["workout"].astype(int)
    df["number_of_meals"] = df["number_of_meals"].astype(int)

    # Convert and clean numeric fields
    df["custom_sleep_score"] = pd.to_numeric(df["custom_sleep_score"], errors="coerce")
    df["avg_meal_interval"] = pd.to_numeric(df["avg_meal_interval"], errors="coerce")

    # Replace missing values in  numeric columns with column means
    for col in ["custom_sleep_score", "avg_meal_interval"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        mean_value = df[col].mean()
        df[col] = df[col].fillna(mean_value)

    # sleep score to 0–100
    df["custom_sleep_score"] = df["custom_sleep_score"].clip(0, 100)

    # Save cleaned file
    df.to_csv(output_path, index=False)

    return df

def clean_sleep_meal_x1(file_path: str, output_path: str = "cleaned_summary_sleep_meal_x1.csv") -> pd.DataFrame:
    df = pd.read_csv(file_path)

    # Drop duplicates
    df = df.drop_duplicates()

    # Normalize column naming
    if "date" not in df.columns and "Day" in df.columns:
        df.rename(columns={"Day": "date"}, inplace=True)

    # Convert types
    df["workout"] = df["workout"].astype(int)
    df["number_of_meals"] = df["number_of_meals"].astype(int)

    # Convert and clean numeric fields
    df["custom_sleep_score"] = pd.to_numeric(df["custom_sleep_score"], errors="coerce")
    df["avg_meal_interval"] = pd.to_numeric(df["avg_meal_interval"], errors="coerce")

    # Replace missing values in numeric columns with  column means
    for col in ["custom_sleep_score", "avg_meal_interval"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        mean_value = df[col].mean()
        df[col] = df[col].fillna(mean_value)

    # sleep score to 0–100
    df["custom_sleep_score"] = df["custom_sleep_score"].clip(0, 100)

    # Save cleaned file
    df.to_csv(output_path, index=False)

    return df
# Clean and save both datasets
clean_sleep_meal_others("../csv files/summary_sleep_meal_others.csv")
clean_sleep_meal_x1("../csv files/summary_sleep_meal_x1.csv")
