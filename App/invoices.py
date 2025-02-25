import os
from datetime import datetime
from data import products, purchases, suppliers, sales

# Directory to store invoices
INVOICE_DIR_SALES = "invoices/sales"
os.makedirs(INVOICE_DIR_SALES, exist_ok=True)
INVOICE_DIR_PURCHASE = "invoices/purchase"
os.makedirs(INVOICE_DIR_PURCHASE, exist_ok=True)


# ---------------------- Sales Invoices ----------------------

def generate_sale_invoice(sale_id, product_id, quantity, customer, date):
    if product_id not in products:
        print(f"Product ID '{product_id}' does not exist.")
        return

    product = products[product_id]
    product_name = product['name']
    unit_price = product['price']
    subtotal = quantity * unit_price
    tax = subtotal * 0.10
    total_amount = subtotal + tax

    invoice_file = os.path.join(INVOICE_DIR_SALES, f"sales_{sale_id}.txt")
    file = open(invoice_file, 'w')
    file.write("=" * 41 + "\n")
    file.write(" " * 18 + "SALE INVOICE\n")
    file.write("=" * 41 + "\n\n")
    file.write("Company Name: Stockify\n")
    file.write("Address: Ahmedabad\n")
    file.write("Contact: +98 9876543210 | sales@stockify.com\n\n")
    file.write("-" * 41 + "\n")
    file.write(f"Invoice No: INV-{sale_id}\n")
    file.write(f"Date: {date}\n\n")
    file.write(f"Customer Name: {customer}\n")
    file.write("-" * 41 + "\n\n")
    file.write(f"{'Product ID':<12}{'Product Name':<20}{'Qty':<6}{'Unit Price':<12}{'Total Price':<12}\n")
    file.write("-" * 63 + "\n")
    file.write(f"{product_id:<12}{product_name:<20}{quantity:<6}${unit_price:<12.2f}${subtotal:<12.2f}\n")
    file.write("-" * 63 + "\n")
    file.write(f"{'Subtotal:':<40}${subtotal:.2f}\n")
    file.write(f"{'Tax (10%):':<40}${tax:.2f}\n")
    file.write("-" * 63 + "\n")
    file.write(f"{'Total Amount:':<40}${total_amount:.2f}\n\n")
    file.write("=" * 41 + "\n")
    file.close()

    print(f"Sale invoice generated: {invoice_file}")


def update_sale_invoice(sale_id):
    if sale_id not in sales:
        print(f"Sale ID '{sale_id}' does not exist.")
        return

    sale = sales[sale_id]
    generate_sale_invoice(sale_id, sale['product_id'], sale['quantity'], sale['customer'], sale['date'])


def delete_sale_invoice(sale_id):
    file_path = os.path.join(INVOICE_DIR_SALES, f"sales_{sale_id}.txt")
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Sale invoice deleted: {file_path}")
    else:
        print(f"Invoice for Sale ID '{sale_id}' not found.")


# ---------------------- Purchase Invoices ----------------------

def generate_purchase_invoice(purchase_id, supplier_id, product_id, quantity):
    if supplier_id not in suppliers:
        print(f"Supplier ID '{supplier_id}' does not exist.")
        return

    if product_id not in products:
        print(f"Product ID '{product_id}' does not exist.")
        return

    supplier = suppliers[supplier_id]
    supplier_name = supplier['name']
    product = products[product_id]
    product_name = product['name']
    unit_price = product['price']

    subtotal = quantity * unit_price
    tax = subtotal * 0.10
    total_amount = subtotal + tax

    invoice_file = os.path.join(INVOICE_DIR_PURCHASE, f"purchase_{purchase_id}.txt")
    file = open(invoice_file, 'w')
    file.write("=" * 41 + "\n")
    file.write(" " * 16 + "PURCHASE INVOICE\n")
    file.write("=" * 41 + "\n\n")
    file.write("Company Name: Stockify\n")
    file.write("Address: Prahlad Nagar, Ahmedabad\n")
    file.write("Contact: +91 987654321 | purchase@stockify.com\n\n")
    file.write("-" * 41 + "\n")
    file.write(f"Invoice No: PINV-{purchase_id}\n")
    file.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}\n\n")
    file.write(f"Supplier Name: {supplier_name}\n")
    file.write(f"Supplier ID: {supplier_id}\n")
    file.write("-" * 41 + "\n\n")
    file.write(f"{'Product ID':<12}{'Product Name':<20}{'Qty':<6}{'Unit Price':<12}{'Total Price':<12}\n")
    file.write("-" * 63 + "\n")
    file.write(f"{product_id:<12}{product_name:<20}{quantity:<6}${unit_price:<12.2f}${subtotal:<12.2f}\n")
    file.write("-" * 63 + "\n")
    file.write(f"{'Subtotal:':<40}${subtotal:.2f}\n")
    file.write(f"{'Tax (10%):':<40}${tax:.2f}\n")
    file.write("-" * 63 + "\n")
    file.write(f"{'Total Amount:':<40}${total_amount:.2f}\n\n")
    file.write("=" * 41 + "\n")
    file.close()

    print(f"Purchase invoice generated: {invoice_file}")


def update_purchase_invoice(purchase_id):
    if purchase_id not in purchases:
        print(f"Purchase ID '{purchase_id}' does not exist.")
        return

    purchase = purchases[purchase_id]
    generate_purchase_invoice(purchase_id, purchase['supplier_id'], purchase['product_id'], purchase['quantity'])


def delete_purchase_invoice(purchase_id):
    file_path = os.path.join(INVOICE_DIR_PURCHASE, f"purchase_{purchase_id}.txt")
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Purchase invoice deleted: {file_path}")
    else:
        print(f"Invoice for Purchase ID '{purchase_id}' not found.")

