import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Create extra columns
df['Month'] = df['Date'].dt.to_period('M')

# ---------------------------
# Data Calculations
# ---------------------------
sales_trend = df.groupby('Date')['Sales'].sum()
region_sales = df.groupby('Region')['Sales'].sum()
product_sales = df.groupby('Product')['Sales'].sum()
monthly_sales = df.groupby('Month')['Sales'].sum()

# ---------------------------
# DASHBOARD (All in one window)
# ---------------------------
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# 1. Sales Trend
axs[0, 0].plot(sales_trend, marker='o')
axs[0, 0].set_title("Sales Trend")
axs[0, 0].set_xlabel("Date")
axs[0, 0].set_ylabel("Sales")
axs[0, 0].grid()

# 2. Region Revenue
region_sales.plot(kind='bar', ax=axs[0, 1])
axs[0, 1].set_title("Revenue by Region")

# 3. Product Distribution
product_sales.plot(kind='pie', autopct='%1.1f%%', ax=axs[1, 0])
axs[1, 0].set_title("Product Share")
axs[1, 0].set_ylabel("")

# 4. Monthly Trend
monthly_sales.plot(marker='o', ax=axs[1, 1])
axs[1, 1].set_title("Monthly Sales")
axs[1, 1].grid()

# Adjust layout
plt.tight_layout()
plt.show()

# ---------------------------
# INSIGHTS
# ---------------------------
print("\n===== INSIGHTS =====")
print("Total Sales:", df['Sales'].sum())
print("Top Region:", region_sales.idxmax())
print("Top Product:", product_sales.idxmax())
