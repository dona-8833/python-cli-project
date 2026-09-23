inventory = [
    {
        "name": "Laptop",
        "category": "Electronics",
        "price": 1200,
        "quantity": 10,
        "SKU": "LAP-001"
    },
    {
        "name": "Wireless Mouse",
        "category": "Accessories",
        "price": 25,
        "quantity": 0,
        "SKU": "MOU-002"
    },
    {
        "name": "Keyboard",
        "category": "Accessories",
        "price": 45,
        "quantity": 30,
        "SKU": "KEY-003"
    },
    {
        "name": "Monitor",
        "category": "Electronics",
        "price": 300,
        "quantity": 15,
        "SKU": "MON-004"
    },
    {
        "name": "USB-C Cable",
        "category": "Accessories",
        "price": 15,
        "quantity": 0,
        "SKU": "USB-005"
    }
]

def get_categories(inventory):
    category = {p["category"] for p in inventory }
    return category
def get_product_names(inventory):
    products_name = [p["name"] for p in inventory]
    return products_name
def get_out_of_stock_products(inventory):
    out_of_stock_products = [p for p in inventory if p["quantity"] == 0]
    return out_of_stock_products
def get_low_stock_products(inventory):
    low_stock_products = [p for p in inventory if p["quantity"] > 0 and p["quantity"] <= 10]
    return low_stock_products
def calculate_inventory_value(inventory):
    inventory_value = 0
    for i in inventory:
        inventory_value += i["price"] * i["quantity"]
    return inventory_value
def find_product_by_sku(inventory, sku):
    clean_sku = sku.strip().upper()
    for product in inventory:
        if product["SKU"] == clean_sku:
            return product
    return None

def generate_inventory_report(inventory):
    total_inventory_value = calculate_inventory_value(inventory)
    out_of_stock = get_out_of_stock_products(inventory)
    low_stock = get_low_stock_products(inventory)
    categories = get_categories(inventory)

    return f'''
    Total inventory value: {total_inventory_value}
    Out of stock: {len(out_of_stock)}
    Low stock: {len(low_stock)}
    Categories: {categories}
'''
generate_inventory_report(inventory)