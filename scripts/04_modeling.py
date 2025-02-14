import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("../outputs/processed_data.csv")

# Define features and target variable
X = df.drop(columns=["Starting_Salary"])
y = df["Starting_Salary"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

# Save results
with open("../outputs/model_performance.txt", "w") as f:
    f.write(f"Mean Absolute Error: {mae:.2f}")

print(f"Modeling complete. MAE: {mae:.2f}. Results saved.")
