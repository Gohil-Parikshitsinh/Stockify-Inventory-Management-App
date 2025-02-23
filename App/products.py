import random
import string
from data import categories, products

# products = {}  # Stores products as {product_id: {"name": name, "category_id": category_id, "price": price, "stock": stock}}

# Generate a unique random product ID starting with 'P' and 7 random alphanumeric characters
def generate_product_id():
    while True:
        product_id = "P" + ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        if product_id not in products:  # Ensure ID is unique
            return product_id

# Add a new product
def add_product(name, category_id, price, stock):
    if category_id not in categories:
        print(f"Category ID '{category_id}' does not exist. Please enter a valid category ID.")
        return
    product_id = generate_product_id()
    products[product_id] = {
        "name": name,
        "category_id": category_id,
        "price": price,
        "stock": stock
    }
    print(f"Product '{name}' added successfully with ID: {product_id}.")

# View all products
def view_products():
    if products:
        print("\nProducts:")
        for product_id, details in products.items():
            print(f"ID: {product_id}, Name: {details['name']}, Category ID: {details['category_id']}, Price: {details['price']}, Stock: {details['stock']}")
    else:
        print("No products available.")

# Update a product
def update_product(product_id, name=None, category_id=None, price=None, stock=None):
    if product_id in products:
        if category_id and category_id not in categories:
            print(f"Category ID '{category_id}' does not exist. Please enter a valid category ID.")
            return
        if name:
            products[product_id]['name'] = name
        if category_id:
            products[product_id]['category_id'] = category_id
        if price is not None:
            products[product_id]['price'] = price
        if stock is not None:
            products[product_id]['stock'] = stock
        print(f"Product ID '{product_id}' updated successfully.")
    else:
        print(f"Product ID '{product_id}' not found.")

# Delete a product
def delete_product(product_id):
    if product_id in products:
        del products[product_id]
        print(f"Product ID '{product_id}' deleted successfully.")
    else:
        print(f"Product ID '{product_id}' not found.")

# Product menu
def products_menu():
    while True:
        print("\nProducts Menu:")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            view_products()
        elif choice == "2":
            name = input("Enter product name: ")
            category_id = input("Enter category ID: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            add_product(name, category_id, price, stock)
        elif choice == "3":
            product_id = input("Enter product ID to update: ")
            name = input("Enter new product name (leave blank to keep current): ") or None
            category_id = input("Enter new category ID (leave blank to keep current): ") or None
            price = input("Enter new price (leave blank to keep current): ")
            stock = input("Enter new stock (leave blank to keep current): ")
            update_product(
                product_id,
                name=name,
                category_id=category_id,
                price=float(price) if price else None,
                stock=int(stock) if stock else None
            )
        elif choice == "4":
            product_id = input("Enter product ID to delete: ")
            delete_product(product_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
