from dataclasses import dataclass

class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self._balance = balance
    def deposit(self,amount):
        self._balance += amount
    @property
    def balance(self):
        return self._balance 

account1 = BankAccount("Alice")
account1.deposit(1000)
print(account1.balance)

class Alert:
    def __init__(self,message):
        self.message = message
    def trigger(self):
        return f"System Alert: {self.message}"
class EmailAlert(Alert):
    def __init__(self,message,email_address):
        super().__init__(message)
        self.email_address=email_address
    def trigger(self):
        system_alert = super().trigger()
        return f"Sending email to {self.email_address}: {self.message} {system_alert} "
    def __str__(self):
        return f"EmailAlert: {self.message}"
    def __repr__(self):
        return f"EmailAlert(message='{self.message}', email_address='{self.email_address}')"
mails = EmailAlert("Server Down","devops@example.com")
print(mails.trigger())
print(mails)

class InventoryItem:
    def __init__(self,sku,price):
        self.sku = sku
        self.price = price
    def __eq__(self,other):
        if isinstance(other,InventoryItem):
            return other.price == self.price and other.sku == self.sku
        return False

item1 = InventoryItem("XYZ-123",50.00)
item2 = InventoryItem("XYZ-123",50.00)

print(item1 == item2)

class LogEntry:
    def __init__(self,level,message):
        self.level = level
        self.message = message
    @classmethod
    def from_csv_line(cls,line):
        level,message = line.split(",")
        return cls(level,message)

logs = LogEntry.from_csv_line("WARN,High memory usage")
print(logs.message,logs.level)

class PDFExporter:
    def __init__(self,filename):
        self.filename = filename
    def export(self,data):
        return f"Writing {data} to PDF: {self.filename}"
class CSVExporter:
    def __init__(self,filename):
        self.filename =filename
    def export(self,data):
        return f"Writing {data} to CSV: {self.filename}"
def generate_reports(exporter_list, data):
    for exporter in exporter_list:
        exporter.export(data)


pdf = PDFExporter("financials.pdf")
csv = CSVExporter("financials.csv")

exporters = [pdf, csv]

print(generate_reports(exporters, "Q3 Financials"))

class Logger:
    def log_info(self,message):
        print(f"[INFO] {message}")


class ShoppingCart:
    def __init__(self,logger):
        self.logger = logger
        self.items = []
    def add_item(self, item_name):
        self.items.append(item_name)
        self.logger.log_info(item_name)

my_log = Logger()
my_cart = ShoppingCart(my_log)
my_cart.add_item("Laptop")
my_cart.add_item("Mouse")
print(my_cart.items)


@dataclass
class Product:
    id:int
    name:str
    price:float
class ShoppingCart:
    def __init__(self):
        self._items = {}
    def add_item(self, product, quantity=1):
        self.product = product
        if product.id in self._items:
            self._items[product.id]["qty"] += quantity
        else:
            self._items[product.id] = {
                        "product": product,
                            "qty": quantity}
    @property
    def total_price(self):
        total = 0
        for product in self._items.values():
            total += product["product"].price * product["qty"]
        return total
    def __str__(self):
        return f"Cart total: ${self.total_price}"
    def get_products(self):
        return [item["product"] for item in self._items.value()]





@dataclass
class Product:
    id: int
    name: str
    price: float


class ShoppingCart:
    def __init__(self):
        self.items = {}  # public

    def add_item(self, product, quantity=1):
        if product.id in self.items:
            self.items[product.id]["qty"] += quantity
        else:
            self.items[product.id] = {
                "product": product,
                "qty": quantity
            }

    @property
    def total_price(self):
        total = 0
        for item in self.items.values():
            total += item["product"].price * item["qty"]
        return total

    def __str__(self):
        return f"Cart total: ${self.total_price}"

    def get_products(self):
        return [item["product"] for item in self.items.values()]


laptop = Product(1, "Laptop", 1000.00)
mouse = Product(2, "Mouse", 50.00)

cart = ShoppingCart()

cart.add_item(laptop, 1)
cart.add_item(mouse, 2)

print(cart)
print(cart.items)



laptop = Product(1,"laptop", 1000.00)
mouse = Product(2,"mouse", 50.00)

cart = ShoppingCart()

cart.add_item(laptop, 1)
cart.add_item(mouse, 2)


