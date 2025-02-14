import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../outputs/processed_data.csv")

# Correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.savefig("../outputs/plots/correlation_heatmap.png")

# Distribution of salaries
plt.figure(figsize=(8, 6))
sns.histplot(df["Starting_Salary"], bins=30, kde=True)
plt.title("Starting Salary Distribution")
plt.savefig("../outputs/plots/salary_distribution.png")

print("Visualizations complete. Plots saved in outputs/plots/")
