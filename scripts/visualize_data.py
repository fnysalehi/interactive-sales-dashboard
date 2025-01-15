import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = "data/processed/cleaned_sales_transactions.csv"
df = pd.read_csv(file_path)

# Set the style for plots
sns.set(style="whitegrid")

# 1. Monthly Revenue Trends
monthly_revenue = df.groupby("Month")["Revenue"].sum().sort_index()
plt.figure(figsize=(10, 6))
monthly_revenue.plot(kind="line", marker="o", title="Monthly Revenue Trends")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("docs/plots/monthly_revenue.png")
plt.show()

# 2. Revenue by Product Category
category_revenue = df.groupby("Product Category")["Revenue"].sum().sort_values()
plt.figure(figsize=(10, 6))
category_revenue.plot(kind="barh", title="Revenue by Product Category")
plt.xlabel("Total Revenue")
plt.ylabel("Product Category")
plt.tight_layout()
plt.savefig("docs/plots/category_revenue.png")
plt.show()

# 3. Revenue Split by Customer Gender
gender_revenue = df.groupby("Customer Gender")["Revenue"].sum()
plt.figure(figsize=(6, 6))
gender_revenue.plot(kind="pie", autopct="%1.1f%%", title="Revenue by Customer Gender")
plt.ylabel("")  # Remove the y-axis label for a clean look
plt.tight_layout()
plt.savefig("docs/plots/gender_revenue.png")
plt.show()

# 4. Profit Margin by Product Category
df["Profit Margin"] = (df["Revenue"] - df["Cost"]) / df["Revenue"] * 100
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Product Category", y="Profit Margin")
plt.title("Profit Margin by Product Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("docs/plots/profit_margin_by_category.png")
plt.show()
