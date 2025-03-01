import random
import string
from data import sales, products
from invoices import generate_sale_invoice, update_sale_invoice, delete_sale_invoice

# sales id generator
def generate_sale_id():
    while True:
        sale_id = "SA" + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        if sale_id not in sales:  # Ensure ID is unique
            return sale_id

def add_sale(product_id, quantity, customer, date):
    if product_id not in products:
        print(f"Product ID '{product_id}' does not exist. Cannot add sale.")
        return

    try:
        quantity = int(quantity)
        if quantity <= 0:
            print("Quantity must be a positive integer.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a valid number.")
        return

    if products[product_id]["stock"] < quantity:
        print(f"Insufficient stock for Product ID '{product_id}'. Available stock: {products[product_id]['stock']}")
        return

    sale_id = generate_sale_id()
    sales[sale_id] = {"product_id": product_id, "quantity": quantity, "customer": customer, "date": date}

    products[product_id]["stock"] -= quantity

    generate_sale_invoice(sale_id, product_id, quantity, customer, date)

    print(f"Sale added successfully with ID: {sale_id}. Stock updated.")

def view_sales():
    if sales:
        print("\nSales:")
        for sale_id, details in sales.items():
            product_name = products[details['product_id']]['name']
            print(f"ID: {sale_id}, Product: {product_name}, Quantity: {details['quantity']}, Customer: {details['customer']}, Date: {details['date']}")
    else:
        print("No sales available.")

def update_sale(sale_id, new_product_id, new_quantity, customer, date):
    if sale_id not in sales:
        print(f"Sale ID '{sale_id}' does not exist.")
        return

    if new_product_id not in products:
        print(f"Product ID '{new_product_id}' does not exist. Cannot update sale.")
        return

    try:
        new_quantity = int(new_quantity)
        if new_quantity <= 0:
            print("Quantity must be a positive integer.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a valid number.")
        return

    old_product_id = sales[sale_id]['product_id']
    old_quantity = sales[sale_id]['quantity']

    products[old_product_id]['stock'] += old_quantity
    if products[new_product_id]['stock'] < new_quantity:
        print(f"Insufficient stock for Product ID '{new_product_id}'. Available stock: {products[new_product_id]['stock']}")
        products[old_product_id]['stock'] -= old_quantity
        return

    products[new_product_id]['stock'] -= new_quantity

    sales[sale_id] = {"product_id": new_product_id, "quantity": new_quantity, "customer": customer, "date": date}

    update_sale_invoice(sale_id)

    print(f"Sale ID '{sale_id}' updated successfully. Stock updated.")

def delete_sale(sale_id):
    if sale_id not in sales:
        print(f"Sale ID '{sale_id}' does not exist.")
        return

    product_id = sales[sale_id]["product_id"]
    quantity = sales[sale_id]["quantity"]

    if product_id in products:
        products[product_id]["stock"] += quantity

    del sales[sale_id]
    delete_sale_invoice(sale_id)
    print(f"Sale ID '{sale_id}' deleted successfully. Stock restored.")

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
            quantity = input("Enter quantity: ")
            customer = input("Enter customer name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_sale(product_id, quantity, customer, date)
        elif choice == "3":
            sale_id = input("Enter sale ID to update: ")
            new_product_id = input("Enter new product ID: ")
            new_quantity = input("Enter new quantity: ")
            customer = input("Enter new customer name: ")
            date = input("Enter new date (YYYY-MM-DD): ")
            update_sale(sale_id, new_product_id, new_quantity, customer, date)
        elif choice == "4":
            sale_id = input("Enter sale ID to delete: ")
            delete_sale(sale_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
