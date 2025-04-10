import matplotlib
matplotlib.use("Agg")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Add late meal flag
def add_late_meal_flag(df: pd.DataFrame) -> pd.DataFrame:
    meal_columns = ["8PM - 10PM", "10PM - 12AM"]
    df["late_meal"] = df[meal_columns].sum(axis=1).apply(lambda x: 1 if x > 0 else 0) if all(col in df.columns for col in meal_columns) else 0
    return df

# Load data
others_df = add_late_meal_flag(pd.read_csv("../csv files/final_sleep_meal_data.csv"))
x1_df = add_late_meal_flag(pd.read_csv("../csv files/final_x1_sleep_meal_data.csv"))

# Set person labels
x1_df["person"] = "x1"
# Make sure others_df only has x2 to x5
others_df["person"] = others_df["person"].replace({
    "Daniel": "x2", "Anas": "x3", "Carmen": "x4", "Lia": "x5"
})

# Define meal columns
meal_columns = [
    "12AM - 2AM", "2AM - 4AM", "4AM - 6AM", "6AM - 8AM",
    "8AM - 10AM", "10AM - 12PM", "12PM - 2PM", "2PM - 4PM",
    "4PM - 6PM", "6PM - 8PM", "8PM - 10PM", "10PM - 12AM"
]

# Recompute number_of_meals
others_df["number_of_meals"] = others_df[meal_columns].sum(axis=1)
x1_df["number_of_meals"] = x1_df[meal_columns].sum(axis=1)

# Time axis
if "date" in x1_df.columns:
    x1_df["date"] = pd.to_datetime(x1_df["date"], errors='coerce')
    x1_df = x1_df.sort_values("date").reset_index(drop=True)
    x1_df["day_index"] = x1_df.index + 1
else:
    x1_df["day_index"] = x1_df["Day"]
others_df["day_index"] = others_df["Day"]

# Combine
combined_df = pd.concat([others_df, x1_df], ignore_index=True)

# --- Plotting ---
print("Others shape:", others_df.shape)
print("X1 shape:", x1_df.shape)
print("\nColumns:", others_df.columns.tolist())
print("\nOthers Summary:\n", others_df.describe())
print("\nX1 Summary:\n", x1_df.describe())

# Histogram: Sleep Score
plt.figure(figsize=(12, 5))
sns.histplot(data=combined_df, x="custom_sleep_score", hue="person", bins=20, kde=True)
plt.title("Sleep Score Distribution")
plt.xlabel("Sleep Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("ss_distr.png")
plt.close()

# Histogram: Meals
plt.figure(figsize=(12, 5))
sns.histplot(data=combined_df, x="number_of_meals", hue="person", bins=12, discrete=True)
plt.title("Number of Meals per Day")
plt.xlabel("Meals")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("no_of_meals_daily.png")
plt.close()

# Boxplot: Sleep Score by Person
plt.figure(figsize=(10, 6))
sns.boxplot(data=combined_df, x="person", y="custom_sleep_score")
plt.title("Sleep Score by Person")
plt.tight_layout()
plt.savefig("sleepscore-byperson.png")
plt.close()

# Boxplot: Meal Interval
plt.figure(figsize=(10, 6))
sns.boxplot(data=combined_df, x="person", y="avg_meal_interval")
plt.title("Average Meal Interval by Person")
plt.tight_layout()
plt.savefig("avg_mealinterval.png")
plt.close()

# Lineplot: Sleep Score Over Time
plt.figure(figsize=(12, 6))
sns.lineplot(data=combined_df, x="day_index", y="custom_sleep_score", hue="person", marker="o")
plt.title("Sleep Score Over Time")
plt.xlabel("Day")
plt.ylabel("Sleep Score")
plt.tight_layout()
plt.savefig("sleep_score_over_time.png")
plt.close()

# Per-person correlation
for person in combined_df["person"].unique():
    person_df = combined_df[combined_df["person"] == person]
    corr = person_df[["custom_sleep_score", "number_of_meals", "avg_meal_interval", "workout", "late_meal"]].corr()
    print(f"\nCorrelation for {person}")
    print(corr)
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(f"Correlation Matrix - {person}")
    plt.tight_layout()
    plt.savefig(f"corr_matrix_{person}.png")
    plt.close()

# Overall correlation
overall_corr = combined_df[["custom_sleep_score", "number_of_meals", "avg_meal_interval", "workout", "late_meal"]].corr()
print("\nOverall Correlation Matrix:")
print(overall_corr)
plt.figure(figsize=(8, 6))
sns.heatmap(overall_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Overall Correlation Matrix (All Users)")
plt.tight_layout()
plt.savefig("corr_matrix_overall.png")
plt.close()

# Boxplot: Sleep Score by Workout
plt.figure(figsize=(8, 5))
sns.boxplot(data=combined_df, x="workout", y="custom_sleep_score")
plt.title("Sleep Score by Workout (All Users)")
plt.xticks([0, 1], ["No Workout", "Workout"])
plt.tight_layout()
plt.savefig("sleepscore_by_workout.png")
plt.close()

# Boxplot: Sleep Score by Late Meal
plt.figure(figsize=(8, 5))
sns.boxplot(data=combined_df, x="late_meal", y="custom_sleep_score")
plt.title("Sleep Score by Late Meal")
plt.xticks([0, 1], ["No Late Meal", "Late Meal"])
plt.tight_layout()
plt.savefig("sleep_score_by_late_meal.png")
plt.close()
