import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../outputs/processed_data.csv")

# Generate summary statistics
summary = df.describe().to_string()

# Identify correlation between features
correlation_matrix = df.corr().to_string()

# Save results
with open("../outputs/eda_summary.txt", "w") as f:
    f.write("Summary Statistics:\n")
    f.write(summary)
    f.write("\n\nCorrelation Matrix:\n")
    f.write(correlation_matrix)

print("EDA complete. Saved as eda_summary.txt")
