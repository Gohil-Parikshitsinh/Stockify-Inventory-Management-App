from users import authenticate_user
from categories import categories_menu
from products import products_menu
from purchases import purchase_menu
from sales import sales_menu
from suppliers import suppliers_menu
from reports import reports_menu


# Role-based menus
role_menus = {
    "Admin": [
        "Products", "Suppliers", "Sales", "Purchase", "Reports", "Invoice", "Customers",
        "Categories", "Stock Management", "Returns & Refunds", "Discounts & Promotions",
        "Audit Logs", "Backup & Restore", "User Roles & Permissions", "Payment Tracking", "Dashboard"
    ],
    "Manager": [
        "Products", "Suppliers", "Sales", "Purchase", "Reports", "Invoice", "Customers",
        "Categories", "Stock Management", "Returns & Refunds", "Discounts & Promotions", "Payment Tracking", "Dashboard"
    ],
    "Sales Staff": [
        "Sales", "Invoice", "Customers", "Returns & Refunds", "Discounts & Promotions", "Payment Tracking", "Dashboard"
    ],
    "Inventory Staff": [
        "Products", "Suppliers", "Purchase", "Categories", "Stock Management", "Dashboard"
    ]
}


def display_menu(role):
    """Displays the role-specific menu and handles continuous navigation."""
    options = role_menus.get(role, [])

    while True:  # Keep showing the menu until user exits
        print(f"\n{role} Menu:")
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
        print(f"{len(options) + 1}. Logout")

        try:
            choice = int(input("\nSelect an option by number: "))
            if 1 <= choice <= len(options):
                selected_option = options[choice - 1]
                call_feature_function(selected_option)
            elif choice == len(options) + 1:  # Logout option
                print("Logging out...")
                break  # Exit the loop, returning control to main()
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a number.")


def handle_menu_selection(role, options):
    """Handles user's menu selection."""
    try:
        choice = int(input("\nSelect an option by number: "))
        if 1 <= choice <= len(options):
            selected_option = options[choice - 1]
            print(f"You selected: {selected_option}")
            call_feature_function(selected_option)
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Please enter a number.")


def call_feature_function(option):
    """Calls the respective feature function based on user selection."""
    feature_functions = {
        "Products": products_menu,
        "Suppliers": suppliers_menu,
        "Sales": sales_menu,
        "Purchase": purchase_menu,
        "Reports": reports_menu,
        "Invoice": invoice_menu,
        "Customers": customers_menu,
        "Categories": categories_menu,
        "Stock Management": stock_management_menu,
        "Returns & Refunds": returns_refunds_menu,
        "Discounts & Promotions": discounts_promotions_menu,
        "Audit Logs": audit_logs_menu,
        "Backup & Restore": backup_restore_menu,
        "User Roles & Permissions": user_roles_permissions_menu,
        "Payment Tracking": payment_tracking_menu,
        "Dashboard": dashboard_menu
    }
    func = feature_functions.get(option)
    if func:
        func()
    else:
        print("Feature not yet implemented.")


def invoice_menu():
    print("Invoice menu selected.")


def customers_menu():
    print("Customers menu selected.")


def stock_management_menu():
    print("Stock Management menu selected.")


def returns_refunds_menu():
    print("Returns & Refunds menu selected.")


def discounts_promotions_menu():
    print("Discounts & Promotions menu selected.")


def audit_logs_menu():
    print("Audit Logs menu selected.")


def backup_restore_menu():
    print("Backup & Restore menu selected.")


def user_roles_permissions_menu():
    print("User Roles & Permissions menu selected.")


def payment_tracking_menu():
    print("Payment Tracking menu selected.")


def dashboard_menu():
    print("Dashboard menu selected.")


def main():
    print("Welcome to Inventory Management System")

    # User login
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Authenticate user
    user = authenticate_user(username, password)
    if user:
        print(f"Login successful! Welcome, {user.username} ({user.role}).")
        display_menu(user.role)
    else:
        print("Invalid username or password.")


if __name__ == "__main__":
    main()
