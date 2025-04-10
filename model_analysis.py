import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
from math import sqrt

#Load the clean datasets
others_df = pd.read_csv("../csv_final_files_used/cleaned_summary_sleep_meal_others.csv")
stelios_df = pd.read_csv("../csv_final_files_used/cleaned_summary_sleep_meal_x1.csv")

# Add 'person' to x1 data if missing
if "person" not in stelios_df.columns:
    stelios_df["person"] = "Stelios"

# Combine datasets
df = pd.concat([others_df, stelios_df], ignore_index=True)

#Features and target
features = ["number_of_meals", "avg_meal_interval", "workout", "late_meal"]
target = "custom_sleep_score"

#Drop missing
model_df = df[features + [target]].dropna()
X = model_df[features]
y = model_df[target]

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

#predict and evaluate
y_pred = model.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Linear Regression Performance")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.2f}")

#Feature coefficients
coef_df = pd.DataFrame({
    "Feature": features,
    "Coefficient": model.coef_
}).sort_values(by="Coefficient", key=abs, ascending=False)

print("\n Linear Model Coefficients")
print(coef_df)

#Plot coefficients
plt.figure(figsize=(8, 5))
sns.barplot(data=coef_df, x="Coefficient", y="Feature")
plt.title("Feature Importance - Linear Regression")
plt.tight_layout()
plt.savefig("feature_importance_linear.png")
plt.close()
