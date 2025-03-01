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
















# Main content frame
main_content = tk.Frame(root, bg="white")
main_content.pack(side="right", fill="both", expand=True)
show_content("Dashboard", active_button=sidebar_buttons[0])

# Run the Tkinter event loop
root.mainloop()
root.mainloop()