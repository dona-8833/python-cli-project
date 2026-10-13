import json
from classes.product import Product


def write_products(products):
    data = []
    for product in products:
        data.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity,
            "category": product.category
        })
    with open("database/products.json", "w") as file:
        json.dump(data, file, indent=4)


def read_products():
    try:
        with open("database/products.json", "r") as file:
            data = json.load(file)
            products = []
            for product_detail in data:
                product = Product(
                    product_detail["id"],
                    product_detail["name"],
                    product_detail["price"],
                    product_detail["quantity"],
                    product_detail["category"]
                )
                products.append(product)
            return products
    except (FileNotFoundError, json.JSONDecodeError):
        print("Products file not found or contains invalid JSON.")
        return []