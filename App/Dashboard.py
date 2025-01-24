import tkinter as tk


# Function to handle button click events
def show_content(content, active_button=None):
    # Clear the main content area
    for widget in main_content.winfo_children():
        widget.destroy()

    # Set the content in the main area
    label = tk.Label(main_content, text=content, font=("Arial", 16), bg="white", fg="#333333")
    label.pack(pady=20)

    # Reset the background of all buttons to inactive
    for btn in sidebar_buttons:
        btn.config(bg="#ffffff", fg="#333333", relief="flat")

    # Highlight the active button
    if active_button:
        active_button.config(bg="#e0f7fa", fg="#00796b", relief="solid")


# Main application window
root = tk.Tk()
root.title("Inventory Management Software")
root.geometry("800x600")
root.resizable(False, False)
root.config(bg="white")

# Sidebar frame
sidebar = tk.Frame(root, bg="#f5f5f5", width=200)
sidebar.pack(side="left", fill="y")

# Sidebar title
title_label = tk.Label(sidebar, text="Menu", bg="#f5f5f5", fg="#333333", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Sidebar buttons
buttons = [
    ("Dashboard", "Dashboard Content"),
    ("Product", "Product Content"),
    ("Sales", "Sales Content"),
    ("Purchase", "Purchase Content"),
    ("Settings", "Settings Content"),
]

sidebar_buttons = []  # To store references to the buttons

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
        command=lambda c=content, b=None: show_content(c, b),  # Placeholder, updated below
    )
    btn.pack(fill="x", pady=5, padx=10, ipadx=5)
    sidebar_buttons.append(btn)

# Set command with a reference to the button itself
for i, (text, content) in enumerate(buttons):
    sidebar_buttons[i].config(command=lambda c=content, b=sidebar_buttons[i]: show_content(c, b))

# Main content frame
main_content = tk.Frame(root, bg="white")
main_content.pack(side="right", fill="both", expand=True)

# Default content
show_content("Dashboard Content", active_button=sidebar_buttons[0])  # Make Dashboard active by default

# Run the Tkinter event loop
root.mainloop()
