from datetime import datetime
class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, description,date=None):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.date = date if date else datetime.now()