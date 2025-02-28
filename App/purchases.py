import random
import string
from data import purchases, products, suppliers
from invoices import generate_purchase_invoice, update_purchase_invoice, delete_purchase_invoice


# purchase id generator
def generate_purchase_id():
    while True:
        purchase_id = "PR" + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        if purchase_id not in purchases:
            return purchase_id

def add_purchase(product_id, quantity, supplier_id, date):
    if product_id not in products:
        print(f"Product ID '{product_id}' does not exist.")
        return

    if supplier_id not in suppliers:
        print(f"Supplier ID '{supplier_id}' does not exist.")
        return

    if product_id not in suppliers[supplier_id]['products_supplied']:
        print(f"Supplier ID '{supplier_id}' does not sell Product ID '{product_id}'. Purchase cannot be made.")
        return

    try:
        quantity = int(quantity)  # Ensure quantity is an integer
        if quantity <= 0:
            print("Quantity must be a positive integer.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a valid number.")
        return

    purchase_id = generate_purchase_id()
    purchases[purchase_id] = {
        "product_id": product_id,
        "quantity": quantity,
        "supplier": supplier_id,
        "date": date
    }

    products[product_id]["stock"] += quantity

    generate_purchase_invoice(purchase_id, supplier_id, product_id, quantity)

    print(f"Purchase added successfully with ID: {purchase_id}. Stock updated.")



def view_purchases():
    if not purchases:
        print("No purchases available.")
        return
    print("\nPurchases:")
    for purchase_id, details in purchases.items():
        product_name = products[details['product_id']]['name']
        supplier_name = suppliers[details['supplier']]['name']  # Assuming the 'name' field exists for suppliers
        purchase_date = details['date']
        print(f"ID: {purchase_id}, Product: {product_name}, Quantity: {details['quantity']}, Supplier: {supplier_name}, Date: {purchase_date}")


def update_purchase(purchase_id, new_quantity, new_product_id=None):
    if purchase_id not in purchases:
        print(f"Purchase ID '{purchase_id}' does not exist.")
        return

    current_purchase = purchases[purchase_id]
    supplier_id = current_purchase['supplier']

    if new_product_id:
        if new_product_id not in products:
            print(f"Product ID '{new_product_id}' does not exist.")
            return

        if new_product_id not in suppliers[supplier_id]['products_supplied']:
            print(f"Supplier ID '{supplier_id}' does not sell Product ID '{new_product_id}'. Update cannot be made.")
            return

    try:
        new_quantity = int(new_quantity)
        if new_quantity <= 0:
            print("Quantity must be a positive integer.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a valid number.")
        return

    old_quantity = current_purchase['quantity']
    product_id = current_purchase['product_id']

    products[product_id]['stock'] -= old_quantity
    products[product_id]['stock'] += new_quantity

    if new_product_id:
        products[new_product_id]['stock'] += new_quantity
        products[product_id]['stock'] -= new_quantity
        purchases[purchase_id]['product_id'] = new_product_id

    purchases[purchase_id]['quantity'] = new_quantity
    update_purchase_invoice(purchase_id)
    print(
        f"Purchase ID '{purchase_id}' updated. Old Quantity: {old_quantity}, New Quantity: {new_quantity}. Stock updated.")


def delete_purchase(purchase_id):
    if purchase_id not in purchases:
        print(f"Purchase ID '{purchase_id}' does not exist.")
        return

    product_id = purchases[purchase_id]["product_id"]
    quantity = purchases[purchase_id]["quantity"]

    if product_id in products:
        products[product_id]["stock"] -= quantity

    del purchases[purchase_id]
    delete_purchase_invoice(purchase_id)
    print(f"Purchase ID '{purchase_id}' deleted. Stock updated.")

def purchase_menu():
    while True:
        print("\nPurchase Menu:")
        print("1. View Purchases")
        print("2. Add Purchase")
        print("3. Update Purchase")
        print("4. Delete Purchase")
        print("5. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            view_purchases()
        elif choice == "2":
            product_id = input("Enter product ID: ")
            quantity = input("Enter quantity: ")
            supplier_id = input("Enter supplier ID: ")  # Add supplier ID prompt
            date = input("Enter purchase date (YYYY-MM-DD): ")  # Add date prompt
            add_purchase(product_id, quantity, supplier_id, date)  # Pass all arguments to add_purchase
        elif choice == "3":
            purchase_id = input("Enter purchase ID to update: ")
            new_quantity = input("Enter new quantity: ")
            update_purchase(purchase_id, new_quantity)
        elif choice == "4":
            purchase_id = input("Enter purchase ID to delete: ")
            delete_purchase(purchase_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
