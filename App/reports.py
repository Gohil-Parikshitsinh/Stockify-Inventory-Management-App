import matplotlib.pyplot as plt
import numpy as np
from data import sales, purchases, products, suppliers

def reports_menu():
    while True:
        print("\nReport Menu:")
        print("1. Sales Trend over Time")
        print("2. Purchases Trend over Time")
        print("3. Sales vs. Purchases per Product")
        print("4. Total Purchases per Supplier")
        print("5. Sales vs. Stock Levels")
        print("6. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            plot_sales_trend()
        elif choice == "2":
            plot_purchases_trend()
        elif choice == "3":
            plot_sales_vs_purchases()
        elif choice == "4":
            plot_purchases_per_supplier()
        elif choice == "5":
            plot_sales_vs_stock()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
# Sales Trend over Time - Line Chart
def plot_sales_trend():
    dates = [details['date'] for details in sales.values()]
    quantities = [details['quantity'] for details in sales.values()]

    # Sorting by date
    unique_dates = sorted(set(dates))
    sales_by_date = {date: sum(details['quantity'] for details in sales.values() if details['date'] == date) for date in unique_dates}

    plt.figure(figsize=(10, 5))
    plt.plot(list(sales_by_date.keys()), list(sales_by_date.values()), marker='o')
    plt.title('Sales Trend over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales Quantity')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Purchases Trend over Time - Line Chart
def plot_purchases_trend():
    dates = [details['date'] for details in purchases.values()]
    quantities = [details['quantity'] for details in purchases.values()]

    # Sorting by date
    unique_dates = sorted(set(dates))
    purchases_by_date = {date: sum(details['quantity'] for details in purchases.values() if details['date'] == date) for date in unique_dates}

    plt.figure(figsize=(10, 5))
    plt.plot(list(purchases_by_date.keys()), list(purchases_by_date.values()), marker='o', color='orange')
    plt.title('Purchases Trend over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Purchases Quantity')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Sales vs. Purchases per Product - Grouped Bar Chart
def plot_sales_vs_purchases():
    product_ids = list(products.keys())
    sales_counts = [sum(details['quantity'] for details in sales.values() if details['product_id'] == pid) for pid in product_ids]
    purchase_counts = [sum(details['quantity'] for details in purchases.values() if details['product_id'] == pid) for pid in product_ids]
    product_names = [products[pid]['name'] for pid in product_ids]

    x = np.arange(len(product_ids))
    width = 0.35

    plt.figure(figsize=(12, 6))
    plt.bar(x - width/2, sales_counts, width, label='Sales')
    plt.bar(x + width/2, purchase_counts, width, label='Purchases')

    plt.title('Sales vs. Purchases per Product')
    plt.xlabel('Products')
    plt.ylabel('Quantity')
    plt.xticks(x, product_names, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Total Purchases per Supplier - Pie Chart
def plot_purchases_per_supplier():
    supplier_names = [details['name'] for details in suppliers.values()]
    purchases_by_supplier = [sum(details['quantity'] for details in purchases.values() if details['supplier'] == sid) for sid in suppliers]

    plt.figure(figsize=(8, 8))
    plt.pie(purchases_by_supplier, labels=supplier_names, autopct='%1.1f%%', startangle=140)
    plt.title('Total Purchases per Supplier')
    plt.show()

# Sales vs. Stock Levels - Scatter Plot
def plot_sales_vs_stock():
    product_ids = list(products.keys())
    sales_counts = [sum(details['quantity'] for details in sales.values() if details['product_id'] == pid) for pid in product_ids]
    stock_levels = [products[pid]['stock'] for pid in product_ids]
    product_names = [products[pid]['name'] for pid in product_ids]

    plt.figure(figsize=(10, 6))
    plt.scatter(stock_levels, sales_counts)
    for i, name in enumerate(product_names):
        plt.annotate(name, (stock_levels[i], sales_counts[i]))

    plt.title('Sales vs. Stock Levels')
    plt.xlabel('Stock Level')
    plt.ylabel('Sales Quantity')
    plt.tight_layout()
    plt.show()
