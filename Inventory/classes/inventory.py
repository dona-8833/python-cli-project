class Inventory:

    def __init__(self):
        self.products = []
        self.sales = []

    def add_product(self, product):
        if any(p.name.lower() == product.name.lower() for p in self.products):
            return False, "duplicate product"
        self.products.append(product)
        return True, "successfully added"
        
    def remove_product(self, product):
        ...

    def update_product(self, product):
        ...

    def search_product(self):
        ...

    def sell_product(self):
        ...

    def restock_product(self):
        ...

    def view_inventory(self):
        ...

    def inventory_value(self):
        ...

    def low_stock(self):
        ...