import pandas as pd

file_path = r"C:\Users\Sneh\Downloads\supermarket_sales - Sheet1.csv"
df = pd.read_csv(file_path)

print("First 5 rows of the dataset:")
print(df.head())


print("Shape of the dataset:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nInfo:")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())
# Drop missing rows
df = df.dropna()

# Confirm it's clean
print("Missing values after dropping:\n", df.isnull().sum())
print("New shape:", df.shape)

print("Product lines:", df['Product line'].unique())

top_sales = df.groupby('Product line')['Total'].sum().sort_values(ascending=False)
print("Total sales by product line:\n", top_sales)

avg_rating = df.groupby('Product line')['Rating'].mean().sort_values(ascending=False)
print("Average rating by product line:\n", avg_rating)

sales_by_city = df.groupby('City')['Total'].sum().sort_values(ascending=False)
print("Total sales by city:\n", sales_by_city)

payment_counts = df['Payment'].value_counts()
print("Sales count per payment method:\n", payment_counts)

df['Date'] = pd.to_datetime(df['Date'])
df['Weekday'] = df['Date'].dt.day_name()

sales_by_day = df.groupby('Weekday')['Total'].sum().sort_values(ascending=False)
print("Sales by weekday:\n", sales_by_day)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

# Plot: Sales distribution by Gender
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Gender", y="Total", estimator=sum, ci=None)
plt.title("Total Sales by Gender")
plt.ylabel("Total Sales")
plt.xlabel("Gender")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(x='Product line', y='Total', data=df, estimator=sum)
plt.title('Total Sales by Product Line')
plt.xticks(rotation=45)
plt.ylabel('Total Sales')
plt.xlabel('Product Line')
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x='City', y='Total', data=df, estimator=sum)
plt.title('Total Sales by City')
plt.ylabel('Total Sales')
plt.xlabel('City')
plt.show()


df['Total'] = pd.to_numeric(df['Total'], errors='coerce')

# Ensure Date is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract Year-Month
df['Month'] = df['Date'].dt.strftime('%Y-%m')

# Group by Month and calculate total sales
monthly_sales = df.groupby('Month')['Total'].sum().reset_index()

# Plot
plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_sales, x='Month', y='Total', marker='o', errorbar=None)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Payment')
plt.title('Payment Method Distribution')
plt.xlabel('Payment Method')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x='Branch', y='gross income', data=df, estimator=sum)
plt.title('Total Gross Income by Branch')
plt.xlabel('Branch')
plt.ylabel('Gross Income')
plt.show()

plt.figure(figsize=(8,4))
sns.histplot(df['Rating'], bins=10, kde=True)
plt.title('Customer Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

























