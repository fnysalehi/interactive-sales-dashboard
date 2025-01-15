import pandas as pd

# Load the dataset
file_path = "data/raw/salesforcourse.csv"
df = pd.read_csv(file_path)

# Quick overview of the dataset
print("Dataset Preview:")
print(df.head())  # Display first 5 rows

print("\nDataset Info:")
print(df.info())  # Check data types and missing values

print("\nSummary Statistics:")
print(df.describe())  # Summary stats for numeric columns

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values[missing_values > 0])

categorical_columns = ["Customer Gender", "Country", "State", "Product Category", "Sub Category"]

for column in categorical_columns:
    print(f"Unique values in {column}:")
    print(df[column].unique())
    print()
    