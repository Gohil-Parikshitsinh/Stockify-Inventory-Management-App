import tkinter as tk
from tkinter import ttk, messagebox

# Data storage for products and categories
products = {
    1: {"name": "Product A", "category": "Category 1", "price": "$10", "stock": "100"},
    2: {"name": "Product B", "category": "Category 2", "price": "$15", "stock": "200"},
}
categories = {
    1: "Category 1",
    2: "Category 2",
}

# Helper function to clear main content area
def clear_main_content():
    for widget in main_content.winfo_children():
        widget.destroy()

# Function to handle Product List
def product_list():
    clear_main_content()
    label = tk.Label(main_content, text="Product List", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)
    columns = ("Product ID", "Product Name", "Category", "Price", "Stock")
    tree = ttk.Treeview(main_content, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    for pid, pdata in products.items():
        tree.insert("", tk.END, values=(pid, pdata["name"], pdata["category"], pdata["price"], pdata["stock"]))
    tree.pack(pady=10)

# Function to handle Category List
def category_list():
    clear_main_content()
    label = tk.Label(main_content, text="Category List", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)
    columns = ("Category ID", "Category Name")
    tree = ttk.Treeview(main_content, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    for cid, cname in categories.items():
        tree.insert("", tk.END, values=(cid, cname))
    tree.pack(pady=10)

# Function to handle Add Category
def add_category():
    clear_main_content()
    label = tk.Label(main_content, text="Add Category", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)
    tk.Label(main_content, text="Category ID:", bg="white").pack(pady=5)
    id_entry = tk.Entry(main_content, width=30)
    id_entry.pack(pady=5)
    tk.Label(main_content, text="Category Name:", bg="white").pack(pady=5)
    name_entry = tk.Entry(main_content, width=30)
    name_entry.pack(pady=5)

    def submit_category():
        cid = id_entry.get()
        name = name_entry.get()
        if not cid.isdigit():
            messagebox.showerror("Error", "Category ID must be a number.")
            return
        cid = int(cid)
        if cid in categories:
            messagebox.showerror("Error", f"Category ID {cid} already exists.")
            return
        if not name:
            messagebox.showerror("Error", "Category Name is required.")
            return
        categories[cid] = name
        messagebox.showinfo("Success", f"Category '{name}' added successfully.")

    tk.Button(main_content, text="Submit", command=submit_category).pack(pady=10)

# Function to handle Remove Category
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

# Function to handle Add Product
def add_product():
    clear_main_content()
    label = tk.Label(main_content, text="Add Product", font=("Arial", 16), bg="white", fg="#333")
    label.pack(pady=10)
    tk.Label(main_content, text="Product ID:", bg="white").pack(pady=5)
    id_entry = tk.Entry(main_content, width=30)
    id_entry.pack(pady=5)
    tk.Label(main_content, text="Product Name:", bg="white").pack(pady=5)
    name_entry = tk.Entry(main_content, width=30)
    name_entry.pack(pady=5)
    tk.Label(main_content, text="Category:", bg="white").pack(pady=5)
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(main_content, textvariable=category_var, state="readonly", width=27)
    category_dropdown['values'] = list(categories.values())
    category_dropdown.pack(pady=5)
    tk.Label(main_content, text="Price:", bg="white").pack(pady=5)
    price_entry = tk.Entry(main_content, width=30)
    price_entry.pack(pady=5)
    tk.Label(main_content, text="Stock:", bg="white").pack(pady=5)
    stock_entry = tk.Entry(main_content, width=30)
    stock_entry.pack(pady=5)

    def submit_product():
        pid = id_entry.get()
        name = name_entry.get()
        category = category_var.get()
        price = price_entry.get()
        stock = stock_entry.get()
        if not pid.isdigit():
            messagebox.showerror("Error", "Product ID must be a number.")
            return
        pid = int(pid)
        if pid in products:
            messagebox.showerror("Error", f"Product ID {pid} already exists.")
            return
        if not name or not category or not price or not stock:
            messagebox.showerror("Error", "All fields are required.")
            return
        products[pid] = {
            "name": name,
            "category": category,
            "price": price,
            "stock": stock,
        }
        messagebox.showinfo("Success", f"Product '{name}' added successfully.")

    tk.Button(main_content, text="Submit", command=submit_product).pack(pady=10)

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
root.state("zoomed")
root.resizable(False, False)

# Sidebar frame
sidebar = tk.Frame(root, bg="#f5f5f5", width=200)
sidebar.pack(side="left", fill="y")

# Main content frame
main_content = tk.Frame(root, bg="white")
main_content.pack(side="right", fill="both", expand=True)

# Sidebar Menu Items
menu_items = [
    ("Product List", product_list),
    ("Category List", category_list),
    ("Add Category", add_category),
    ("Remove Category", remove_category),
    ("Update Category", update_category),
    ("Add Product", add_product),
    ("Remove Product", remove_product),
]

for text, command in menu_items:
    tk.Button(
        sidebar,
        text=text,
        font=("Arial", 12),
        bg="#ffffff",
        fg="#333333",
        activebackground="#e0f7fa",
        activeforeground="#00796b",
        relief="flat",
        command=command,
    ).pack(fill="x", pady=5, padx=10)

# Run the application
root.mainloop()
