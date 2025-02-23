import random
import string
from data import categories, products


# categories = {}  # Stores categories as {category_id: name}

# Generate a unique random category ID starting with 'C' and 7 random alphanumeric characters
def generate_category_id():
    while True:
        category_id = "C" + ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        if category_id not in categories:  # Ensure ID is unique
            return category_id

# Add a new category
def add_category(name):
    if name in categories.values():
        print(f"Category '{name}' already exists.")
    else:
        category_id = generate_category_id()
        categories[category_id] = name
        print(f"Category '{name}' added successfully with ID: {category_id}.")

# View all categories
def view_categories():
    if categories:
        print("\nCategories:")
        for category_id, name in categories.items():
            print(f"ID: {category_id}, Name: {name}")
    else:
        print("No categories available.")

# Edit an existing category
def edit_category(category_id, new_name):
    if category_id not in categories:
        print(f"Category ID '{category_id}' does not exist.")
    elif new_name in categories.values():
        print(f"Category '{new_name}' already exists.")
    else:
        categories[category_id] = new_name
        print(f"Category ID '{category_id}' updated to '{new_name}'.")

# Delete a category
def delete_category(category_id):
    if category_id not in categories:
        print(f"Category ID '{category_id}' does not exist.")
    elif any(product['category_id'] == category_id for product in products.values()):
        print(f"Category ID '{category_id}' cannot be deleted as there are products associated with it.")
    else:
        del categories[category_id]
        print(f"Category ID '{category_id}' deleted successfully.")

# Category menu
def categories_menu():
    while True:
        print("\nCategories Menu:")
        print("1. View Categories")
        print("2. Add Category")
        print("3. Update Category")
        print("4. Delete Category")
        print("5. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            view_categories()
        elif choice == "2":
            name = input("Enter category name to add: ")
            add_category(name)
        elif choice == "3":
            category_id = input("Enter category ID to update: ")
            new_name = input("Enter new category name: ")
            edit_category(category_id, new_name)
        elif choice == "4":
            category_id = input("Enter category ID to delete: ")
            delete_category(category_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
