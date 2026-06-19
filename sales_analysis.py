import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv", encoding="latin1")

print(data)

print("\nTotal Sales =", data["Sales"].sum())
print("Total Profit =", data["Profit"].sum())

sales_by_product = data.groupby("Product")["Sales"].sum()

sales_by_product.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()

monthly_sales = data.groupby("Month")["Sales"].sum()

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show() 

monthly_sales = data.groupby("Month")["Sales"].sum()

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()