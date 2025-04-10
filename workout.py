import pandas as pd

# Load the merged sleep-meal dataset
df = pd.read_csv("../csv files/merged_sleep_meal_data.csv")

# Define how many days per week each person works out
workout_schedule = {
    "x3": 3,
    "x4": 0,
    "x2": 3,
    "x5": 1
}

# Add 'workout' column
df["workout"] = df.groupby("person").cumcount() % 7
df["workout"] = df.apply(
    lambda row: 1 if row["workout"] < workout_schedule[row["person"]] else 0, axis=1
)

# Get meal time slots
meal_slots = ["12AM - 2AM", "2AM - 4AM", "4AM - 6AM", "6AM - 8AM", "8AM - 10AM",
              "10AM - 12PM", "12PM - 2PM", "2PM - 4PM", "4PM - 6PM", "6PM - 8PM",
              "8PM - 10PM", "10PM - 12AM"]

# Compute average time between meals
def avg_meal_interval(row):
    active_meals = [slot for slot in meal_slots if row.get(slot) == 1]
    if len(active_meals) <= 1:
        return None
    indices = [meal_slots.index(slot) for slot in active_meals]
    indices.sort()
    intervals = [2 * (j - i) for i, j in zip(indices[:-1], indices[1:])]
    return sum(intervals) / len(intervals)

df["avg_meal_interval"] = df.apply(avg_meal_interval, axis=1)

# Save updated file
df.to_csv("updated_sleep_meal_data.csv", index=False)
