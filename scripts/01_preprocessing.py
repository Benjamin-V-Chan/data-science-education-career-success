import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("../data/education_career_success.csv")

# Drop unnecessary columns (e.g., Student_ID)
df.drop(columns=["Student_ID"], inplace=True)

# Handle missing values
df.fillna(df.median(numeric_only=True), inplace=True)

# Convert categorical variables to numeric
categorical_cols = ["Gender", "Field_of_Study", "Current_Job_Level", "Entrepreneurship"]
label_encoders = {col: LabelEncoder() for col in categorical_cols}

for col in categorical_cols:
    df[col] = label_encoders[col].fit_transform(df[col])

# Save the cleaned dataset
df.to_csv("../outputs/processed_data.csv", index=False)
print("Preprocessing complete. Saved as processed_data.csv")
