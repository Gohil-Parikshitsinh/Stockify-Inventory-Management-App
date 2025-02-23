import random
import string
from data import products,suppliers, purchases, sales

# Generate a unique random supplier ID starting with 'S' and 7 random alphanumeric characters
def generate_supplier_id():
    while True:
        supplier_id = "S" + ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        if supplier_id not in suppliers:  # Ensure ID is unique
            return supplier_id

# Add a new supplier
def add_supplier(name, products_supplied):
    if name in [supplier['name'] for supplier in suppliers.values()]:
        print(f"Supplier '{name}' already exists.")
        return

    invalid_products = [pid for pid in products_supplied if pid not in products]
    if invalid_products:
        print(f"Invalid product IDs: {', '.join(invalid_products)}. Please provide valid product IDs.")
        return

    supplier_id = generate_supplier_id()
    suppliers[supplier_id] = {"name": name, "products_supplied": products_supplied}
    print(f"Supplier '{name}' added successfully with ID: {supplier_id}.")

# View all suppliers
def view_suppliers():
    if suppliers:
        print("\nSuppliers:")
        for supplier_id, details in suppliers.items():
            print(f"ID: {supplier_id}, Name: {details['name']}, Products Supplied: {', '.join(details['products_supplied'])}")
    else:
        print("No suppliers available.")

# Edit an existing supplier
def edit_supplier(supplier_id, new_name, new_products_supplied):
    if supplier_id not in suppliers:
        print(f"Supplier ID '{supplier_id}' does not exist.")
        return

    invalid_products = [pid for pid in new_products_supplied if pid not in products]
    if invalid_products:
        print(f"Invalid product IDs: {', '.join(invalid_products)}. Please provide valid product IDs.")
        return

    suppliers[supplier_id] = {"name": new_name, "products_supplied": new_products_supplied}
    print(f"Supplier ID '{supplier_id}' updated to Name: '{new_name}' and Products Supplied: {', '.join(new_products_supplied)}.")

def delete_supplier(supplier_id):
    if supplier_id not in suppliers:
        print(f"Supplier ID '{supplier_id}' does not exist.")
        return

    # Check if any purchases or sales are linked to the supplier's products
    supplier_products = suppliers[supplier_id]['products_supplied']

    linked_to_purchases = any(purchase['product_id'] in supplier_products for purchase in purchases.values())
    linked_to_sales = any(sale['product_id'] in supplier_products for sale in sales.values())

    if linked_to_purchases or linked_to_sales:
        print(f"Cannot delete Supplier ID '{supplier_id}' — their products are linked to purchases or sales.")
    else:
        del suppliers[supplier_id]
        print(f"Supplier ID '{supplier_id}' deleted successfully.")


# Supplier menu
def suppliers_menu():
    while True:
        print("\nSuppliers Menu:")
        print("1. View Suppliers")
        print("2. Add Supplier")
        print("3. Update Supplier")
        print("4. Delete Supplier")
        print("5. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            view_suppliers()
        elif choice == "2":
            name = input("Enter supplier name to add: ")
            products_supplied = input("Enter product IDs supplied (comma-separated): ").split(',')
            add_supplier(name, [pid.strip() for pid in products_supplied])
        elif choice == "3":
            supplier_id = input("Enter supplier ID to update: ")
            new_name = input("Enter new supplier name: ")
            new_products_supplied = input("Enter new product IDs supplied (comma-separated): ").split(',')
            edit_supplier(supplier_id, new_name, [pid.strip() for pid in new_products_supplied])
        elif choice == "4":
            supplier_id = input("Enter supplier ID to delete: ")
            delete_supplier(supplier_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
