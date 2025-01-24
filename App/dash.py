import tkinter as tk
from tkinter.font import Font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

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
    sales_fig = plt.Figure(figsize=(4, 2), dpi=100)
    sales_ax = sales_fig.add_subplot(111)
    sales_ax.plot([1, 2, 3, 4], [5000, 7000, 8500, 9000], marker="o", color="#00796b", label="Sales")
    sales_ax.set_title("Sales Over Time", fontsize=10)
    sales_ax.set_xlabel("Quarter")
    sales_ax.set_ylabel("Sales ($)")
    sales_ax.legend()

    sales_canvas = FigureCanvasTkAgg(sales_fig, dashboard)
    sales_canvas.get_tk_widget().grid(row=2, column=0, pady=10, sticky="nsew")

    # Profit Graph
    profit_fig = plt.Figure(figsize=(4, 2), dpi=100)
    profit_ax = profit_fig.add_subplot(111)
    profit_ax.bar(["Q1", "Q2", "Q3", "Q4"], [2000, 3000, 4000, 5000], color="#ff8a65", label="Profit")
    profit_ax.set_title("Profit Over Time", fontsize=10)
    profit_ax.set_xlabel("Quarter")
    profit_ax.set_ylabel("Profit ($)")
    profit_ax.legend()

    profit_canvas = FigureCanvasTkAgg(profit_fig, dashboard)
    profit_canvas.get_tk_widget().grid(row=2, column=1, pady=10, sticky="nsew")

    # Simulate dynamic updates every 3 seconds
    root.after(3000, update_sales_graph)  # Update Sales graph
    root.after(3000, update_profit_graph)  # Update Profit graph

# Function to create the dashboard content
def show_dashboard():
    dashboard = tk.Frame(main_content, bg="white", padx=20, pady=20)
    dashboard.pack(fill="both", expand=True)

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
            card_frame = tk.Frame(dashboard, bg=card["bg"], width=150, height=100, relief="ridge", bd=2)
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
    ("Product", "Product Content"),
    ("Sales", "Sales Content"),
    ("Purchase", "Purchase Content"),
    ("Settings", "Settings Content"),
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

# Set command with a reference to the button itself
for i, (text, content) in enumerate(buttons):
    sidebar_buttons[i].config(command=lambda c=content, b=sidebar_buttons[i]: show_content(c, b))

# Main content frame
main_content = tk.Frame(root, bg="white")
main_content.pack(side="right", fill="both", expand=True)

# Show Dashboard as default content
show_content("Dashboard", active_button=sidebar_buttons[0])

# Run the Tkinter event loop
root.mainloop()
