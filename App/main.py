from users import authenticate_user
from categories import categories_menu
from products import products_menu
from purchases import purchase_menu
from sales import sales_menu
from suppliers import suppliers_menu
from reports import reports_menu
from exceptions import AuthenticationError,InvalidRoleError, InvalidMenuChoiceError

role_menus = {
    "Admin": ["Products", "Suppliers", "Sales", "Purchase", "Reports", "Categories"],
    "Manager": ["Products", "Suppliers", "Sales", "Purchase", "Reports", "Categories"],
    "Sales Staff": ["Sales"],
    "Inventory Staff": ["Products", "Suppliers", "Purchase", "Categories"]
}


def display_menu(role):
    options = role_menus.get(role)
    if options is None:
        raise InvalidRoleError(f"Invalid role: {role}")

    while True:
        print(f"\n{role} Menu:")
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
        print(f"{len(options) + 1}. Logout")

        try:
            handle_menu_selection(role, options)
        except InvalidMenuChoiceError as e:
            print(e)
        except ValueError:
            print("Please enter a valid number.")

def handle_menu_selection(role, options):
    try:
        choice = int(input("\nSelect an option by number: "))
        if 1 <= choice <= len(options):
            selected_option = options[choice - 1]
            call_feature_function(selected_option)
        elif choice == len(options) + 1:  # Logout option
            print("Logging out...")
            exit()  # Exit the program
        else:
            raise InvalidMenuChoiceError("Invalid choice. Please select a valid option.")
    except ValueError:
        raise

def call_feature_function(option):
    feature_functions = {
        "Products": products_menu,
        "Suppliers": suppliers_menu,
        "Sales": sales_menu,
        "Purchase": purchase_menu,
        "Reports": reports_menu,
        "Categories": categories_menu,
    }
    func = feature_functions.get(option)
    if func:
        try:
            func()
        except Exception as e:
            print(f"An error occurred while executing {option}: {e}")
    else:
        print("Feature not yet implemented.")

def main():
    print("Welcome to Inventory Management System")

    try:
        # User login
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Authenticate user
        user = authenticate_user(username, password)
        if not user:
            raise AuthenticationError("Invalid username or password.")

        print(f"Login successful! Welcome, {user.username} ({user.role}).")
        display_menu(user.role)

    except AuthenticationError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
