import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
df_Customer = pd.read_csv(r"C:\Users\DHRUV SHAH\Customer Order & Review\Customer.csv")
df_Order = pd.read_csv(r"C:\Users\DHRUV SHAH\Customer Order & Review\Order.csv")
print(df_Customer.head())
print()
print(df_Order.head())
print()

# Merge two dataset
merged_df = pd.merge(df_Customer, df_Order, on="CustomerID", how="outer")
print(merged_df)
print()

# Add Revenue column
merged_df['Revenue'] = merged_df['Price'] * merged_df['Quantity']
print(merged_df)
print()

# Revenue by Category
Revenue_Category = merged_df.groupby('Category')['Revenue'].sum()
print(Revenue_Category)
print()

# Revenue by City
Revenue_City = merged_df.groupby('City')['Revenue'].sum()
print(Revenue_City)
print()

# Revenue by Customer
Revenue_CustomerName = merged_df.groupby('CustomerName')['Revenue'].sum()
print(Revenue_CustomerName)
print()

# Monthly Trend
merged_df["OrderDate"] = pd.to_datetime(merged_df["OrderDate"])
merged_df["Month"] = merged_df["OrderDate"].dt.to_period("M")
monthly_orders = merged_df.groupby("Month")["OrderID"].count().reset_index()
print(monthly_orders)
print()

# Visualization 
sns.countplot(x="Category", data=merged_df, color="r")
plt.title("Orders per Category")
plt.show()
print()

sns.barplot(x="Category", y="Revenue", data=merged_df, color="y")
plt.title("Revenue by Category")
plt.show()
print()

sns.lineplot(x="OrderDate", y="OrderID", data=merged_df, color="y")
plt.title("Order Over Time")
plt.show()
print()

sns.countplot(x="City", data=merged_df, color="r")
plt.title("Order by City")
plt.show()
print()

sns.histplot(merged_df["Quantity"])
plt.title("Quantity Distribution")
plt.show()