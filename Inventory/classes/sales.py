from datetime import datetime
class Sales:
    def __init__(self,ref,id,name,amount,quantity,date=None):
        self.ref = ref
        self.id = id
        self.name = name
        self.amount = amount
        self.quantity = quantity
        self.date = date if date else datetime.now()
