# Inventory Management System

## 📦 Overview
The **Inventory Management System** is a console-based application built with Python that helps businesses efficiently manage their inventory, sales, and purchases. It supports essential features like product and category management, supplier tracking, sales and purchase processing, and automated invoice generation.

## 🚀 Features
### 1. Product Management
- Add, update, and delete products.
- Each product has a unique Product ID.
- Products are linked to categories.

### 2. Category Management
- Add, update, and delete categories.
- Each category has a unique Category ID.

### 3. Supplier Management
- Add, update, and delete suppliers.
- Track products supplied by each supplier.

### 4. Sales Management
- Add, update, and delete sales entries.
- Automatically generate sales invoices (`SA-XXXXXXXX`).
- Sales invoices include:
  - Product details
  - Quantity sold
  - 10% tax (default)
  - Total amount
- Sales invoices are saved as text files: `invoices/sales_[saleID].txt`

### 5. Purchase Management
- Add, update, and delete purchase entries.
- Automatically generate purchase invoices (`P-XXXXXXXX`).
- Purchase invoices include:
  - Supplier details
  - Product details
  - Quantity purchased
  - 10% tax (default)
  - Total amount
- Purchase invoices are saved as text files: `invoices/purchase_[purchaseID].txt`

### 6. Reports
- Generate visual reports using Matplotlib and NumPy.
- Available reports:
  - Sales Trend over Time (Line Chart)
  - Purchases Trend over Time (Line Chart)
  - Sales vs. Purchases per Product (Grouped Bar Chart)
  - Total Purchases per Supplier (Pie Chart)
  - Sales vs. Stock Levels (Scatter Plot)

### 7. User Roles & Permissions
- Role-based access control (Admin, Manager, Sales Staff, Inventory Staff)
- Menus adjust dynamically based on user roles.

## 🏗️ Project Structure
```
.
├── data.py                  # Stores all data (products, categories, sales, purchases, suppliers)
├── main.py                  # Main entry point and menu handling
├── categories.py            # Category CRUD operations
├── products.py              # Product CRUD operations
├── suppliers.py             # Supplier CRUD operations
├── sales.py                 # Sales CRUD operations
├── purchases.py             # Purchase CRUD operations
├── invoices.py              # Invoice generation (sales & purchases)
├── reports.py               # Report generation using Matplotlib
├── exceptions.py            # Data validation methods
├── invoices/                # Directory to store all invoices
├── README.md                # Project documentation
```

## 🔧 Setup Instructions
1. **Clone the repository:**
```bash
git clone <repository-url>
cd inventory-management-system
```
2. **Create a virtual environment (optional):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Run the program:**
```bash
python main.py
```

## 📈 Usage
1. **Login:**
   - Choose your role (Admin, Manager, Sales Staff, Inventory Staff).
   - Access the corresponding menu based on your role.

2. **Perform CRUD operations:**
   - Navigate through the menu to add/update/delete products, categories, sales, purchases, and suppliers.

3. **Invoices:**
   - Sales and purchase invoices are auto-generated and stored in the `invoices/` folder.

4. **Reports:**
   - Select the "Reports" option to view visual data representations.

## 🧪 Testing
- Ensure your data is correctly populated in `data.py`.
- Test adding and deleting sales/purchases and check the corresponding invoice files.
- Run the reports to confirm the visualizations are accurate.

## 📚 Technologies Used
- **Python**: Core programming language.
- **Matplotlib**: For report visualizations.
- **NumPy**: For numerical operations.

## 📄 License
This project is licensed under the MIT License.

---

*Thank you for using Stockify — Your Smart Inventory Partner!* ✨
