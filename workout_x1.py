import pandas as pd

# Loadx1 data
df = pd.read_csv("../csv files/x1_sleep_meal_data.csv")

# Add 'workout' column — 5 times per week
df["workout"] = df["Day"].apply(lambda x: 1 if (x - 1) % 7 < 5 else 0)

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
df.to_csv("updated_x1_sleep_meal_data.csv", index=False)
