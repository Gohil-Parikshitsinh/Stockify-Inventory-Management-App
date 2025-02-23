# data.py

# categories = {}  # Stores categories as {category_id: name}
# products = {}    # Stores products as {product_id: {'name': name, 'category_id': category_id}}
# purchases = {}  # Stores purchases as {purchase_id: {'product_id': ..., 'quantity': ..., 'price': ..., 'date': ...}}


# Sample Categories (category_id: name)
categories = {
    "C0000001": "Electronics",
    "C0000002": "Clothing",
    "C0000003": "Groceries",
    "C0000004": "Furniture"
}

# Sample Products (product_id: {'name': name, 'category_id': category_id, 'price': price, 'stock': stock})
products = {
    "P0000001": {"name": "Laptop", "category_id": "C0000001", "price": 1000, "stock": 10},
    "P0000002": {"name": "Smartphone", "category_id": "C0000001", "price": 800, "stock": 15},
    "P0000003": {"name": "T-shirt", "category_id": "C0000002", "price": 20, "stock": 50},
    "P0000004": {"name": "Dining Table", "category_id": "C0000004", "price": 300, "stock": 5},
    "P0000005": {"name": "Apple", "category_id": "C0000003", "price": 1, "stock": 100}
}


# Sample Purchases (purchase_id: {'product_id': product_id, 'quantity': quantity, 'supplier': supplier_id, 'date': date})
purchases = {
    "PR000001": {"product_id": "P0000001", "quantity": 10, "supplier": "S0000001", "date": "2025-02-23"},
    "PR000002": {"product_id": "P0000003", "quantity": 25, "supplier": "S0000002", "date": "2025-02-22"},
    "PR000003": {"product_id": "P0000005", "quantity": 50, "supplier": "S0000003", "date": "2025-02-20"},
    "PR000004": {"product_id": "P0000002", "quantity": 15, "supplier": "S0000001", "date": "2025-02-21"},
    "PR000005": {"product_id": "P0000004", "quantity": 8, "supplier": "S0000004", "date": "2025-02-19"}
}

# Sample Sales (sale_id: {'product_id': product_id, 'quantity': quantity, 'customer': customer, 'date': date})
sales = {
    "S0000001": {"product_id": "P0000001", "quantity": 2, "customer": "John Doe", "date": "2025-02-23"},
    "S0000002": {"product_id": "P0000003", "quantity": 5, "customer": "Jane Smith", "date": "2025-02-22"},
    "S0000003": {"product_id": "P0000002", "quantity": 1, "customer": "Alice Johnson", "date": "2025-02-21"},
    "S0000004": {"product_id": "P0000004", "quantity": 3, "customer": "Michael Brown", "date": "2025-02-20"},
    "S0000005": {"product_id": "P0000005", "quantity": 10, "customer": "Emily Davis", "date": "2025-02-19"}
}

# Sample Suppliers (supplier_id: {'name': name, 'products_supplied': [product_ids]})
suppliers = {
    "S0000001": {"name": "TechWorld", "products_supplied": ["P0000001", "P0000002"]},
    "S0000002": {"name": "FashionHub", "products_supplied": ["P0000003"]},
    "S0000003": {"name": "FreshFoods", "products_supplied": ["P0000005"]},
    "S0000004": {"name": "FurniCraft", "products_supplied": ["P0000004"]},
    "S0000005": {"name": "GadgetZone", "products_supplied": ["P0000001", "P0000002", "P0000005"]}
}
