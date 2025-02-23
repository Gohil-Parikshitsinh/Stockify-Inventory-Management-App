import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox, filedialog, ttk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import string
from datetime import datetime
from datetime import date

# import matplotlib.pyplot as plt

# Function to handle button click events for sidebar
def show_content(content, active_button=None):
    # Clear the main content area
    for widget in main_content.winfo_children():
        widget.destroy()

    # Highlight the active button
    for btn in sidebar_buttons:
        btn.config(bg="#ffffff", fg="#333333", relief="flat")
    if active_button:
        active_button.config(bg="#e0f7fa", fg="#00796b", relief="solid")

    # Show specific content for the Dashboard
    if content == "Dashboard":
        show_dashboard()
    else:
        label = tk.Label(main_content, text=f"{content} Content", font=("Arial", 16), bg="white", fg="#333333")
        label.pack(pady=20)

# Helper function to clear main content area
def clear_main_content():
    for widget in main_content.winfo_children():
        widget.destroy()

# Function to dynamically update card values
def update_card_value(card_label, new_value):
    card_label.config(text=new_value)

# Function to update the Sales graph
def update_sales_graph():
    global sales_ax, sales_canvas
    # Simulate changing sales data
    new_sales_data = [5500, 7500, 9000, 9500]
    sales_ax.clear()  # Clear the previous plot
    sales_ax.plot([1, 2, 3, 4], new_sales_data, marker="o", color="#00796b", label="Sales")
    sales_ax.set_title("Sales Over Time", fontsize=10)
    sales_ax.set_xlabel("Quarter")
    sales_ax.set_ylabel("Sales ($)")
    sales_ax.legend()
    sales_canvas.draw()  # Redraw the canvas with updated data

# Function to update the Profit graph
def update_profit_graph():
    global profit_ax, profit_canvas
    # Simulate changing profit data
    new_profit_data = [2500, 3500, 4500, 5500]
    profit_ax.clear()  # Clear the previous plot
    profit_ax.bar(["Q1", "Q2", "Q3", "Q4"], new_profit_data, color="#ff8a65", label="Profit")
    profit_ax.set_title("Profit Over Time", fontsize=10)
    profit_ax.set_xlabel("Quarter")
    profit_ax.set_ylabel("Profit ($)")
    profit_ax.legend()
    profit_canvas.draw()  # Redraw the canvas with updated data

# Function to add graphs below the cards
def add_graphs(dashboard):
    global sales_ax, sales_canvas, profit_ax, profit_canvas

    # Sales Graph
    sales_fig = plt.Figure(figsize=(6, 4), dpi=100)
    sales_ax = sales_fig.add_subplot(111)
    sales_ax.plot([1, 2, 3, 4], [5000, 7000, 8500, 9000], marker="o", color="#00796b", label="Sales")
    sales_ax.set_title("Sales Over Time", fontsize=10)
    sales_ax.set_xlabel("Quarter")
    sales_ax.set_ylabel("Sales ($)")
    sales_ax.legend()

    sales_canvas = FigureCanvasTkAgg(sales_fig, dashboard)
    sales_canvas.get_tk_widget().grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

    # Profit Graph
    profit_fig = plt.Figure(figsize=(6, 4), dpi=100)
    profit_ax = profit_fig.add_subplot(111)
    profit_ax.bar(["Q1", "Q2", "Q3", "Q4"], [2000, 3000, 4000, 5000], color="#ff8a65", label="Profit")
    profit_ax.set_title("Profit Over Time", fontsize=10)
    profit_ax.set_xlabel("Quarter")
    profit_ax.set_ylabel("Profit ($)")
    profit_ax.legend()

    profit_canvas = FigureCanvasTkAgg(profit_fig, dashboard)
    profit_canvas.get_tk_widget().grid(row=2, column=2, columnspan=2, pady=10, sticky="nsew")

    # Simulate dynamic updates every 3 seconds
    root.after(3000, update_sales_graph)  # Update Sales graph
    root.after(3000, update_profit_graph)  # Update Profit graph

# Function to create the dashboard content
def show_dashboard():
    dashboard = tk.Frame(main_content, bg="white", padx=20, pady=20)
    dashboard.pack(fill="both", expand=True)

    # Set row and column weights to evenly distribute space
    dashboard.grid_rowconfigure(0, weight=0)  # First row (cards) should take up available space
    dashboard.grid_rowconfigure(1, weight=0)  # Second row (graphs) will be auto-adjusted
    dashboard.grid_rowconfigure(2, weight=0)  # Second row (graphs) will take up available space
    dashboard.grid_columnconfigure(0, weight=0)  # First column (cards) will take up equal space
    dashboard.grid_columnconfigure(1, weight=0)  # Second column (cards) will take up equal space
    dashboard.grid_columnconfigure(2, weight=0)  # Third column (cards) will take up equal space
    dashboard.grid_columnconfigure(3, weight=0)  # Fourth column (cards) will take up equal space

    # Data for dashboard cards
    cards = [
        {"title": "Total Purchase Due", "icon": "📦", "bg": "#e3f2fd", "value": "$1,200"},
        {"title": "Total Sales Due", "icon": "🛒", "bg": "#ffe0b2", "value": "$950"},
        {"title": "Total Sales", "icon": "📈", "bg": "#e8f5e9", "value": "$10,500"},
        {"title": "Total Profit", "icon": "💰", "bg": "#fce4ec", "value": "$3,200"},
        {"title": "Customers", "icon": "👥", "bg": "#f3e5f5", "value": "250"},
        {"title": "Suppliers", "icon": "🏭", "bg": "#ffccbc", "value": "45"},
        {"title": "Purchase Invoices", "icon": "📑", "bg": "#e1f5fe", "value": "320"},
        {"title": "Sales Invoices", "icon": "📜", "bg": "#d7ccc8", "value": "410"},
    ]

    rows = 2
    cols = 4
    card_labels = []  # To store card value labels for dynamic updates
    for i in range(rows):
        for j in range(cols):
            card = cards[i * cols + j]

            # Card frame
            card_frame = tk.Frame(dashboard, bg=card["bg"], width=150, height=200, relief="ridge", bd=2)
            card_frame.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
            card_frame.grid_propagate(False)

            # Icon
            icon_label = tk.Label(card_frame, text=card["icon"], font=("Arial", 24), bg=card["bg"], fg="#333")
            icon_label.pack(side="left", padx=10)

            # Value
            value_label = tk.Label(card_frame, text=card["value"], font=value_font, bg=card["bg"], fg="#333")
            value_label.pack(anchor="n", pady=10)
            card_labels.append(value_label)

            # Title
            title_label = tk.Label(card_frame, text=card["title"], font=title_font, bg=card["bg"], fg="#555")
            title_label.pack(anchor="s", pady=5)

    # Add graphs below cards
    add_graphs(dashboard)


def product_list():
    clear_main_content()
    label = tk.Label(main_content, text="Product List", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)

    # Table for products
    columns = ("Product ID", "Product Name", "Category", "Price", "Stock")
    tree = ttk.Treeview(main_content, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    for pid, pdata in products.items():
        tree.insert("", tk.END, values=(pid, pdata["name"], pdata["category"], pdata["price"], pdata["stock"]))
    tree.pack(pady=10)

def add_category():
    clear_main_content()
    tk.Label(main_content, text="Add Category", font=("Arial", 16), bg="white").pack(pady=10)
    tk.Label(main_content, text="Category ID:", bg="white").pack()
    id_entry = tk.Entry(main_content)
    id_entry.pack()
    tk.Label(main_content, text="Category Name:", bg="white").pack()
    name_entry = tk.Entry(main_content)
    name_entry.pack()

    def submit():
        cid = id_entry.get()
        name = name_entry.get()
        if not cid.isdigit() or not name:
            messagebox.showerror("Error", "Invalid inputs")
            return
        categories[int(cid)] = name
        messagebox.showinfo("Success", f"Added category '{name}'")
    tk.Button(main_content, text="Submit", command=submit).pack(pady=10)

def add_product():
    clear_main_content()
    tk.Label(main_content, text="Add Product", font=("Arial", 16), bg="white").pack(pady=10)
    tk.Label(main_content, text="Product ID:", bg="white").pack()
    id_entry = tk.Entry(main_content)
    id_entry.pack()
    tk.Label(main_content, text="Product Name:", bg="white").pack()
    name_entry = tk.Entry(main_content)
    name_entry.pack()
    tk.Label(main_content, text="Category (Dropdown):", bg="white").pack()
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(main_content, textvariable=category_var, state="readonly")
    category_dropdown["values"] = list(categories.values())
    category_dropdown.pack()
    tk.Label(main_content, text="Price:", bg="white").pack()
    price_entry = tk.Entry(main_content)
    price_entry.pack()
    tk.Label(main_content, text="Stock:", bg="white").pack()
    stock_entry = tk.Entry(main_content)
    stock_entry.pack()

    def submit():
        pid = id_entry.get()
        name = name_entry.get()
        category = category_var.get()
        price = price_entry.get()
        stock = stock_entry.get()
        if not pid.isdigit() or not name or not category or not price or not stock:
            messagebox.showerror("Error", "All fields are required")
            return
        products[int(pid)] = {"name": name, "category": category, "price": price, "stock": stock}
        messagebox.showinfo("Success", f"Added product '{name}'")
    tk.Button(main_content, text="Submit", command=submit).pack(pady=10)

def remove_category():
    clear_main_content()
    label = tk.Label(main_content, text="Remove Category", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)
    tk.Label(main_content, text="Category ID:", bg="white").pack(pady=5)
    id_entry = tk.Entry(main_content, width=30)
    id_entry.pack(pady=5)

    def submit_remove():
        cid = id_entry.get()
        if not cid.isdigit():
            messagebox.showerror("Error", "Category ID must be a number.")
            return
        cid = int(cid)
        if cid not in categories:
            messagebox.showerror("Error", f"Category ID {cid} does not exist.")
            return
        del categories[cid]
        messagebox.showinfo("Success", f"Category ID {cid} removed successfully.")

    tk.Button(main_content, text="Submit", command=submit_remove).pack(pady=10)

# Function to handle Update Category
def update_category():
    clear_main_content()
    label = tk.Label(main_content, text="Update Category", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)
    tk.Label(main_content, text="Category ID:", bg="white").pack(pady=5)
    id_entry = tk.Entry(main_content, width=30)
    id_entry.pack(pady=5)
    tk.Label(main_content, text="New Category Name (leave blank to skip):", bg="white").pack(pady=5)
    name_entry = tk.Entry(main_content, width=30)
    name_entry.pack(pady=5)

    def submit_update():
        cid = id_entry.get()
        if not cid.isdigit():
            messagebox.showerror("Error", "Category ID must be a number.")
            return
        cid = int(cid)
        if cid not in categories:
            messagebox.showerror("Error", f"Category ID {cid} does not exist.")
            return
        name = name_entry.get()
        if name:
            categories[cid] = name
            messagebox.showinfo("Success", f"Category ID {cid} updated successfully.")
        else:
            messagebox.showinfo("Info", "No changes made.")

    tk.Button(main_content, text="Submit", command=submit_update).pack(pady=10)

# Function to handle Remove Product
def remove_product():
    clear_main_content()
    label = tk.Label(main_content, text="Remove Product", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)
    tk.Label(main_content, text="Product ID:", bg="white").pack(pady=5)
    id_entry = tk.Entry(main_content, width=30)
    id_entry.pack(pady=5)

    def submit_remove():
        pid = id_entry.get()
        if not pid.isdigit():
            messagebox.showerror("Error", "Product ID must be a number.")
            return
        pid = int(pid)
        if pid not in products:
            messagebox.showerror("Error", f"Product ID {pid} does not exist.")
            return
        del products[pid]
        messagebox.showinfo("Success", f"Product ID {pid} removed successfully.")

    tk.Button(main_content, text="Submit", command=submit_remove).pack(pady=10)

# Function to handle Update Product
def update_product():
    clear_main_content()
    tk.Label(main_content, text="Update Product", font=("Arial", 16), bg="white").pack(pady=10)

    tk.Label(main_content, text="Product ID:", bg="white").pack(pady=5)
    id_entry = tk.Entry(main_content)
    id_entry.pack(pady=5)

    tk.Label(main_content, text="New Product Name (leave blank to skip):", bg="white").pack(pady=5)
    name_entry = tk.Entry(main_content)
    name_entry.pack(pady=5)

    tk.Label(main_content, text="New Category (leave blank to skip):", bg="white").pack(pady=5)
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(main_content, textvariable=category_var, state="readonly", width=27)
    category_dropdown['values'] = list(categories.values())  # Populate with available categories
    category_dropdown.pack(pady=5)

    tk.Label(main_content, text="New Price (leave blank to skip):", bg="white").pack(pady=5)
    price_entry = tk.Entry(main_content)
    price_entry.pack(pady=5)

    tk.Label(main_content, text="New Stock (leave blank to skip):", bg="white").pack(pady=5)
    stock_entry = tk.Entry(main_content)
    stock_entry.pack(pady=5)

    def submit_update():
        pid = id_entry.get()

        # Validation: Check if ID is entered
        if not pid.isdigit():
            messagebox.showerror("Error", "Product ID must be a number.")
            return

        pid = int(pid)

        # Check if the product exists
        if pid not in products:
            messagebox.showerror("Error", f"Product ID {pid} does not exist.")
            return

        # Update fields if not empty
        name = name_entry.get()
        category = category_var.get()
        price = price_entry.get()
        stock = stock_entry.get()

        if name:
            products[pid]["name"] = name
        if category:
            products[pid]["category"] = category
        if price:
            products[pid]["price"] = price
        if stock:
            products[pid]["stock"] = stock

        messagebox.showinfo("Success", f"Product ID {pid} updated successfully.")

    tk.Button(main_content, text="Submit", command=submit_update).pack(pady=10)

# Main application window
root = tk.Tk()
root.title("Inventory Management Software")
root.state("zoomed")  # Open in full-screen mode
root.config(bg="white")
root.resizable(False, False)  # Disable resizing

# Create custom fonts
value_font = Font(family="Arial", size=16, weight="bold")
title_font = Font(family="Arial", size=12)


# Sidebar frame
sidebar = tk.Frame(root, bg="#f5f5f5", width=200)
sidebar.pack(side="left", fill="y")

# Sidebar title
title_label = tk.Label(sidebar, text="Menu", bg="#f5f5f5", fg="#333333", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Sidebar buttons
buttons = [
    ("Dashboard", "Dashboard"),
]


sidebar_buttons = []
for text, content in buttons:
    btn = tk.Button(
        sidebar,
        text=text,
        font=("Arial", 14),
        bg="#ffffff",
        fg="#333333",
        activebackground="#e0f7fa",
        activeforeground="#00796b",
        relief="flat",
        command=lambda c=content, b=None: show_content(c, b),
    )
    btn.pack(fill="x", pady=5, padx=10)
    sidebar_buttons.append(btn)


# Sidebar dropdown for Product
product_frame = tk.Frame(sidebar, bg="#f5f5f5")  # Create a frame for the Product dropdown
product_label = tk.Label(
    product_frame, text="Product", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#333333"
)
product_label.pack(pady=(10, 0))


# Data storage for products and categories
products = {
    1: {"name": "Product A", "category": "Category 1", "price": "$10", "stock": "100"},
    2: {"name": "Product B", "category": "Category 2", "price": "$15", "stock": "200"},
}
categories = {
    1: "Category 1",
    2: "Category 2",
}

# Dropdown buttons for product menu
product_buttons = [
    ("Product List", product_list),
    ("Add Category", add_category),
    ("Remove Category", remove_category),
    ("Update Category", update_category),
    ("Add Product", add_product),
    ("Remove Product", remove_product),
    ("Update Product", update_product),
]

# Create individual buttons for each product-related action
for text, command in product_buttons:
    tk.Button(
        product_frame,
        text=f"  {text}",  # Add padding for a dropdown effect
        font=("Arial", 12),
        bg="#ffffff",
        fg="#333333",
        activebackground="#e0f7fa",
        activeforeground="#00796b",
        relief="flat",
        command=command,  # Assign the corresponding function
    ).pack(fill="x", padx=20, pady=2)

product_frame.pack(fill="x", pady=5)  # Add the product dropdown to the sidebar

# Function to generate a unique Purchase ID
def generate_purchase_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Function to clear main content area
def clear_main_content():
    for widget in main_content.winfo_children():
        widget.destroy()

# View Purchase List
def purchase_list():
    clear_main_content()
    label = tk.Label(main_content, text="Purchase List", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)

    columns = ("Purchase ID", "Product ID", "Quantity", "Purchase Price", "Total Cost", "Date")
    tree = ttk.Treeview(main_content, columns=columns, show="headings", height=10)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    for purchase_id, purchase_data in purchases.items():
        tree.insert("", tk.END, values=(
            purchase_id, purchase_data["product_id"], purchase_data["quantity"],
            purchase_data["purchase_price"], purchase_data["total_cost"], purchase_data["date"]
        ))

    tree.pack(pady=10)


def add_purchase():
    clear_main_content()
    label = tk.Label(main_content, text="Add Purchase", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)

    tk.Label(main_content, text="Product ID:", bg="white").pack(pady=5)
    product_entry = tk.Entry(main_content)
    product_entry.pack(pady=5)

    tk.Label(main_content, text="Quantity:", bg="white").pack(pady=5)
    quantity_entry = tk.Entry(main_content)
    quantity_entry.pack(pady=5)

    tk.Label(main_content, text="Purchase Price:", bg="white").pack(pady=5)
    purchase_price_entry = tk.Entry(main_content)
    purchase_price_entry.pack(pady=5)

    def submit_purchase():
        product_id = product_entry.get().strip()
        quantity = quantity_entry.get().strip()
        purchase_price = purchase_price_entry.get().strip()

        # Validation
        if not product_id.isdigit():
            messagebox.showerror("Error", "Product ID must be a number.")
            return

        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showerror("Error", "Quantity must be a positive number.")
            return

        if not purchase_price.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "Purchase price must be a valid number.")
            return

        product_id = int(product_id)
        quantity = int(quantity)
        purchase_price = float(purchase_price)

        # Check if product exists
        if product_id not in products:
            messagebox.showerror("Error", f"Product ID {product_id} does not exist.")
            return

        # Generate Purchase ID
        purchase_id = generate_purchase_id()
        total_cost = quantity * purchase_price
        purchase_date = date.today().strftime("%Y-%m-%d")  # FIXED THE ISSUE

        # Store purchase details
        purchases[purchase_id] = {
            "product_id": product_id,
            "quantity": quantity,
            "purchase_price": purchase_price,
            "total_cost": total_cost,
            "date": purchase_date
        }

        # Update stock automatically
        products[product_id]["stock"] += quantity

        messagebox.showinfo("Success", f"Purchase ID {purchase_id} added successfully.")
        purchase_list()  # Refresh the purchase list

    tk.Button(main_content, text="Submit", command=submit_purchase).pack(pady=10)


# Update Purchase
def update_purchase():
    clear_main_content()
    label = tk.Label(main_content, text="Update Purchase", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)

    tk.Label(main_content, text="Purchase ID:", bg="white").pack(pady=5)
    purchase_id_entry = tk.Entry(main_content)
    purchase_id_entry.pack(pady=5)

    tk.Label(main_content, text="New Quantity (leave blank to skip):", bg="white").pack(pady=5)
    quantity_entry = tk.Entry(main_content)
    quantity_entry.pack(pady=5)

    tk.Label(main_content, text="New Purchase Price (leave blank to skip):", bg="white").pack(pady=5)
    purchase_price_entry = tk.Entry(main_content)
    purchase_price_entry.pack(pady=5)

    def submit_update():
        purchase_id = purchase_id_entry.get()
        if purchase_id not in purchases:
            messagebox.showerror("Error", "Invalid Purchase ID.")
            return

        quantity = quantity_entry.get()
        purchase_price = purchase_price_entry.get()

        if quantity:
            purchases[purchase_id]["quantity"] = int(quantity)
        if purchase_price:
            purchases[purchase_id]["purchase_price"] = float(purchase_price)

        purchases[purchase_id]["total_cost"] = purchases[purchase_id]["quantity"] * purchases[purchase_id]["purchase_price"]
        messagebox.showinfo("Success", f"Purchase ID {purchase_id} updated successfully.")

    tk.Button(main_content, text="Submit", command=submit_update).pack(pady=10)

# Remove Purchase
def remove_purchase():
    clear_main_content()
    label = tk.Label(main_content, text="Remove Purchase", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)

    tk.Label(main_content, text="Purchase ID:", bg="white").pack(pady=5)
    purchase_id_entry = tk.Entry(main_content)
    purchase_id_entry.pack(pady=5)

    def submit_remove():
        purchase_id = purchase_id_entry.get()
        if purchase_id not in purchases:
            messagebox.showerror("Error", "Invalid Purchase ID.")
            return

        del purchases[purchase_id]
        messagebox.showinfo("Success", f"Purchase ID {purchase_id} removed successfully.")

    tk.Button(main_content, text="Submit", command=submit_remove).pack(pady=10)

from tkinter import filedialog
from datetime import datetime

def purchase_report():
    clear_main_content()

    label = tk.Label(main_content, text="Generate Purchase Report", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)

    tk.Label(main_content, text="Start Date (YYYY-MM-DD):", bg="white").pack(pady=5)
    start_date_entry = tk.Entry(main_content)
    start_date_entry.pack(pady=5)

    tk.Label(main_content, text="End Date (YYYY-MM-DD):", bg="white").pack(pady=5)
    end_date_entry = tk.Entry(main_content)
    end_date_entry.pack(pady=5)

    def generate_report():
        start_date_str = start_date_entry.get().strip()
        end_date_str = end_date_entry.get().strip()

        # Validate date format
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
            return

        # Filter purchases by date
        filtered_purchases = [
            (pid, details) for pid, details in purchases.items()
            if start_date <= datetime.strptime(details["date"], "%Y-%m-%d") <= end_date
        ]

        if not filtered_purchases:
            messagebox.showinfo("Info", "No purchases found in the selected date range.")
            return

        # Ask user where to save the file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")],
                                                 title="Save Purchase Report")
        if not file_path:
            return

        # Write report to file
        with open(file_path, "w") as file:
            file.write(f"Purchase Report ({start_date_str} to {end_date_str})\n")
            file.write("=" * 50 + "\n")
            for pid, details in filtered_purchases:
                file.write(f"Purchase ID: {pid}\n")
                file.write(f"Product ID: {details['product_id']}\n")
                file.write(f"Quantity: {details['quantity']}\n")
                file.write(f"Purchase Price: {details['purchase_price']}\n")
                file.write(f"Total Cost: {details['total_cost']}\n")
                file.write(f"Date: {details['date']}\n")
                file.write("-" * 50 + "\n")

        messagebox.showinfo("Success", f"Purchase report saved to {file_path}")

    tk.Button(main_content, text="Generate Report", command=generate_report).pack(pady=10)


# Purchase section in Sidebar
purchase_frame = tk.Frame(sidebar, bg="#f5f5f5")
purchase_label = tk.Label(purchase_frame, text="Purchase", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#333333")
purchase_label.pack(pady=(10, 0))
purchase_buttons = [
    ("Purchase List", purchase_list),
    ("Add Purchase", add_purchase),
    ("Update Purchase", update_purchase),
    ("Remove Purchase", remove_purchase),
    ("Purchase Report", purchase_report),  # ✅ New Button
]

purchases = {}


for text, command in purchase_buttons:
    tk.Button(
        purchase_frame,
        text=f"  {text}",
        font=("Arial", 12),
        bg="#ffffff",
        fg="#333333",
        activebackground="#e0f7fa",
        activeforeground="#00796b",
        relief="flat",
        command=command,
    ).pack(fill="x", padx=20, pady=2)

purchase_frame.pack(fill="x", pady=5)



sales = {}  # Dictionary to store sales
import random
import string
import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# Function to generate a unique Sale ID (random letters + numbers)
def generate_sale_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Function to add a new sale
def add_sale():
    def submit_sale():
        sale_id = generate_sale_id()
        product_id = product_id_entry.get()
        quantity = quantity_entry.get()
        price = price_entry.get()
        date = datetime.date.today().strftime("%Y-%m-%d")

        if not product_id or not quantity or not price:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            quantity = int(quantity)
            price = float(price)
            total = quantity * price

            # Save to dictionary
            sales[sale_id] = {
                "product_id": product_id,
                "quantity": quantity,
                "price": price,
                "total": total,
                "date": date,
            }

            # Save sales data to file
            with open("sales_data.txt", "a") as file:
                file.write(f"{sale_id}|{product_id}|{quantity}|{price}|{total}|{date}\n")

            messagebox.showinfo("Success", f"Sale {sale_id} added successfully!")
            sale_window.destroy()

        except ValueError:
            messagebox.showerror("Error", "Invalid quantity or price!")

    sale_window = tk.Toplevel()
    sale_window.title("Add Sale")
    sale_window.geometry("350x300")

    tk.Label(sale_window, text="Product ID:").pack()
    product_id_entry = tk.Entry(sale_window)
    product_id_entry.pack()

    tk.Label(sale_window, text="Quantity:").pack()
    quantity_entry = tk.Entry(sale_window)
    quantity_entry.pack()

    tk.Label(sale_window, text="Price:").pack()
    price_entry = tk.Entry(sale_window)
    price_entry.pack()

    submit_btn = tk.Button(sale_window, text="Add Sale", command=submit_sale)
    submit_btn.pack(pady=10)


def view_sales():
    clear_main_content()

    label = tk.Label(main_content, text="Sales Records", font=("Arial", 16, "bold"), bg="white", fg="#333")
    label.pack(pady=10)

    columns = ("Sale ID", "Product ID", "Quantity", "Price", "Total", "Date")

    sales_tree = ttk.Treeview(main_content, columns=columns, show="headings", height=15)

    # Define column headings
    for col in columns:
        sales_tree.heading(col, text=col)
        sales_tree.column(col, width=120)

    # Add scrollbar
    scrollbar = ttk.Scrollbar(main_content, orient="vertical", command=sales_tree.yview)
    sales_tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Load sales data into the view
    try:
        with open("sales_data.txt", "r") as file:
            for line in file:
                sale_id, product_id, quantity, price, total, date = line.strip().split("|")
                sales_tree.insert("", tk.END, values=(sale_id, product_id, quantity, price, total, date))
    except FileNotFoundError:
        pass  # If file doesn't exist, keep sales list empty

    sales_tree.pack(pady=10, fill="both", expand=True)

def remove_sale():
    def delete_selected():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No sale selected!")
            return

        sale_id = tree.item(selected_item)["values"][0]
        tree.delete(selected_item)

        if sale_id in sales:
            del sales[sale_id]

        # Update file after deletion
        with open("sales_data.txt", "w") as file:
            for key, sale_data in sales.items():
                file.write(f"{key}|{sale_data['product_id']}|{sale_data['quantity']}|{sale_data['price']}|{sale_data['total']}|{sale_data['date']}\n")

        messagebox.showinfo("Success", f"Sale {sale_id} removed!")

    clear_main_content()
    label = tk.Label(main_content, text="Remove Sale", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)

    columns = ("Sale ID", "Product ID", "Quantity", "Price", "Total", "Date")
    tree = ttk.Treeview(main_content, columns=columns, show="headings", height=10)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    try:
        with open("sales_data.txt", "r") as file:
            for line in file:
                sale_id, product_id, quantity, price, total, date = line.strip().split("|")
                tree.insert("", tk.END, values=(sale_id, product_id, quantity, price, total, date))
    except FileNotFoundError:
        pass

    tree.pack(pady=10)
    delete_btn = tk.Button(main_content, text="Delete Sale", command=delete_selected)
    delete_btn.pack(pady=10)

def export_sales_report():
    def save_report():
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()
        report_file = "sales_report.txt"

        with open(report_file, "w") as file:
            file.write("Sale ID | Product ID | Quantity | Price | Total | Date\n")
            file.write("-" * 50 + "\n")

            with open("sales_data.txt", "r") as sales_file:
                for line in sales_file:
                    sale_id, product_id, quantity, price, total, date = line.strip().split("|")

                    if start_date <= date <= end_date:
                        file.write(f"{sale_id} | {product_id} | {quantity} | {price} | {total} | {date}\n")

        messagebox.showinfo("Success", f"Sales report saved as {report_file}")
        report_window.destroy()

    report_window = tk.Toplevel()
    report_window.title("Export Sales Report")
    report_window.geometry("300x200")

    tk.Label(report_window, text="Start Date (YYYY-MM-DD):").pack()
    start_date_entry = tk.Entry(report_window)
    start_date_entry.pack()

    tk.Label(report_window, text="End Date (YYYY-MM-DD):").pack()
    end_date_entry = tk.Entry(report_window)
    end_date_entry.pack()

    save_button = tk.Button(report_window, text="Export Report", command=save_report)
    save_button.pack(pady=10)

def update_sale():
    def select_sale():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No sale selected!")
            return

        sale_id = tree.item(selected_item)["values"][0]
        sale_data = sales[sale_id]

        update_window = tk.Toplevel()
        update_window.title("Update Sale")
        update_window.geometry("350x300")

        tk.Label(update_window, text="Product ID:").pack()
        product_id_entry = tk.Entry(update_window)
        product_id_entry.insert(0, sale_data["product_id"])
        product_id_entry.pack()

        tk.Label(update_window, text="Quantity:").pack()
        quantity_entry = tk.Entry(update_window)
        quantity_entry.insert(0, sale_data["quantity"])
        quantity_entry.pack()

        tk.Label(update_window, text="Price:").pack()
        price_entry = tk.Entry(update_window)
        price_entry.insert(0, sale_data["price"])
        price_entry.pack()

        def save_update():
            new_product_id = product_id_entry.get()
            new_quantity = quantity_entry.get()
            new_price = price_entry.get()

            if not new_product_id or not new_quantity or not new_price:
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                new_quantity = int(new_quantity)
                new_price = float(new_price)
                new_total = new_quantity * new_price

                # Update the dictionary
                sales[sale_id] = {
                    "product_id": new_product_id,
                    "quantity": new_quantity,
                    "price": new_price,
                    "total": new_total,
                    "date": sale_data["date"],  # Keep the same date
                }

                # Update the file
                with open("sales_data.txt", "w") as file:
                    for key, sale in sales.items():
                        file.write(f"{key}|{sale['product_id']}|{sale['quantity']}|{sale['price']}|{sale['total']}|{sale['date']}\n")

                messagebox.showinfo("Success", f"Sale {sale_id} updated successfully!")
                update_window.destroy()
                tree.item(selected_item, values=(sale_id, new_product_id, new_quantity, new_price, new_total, sale_data["date"]))

            except ValueError:
                messagebox.showerror("Error", "Invalid quantity or price!")

        save_btn = tk.Button(update_window, text="Save Changes", command=save_update)
        save_btn.pack(pady=10)

    clear_main_content()

    label = tk.Label(main_content, text="Update Sale", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)

    columns = ("Sale ID", "Product ID", "Quantity", "Price", "Total", "Date")
    tree = ttk.Treeview(main_content, columns=columns, show="headings", height=10)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    try:
        with open("sales_data.txt", "r") as file:
            for line in file:
                sale_id, product_id, quantity, price, total, date = line.strip().split("|")
                sales[sale_id] = {"product_id": product_id, "quantity": quantity, "price": price, "total": total, "date": date}
                tree.insert("", tk.END, values=(sale_id, product_id, quantity, price, total, date))
    except FileNotFoundError:
        pass

    tree.pack(pady=10)
    update_btn = tk.Button(main_content, text="Update Selected Sale", command=select_sale)
    update_btn.pack(pady=10)

# Purchase section in Sidebar
sales_frame = tk.Frame(sidebar, bg="#f5f5f5")
sales_label = tk.Label(sales_frame, text="Sales", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#333333")
sales_label.pack(pady=(10, 0))
sales_buttons = [
    ("View Sales", view_sales),
    ("Add Sale", add_sale),
    ("Update Sale", update_sale),
    ("Remove Sale", remove_sale),
    ("Export Sales Report", export_sales_report)
]

sales = {}

for text, command in sales_buttons:
    tk.Button(
        sales_frame,
        text=f"  {text}",
        font=("Arial", 12),
        bg="#ffffff",
        fg="#333333",
        activebackground="#e0f7fa",
        activeforeground="#00796b",
        relief="flat",
        command=command,
    ).pack(fill="x", padx=20, pady=2)

sales_frame.pack(fill="x", pady=5)

# Main content frame
main_content = tk.Frame(root, bg="white")
main_content.pack(side="right", fill="both", expand=True)

# Show Dashboard as default content
show_content("Dashboard", active_button=sidebar_buttons[0])

# Run the Tkinter event loop
root.mainloop()