from classes.inventory import Inventory
from classes.product import Product
from file_op.product_op import write_products,read_products
from file_op.sales_op import write_sale,read_sales
import questionary
inventory = Inventory()
inventory.products =  read_products()
inventory.sales = read_sales()



def add_product():
    while True:
        name = questionary.text(
            "Enter product name (q to quit):"
        ).ask()
        if name is None or name.strip().lower() == "q":
            print("Operation cancelled.")
            return
        name = name.strip()
        if not name:
            print("Product name cannot be empty.")
            continue
        if any(
            product.name.strip().lower() == name.lower()
            for product in inventory.products
        ):
            print("Duplicate product name.")
            continue
        while True:
            price = questionary.text(
                "Enter product price (q to quit):"
            ).ask()
            if price is None or price.strip().lower() == "q":
                print("Operation cancelled.")
                return
            try:
                price = float(price)
                if price <= 0:
                    print("Price must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid price. Enter a number.")
        while True:
            quantity = questionary.text(
                "Enter product quantity (q to quit):"
            ).ask()
            if quantity is None or quantity.strip().lower() == "q":
                print("Operation cancelled.")
                return
            try:
                quantity = int(quantity)
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid quantity. Enter a whole number.")
        while True:
            category = questionary.text(
                "Enter product category (q to quit):"
            ).ask()
            if category is None or category.strip().lower() == "q":
                print("Operation cancelled.")
                return
            category = category.strip()
            if not category:
                print("Category cannot be empty.")
                continue
            break
        product_id = max(
            (product.id for product in inventory.products),
            default=0
        ) + 1
        product = Product(
            product_id,
            name,
            price,
            quantity,
            category
        )
        status, message = inventory.add_product(product)
        print(message)
        if status:
            write_products(inventory.products)
        break