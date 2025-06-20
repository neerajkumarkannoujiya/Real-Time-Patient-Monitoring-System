import pandas as pd

# Load your CSV file
df = pd.read_csv("merged_numeric.csv")

# Clean column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Apply rule-based disease risk logic
df['disease_risk'] = df.apply(lambda row: 1 if (
    row['hr'] < 50 or row['hr'] > 110 or
    row['pulse'] < 50 or row['pulse'] > 110 or
    row['resp'] < 10 or row['resp'] > 24 or
    row['spo2'] < 92
) else 0, axis=1)

# Save the labeled data as a new CSV
df.to_csv("labeled_data.csv", index=False)
print("✅ labeled_data.csv created.")
