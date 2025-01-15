import pandas as pd

# Load the dataset
file_path = "data/raw/salesforcourse.csv"
df = pd.read_csv(file_path)

# Drop irrelevant or mostly empty columns
df = df.drop(columns=["Column1"])

# Handle missing values
df.fillna({
    "Date": df["Date"].mode()[0],
    "Year": df["Year"].median(),
    "Month": df["Month"].mode()[0],
    "Customer Age": df["Customer Age"].median(),
    "Customer Gender": df["Customer Gender"].mode()[0],
    "Country": df["Country"].mode()[0],
    "State": df["State"].mode()[0],
    "Product Category": df["Product Category"].mode()[0],
    "Sub Category": df["Sub Category"].mode()[0],
    "Quantity": df["Quantity"].median(),
    "Unit Cost": df["Unit Cost"].median(),
    "Unit Price": df["Unit Price"].median(),
    "Cost": df["Cost"].median(),
    "Revenue": df["Revenue"].median()
}, inplace=True)

# Fill missing values in key categorical columns
df["Customer Gender"] = df["Customer Gender"].fillna("Unknown")
df["Country"] = df["Country"].fillna("Unknown")
df["State"] = df["State"].fillna("Unknown")
df["Product Category"] = df["Product Category"].fillna("Unknown")
df["Sub Category"] = df["Sub Category"].fillna("Other")

# Ensure consistent formatting (e.g., title case)
df["Country"] = df["Country"].str.title()
df["State"] = df["State"].str.title()

# Add calculated columns
df["Profit"] = df["Revenue"] - df["Cost"]
df["Profit Margin"] = (df["Profit"] / df["Revenue"]) * 100

# Save cleaned dataset
output_path = "data/processed/cleaned_sales_transactions.csv"
df.to_csv(output_path, index=False)
print(f"Cleaned data saved to {output_path}")


