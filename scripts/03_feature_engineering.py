import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("../outputs/processed_data.csv")

# Feature engineering: Interaction terms
df["Internships_x_Projects"] = df["Internships_Completed"] * df["Projects_Completed"]

# Scaling numerical features
scaler = StandardScaler()
numerical_cols = ["High_School_GPA", "SAT_Score", "University_GPA", "Starting_Salary"]
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Save dataset with new features
df.to_csv("../outputs/processed_data.csv", index=False)
print("Feature engineering complete. Updated dataset saved.")
