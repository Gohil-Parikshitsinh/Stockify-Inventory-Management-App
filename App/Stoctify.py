from tkinter import *
from tkinter import ttk

from tkinter.font import Font
from tkinter import ttk, messagebox, Menubutton
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

window = Tk()
style = ttk.Style()

# --------------------------------------FUNCTIONS---------------------------------------------------------------
def openFile():
    print("File has been opened")
def saveFile():
    print("File has been saved")
def cut():
    print("You cut some text")
def copy():
    print("You copied some text")
def paste():
    print("You paste some text")


# -----------------------------------------------MENUBAR ---------------------------------------------------------
menubar =  Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile, compound="left")
fileMenu.add_command(label="Save", command=saveFile, compound="left")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit, compound="left")

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)


# ----------------------------------------------- TABS ---------------------------------------------------------
notebook = ttk.Notebook(window)
dashboardTab = Frame(notebook)
productTab = Frame(notebook)
supplierTab = Frame(notebook)
reportTab =  Frame(notebook)

notebook.add(dashboardTab,text="Dashboard")
notebook.add(productTab,text="Products")
notebook.add(supplierTab,text="Suppliers")
notebook.add(reportTab,text="Reports")

style.configure(
    "TNotebook.Tab",
    padding=[20, 10],  # Increase padding (width, height)
    font=("Arial", 12)  # Optional: Change font size
)

style.map(
    "TNotebook.Tab",
    background=[
        ("selected", "lightblue"),  # Background color for active tab
        ("!selected", "lightgray"),  # Background color for inactive tabs
    ],
    foreground=[
        ("selected", "black"),  # Text color for active tab
        ("!selected", "gray"),  # Text color for inactive tabs
    ],
)

# Add cards to the dashboard tab
card_container = Frame(dashboardTab)
card_container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Create reusable card function with support for columnspan
def create_card(parent, emoji, value, name, row, column):
    card_frame = Frame(parent, bg="white", relief="ridge", bd=2, padx=10, pady=10)
    card_frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    # Emoji icon
    Label(card_frame, text=emoji, font=("Arial", 32), bg="white").grid(row=0, column=0, sticky="w")

    # Value
    Label(card_frame, text=value, font=("Arial", 18, "bold"), fg="green", bg="white").grid(row=0, column=1, sticky="w")

    # Name
    Label(card_frame, text=name, font=("Arial", 12), fg="gray", bg="white").grid(row=1, column=0, columnspan=2, sticky="w")

# Add four cards in a single row, distributed equally
create_card(card_container, "📈", "$50,000", "Sales", 0, 0)
create_card(card_container, "🛒", "1,200", "Orders", 0, 1)
create_card(card_container, "📦", "850", "Products", 0, 2)
create_card(card_container, "👥", "500", "Customers", 0, 3)

# Configure grid weights to make it responsive and fill the screen evenly
card_container.columnconfigure(0, weight=1)
card_container.columnconfigure(1, weight=1)
card_container.columnconfigure(2, weight=1)
card_container.columnconfigure(3, weight=1)
card_container.rowconfigure(0, weight=1)

# Tabs content
Label(productTab,text="Hello this is product tab", width=50, height=25).pack()
Label(supplierTab,text="Hello this is supplier tab", width=50, height=25).pack()
Label(reportTab,text="Hello this is report tab", width=50, height=25).pack()

# Set window to full screen mode
window.attributes("-fullscreen", True)

# Make the notebook container fill the screen as well
notebook.pack(expand=True, fill="both")

window.mainloop()
