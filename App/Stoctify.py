from tkinter import *
from tkinter import ttk

from tkinter.font import Font
from tkinter import ttk, messagebox, Menubutton
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

window = Tk()


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
window.config(menu=menubar) # used to create the menubar
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

# dashboard
Label(dashboardTab,text="Hello this is dashboard", width=50, height=25).pack()



Label(productTab,text="Hello this is product tab", width=50, height=25).pack()
Label(supplierTab,text="Hello this is supplier tab", width=50, height=25).pack()
Label(reportTab,text="Hello this is report tab", width=50, height=25).pack()

notebook.pack(expand=True,fill="both")




window.mainloop()