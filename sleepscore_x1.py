import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def calculate_x1_sleep_score(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Positive and negative contributors
    positive_vars = ["sleepDuration", "deepSleepTime", "remSleepTime"]
    negative_vars = ["awakeCount", "heartRateAvg"]

    # Filter available variables
    pos = [v for v in positive_vars if v in df.columns]
    neg = [v for v in negative_vars if v in df.columns]

    # Normalize and reverse-score
    scaler = MinMaxScaler()

    for var in pos:
        df[f"{var}_norm"] = scaler.fit_transform(df[[var]].fillna(0))

    for var in neg:
        df[f"{var}_norm"] = 1 - scaler.fit_transform(df[[var]].fillna(0))  # reverse = higher is better

    # Combine into final score
    norm_cols = [f"{v}_norm" for v in pos + neg]
    df["custom_sleep_score"] = df[norm_cols].mean(axis=1) * 100

    return df
x1_df = pd.read_csv(r"C:\Users\20221063\PycharmProjects\pythonProject11\updated_x1_sleep_meal_data.csv")
x1_df = calculate_x1_sleep_score(x1_df)
x1_df.to_csv("final_x1_sleep_meal_data.csv", index=False)
