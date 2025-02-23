import random
import string
from data import sales, products

# Generate a unique random sale ID starting with 'S' and 7 random alphanumeric characters
def generate_sale_id():
    while True:
        sale_id = "S" + ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        if sale_id not in sales:  # Ensure ID is unique
            return sale_id

# Add a new sale
def add_sale(product_id, quantity, customer, date):
    if product_id not in products:
        print(f"Product ID '{product_id}' does not exist. Cannot add sale.")
        return
    sale_id = generate_sale_id()
    sales[sale_id] = {"product_id": product_id, "quantity": quantity, "customer": customer, "date": date}
    print(f"Sale added successfully with ID: {sale_id}.")

# View all sales
def view_sales():
    if sales:
        print("\nSales:")
        for sale_id, details in sales.items():
            print(f"ID: {sale_id}, Product ID: {details['product_id']}, Quantity: {details['quantity']}, Customer: {details['customer']}, Date: {details['date']}")
    else:
        print("No sales available.")

# Edit an existing sale
def edit_sale(sale_id, product_id, quantity, customer, date):
    if sale_id not in sales:
        print(f"Sale ID '{sale_id}' does not exist.")
    elif product_id not in products:
        print(f"Product ID '{product_id}' does not exist. Cannot update sale.")
    else:
        sales[sale_id] = {"product_id": product_id, "quantity": quantity, "customer": customer, "date": date}
        print(f"Sale ID '{sale_id}' updated successfully.")

# Delete a sale
def delete_sale(sale_id):
    if sale_id not in sales:
        print(f"Sale ID '{sale_id}' does not exist.")
    else:
        del sales[sale_id]
        print(f"Sale ID '{sale_id}' deleted successfully.")

# Sales menu
def sales_menu():
    while True:
        print("\nSales Menu:")
        print("1. View Sales")
        print("2. Add Sale")
        print("3. Update Sale")
        print("4. Delete Sale")
        print("5. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            view_sales()
        elif choice == "2":
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity: "))
            customer = input("Enter customer name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_sale(product_id, quantity, customer, date)
        elif choice == "3":
            sale_id = input("Enter sale ID to update: ")
            product_id = input("Enter new product ID: ")
            quantity = int(input("Enter new quantity: "))
            customer = input("Enter new customer name: ")
            date = input("Enter new date (YYYY-MM-DD): ")
            edit_sale(sale_id, product_id, quantity, customer, date)
        elif choice == "4":
            sale_id = input("Enter sale ID to delete: ")
            delete_sale(sale_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
