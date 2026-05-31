import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# KPI Calculations
total_sales = df['Quantity'].sum()
total_revenue = df['Revenue'].sum()

print("Total Sales:", total_sales)
print("Total Revenue:", total_revenue)

# Revenue Trend
monthly_revenue = df.groupby(df['Date'].dt.to_period('M'))['Revenue'].sum()

plt.figure(figsize=(10, 5))
monthly_revenue.plot(kind='line', marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

# Top Products
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
top_products.plot(kind='bar')
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()
