import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Info")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nStatistics")
print(df.describe())

plt.figure(figsize=(8,5))
sns.barplot(x="Product", y="Sales", data=df)
plt.title("Sales by Product")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(6,6))
plt.pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x="Sales", y="Profit", data=df)
plt.title("Sales vs Profit")
plt.show()
