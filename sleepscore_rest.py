import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def calculate_sleep_score(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Variables contributing positively (higher = better)
    positive_vars = [
        'total_long_duration',
        'sleep_deep_duration',
        'sleep_rem_duration',
        'avg_spo2'
    ]

    # Variables contributing negatively (higher = worse)
    negative_vars = [
        'awake_count',
        'total_body_move',
        'avg_hr'
    ]

    # Filter available variables
    available_pos = [var for var in positive_vars if var in df.columns]
    available_neg = [var for var in negative_vars if var in df.columns]

    # Normalize each feature
    scaler = MinMaxScaler()

    for var in available_pos:
        df[f"{var}_norm"] = scaler.fit_transform(df[[var]].fillna(0))

    for var in available_neg:
        df[f"{var}_norm"] = 1 - scaler.fit_transform(df[[var]].fillna(0))  # reverse scale

    # Combine all normalized components
    norm_columns = [f"{var}_norm" for var in available_pos + available_neg]
    df["custom_sleep_score"] = df[norm_columns].mean(axis=1) * 100  # scale to 0-100

    return df

df = pd.read_csv(r"C:\Users\20221063\PycharmProjects\pythonProject11\updated_sleep_meal_data.csv")
df = calculate_sleep_score(df)
df.to_csv("final_sleep_meal_data.csv", index=False)
