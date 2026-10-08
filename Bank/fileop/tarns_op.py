from classes.tansaction import Transaction
import json
from datetime import datetime

def read_transactions():
    try:
        with open("database/transaction.json","r") as file:
            data = json.load(file)
            transactions = []
            for transaction_details in data:
                trans = Transaction(
                    transaction_details["transaction_id"],
                    transaction_details["transaction_type"],
                    transaction_details["amount"],
                    transaction_details["description"],
                    datetime.strptime(transaction_details["date"],"%d-%m-%Y %H:%M:%S")
                )
                transactions.append(trans)
            return transactions
    except (FileNotFoundError,json.JSONDecodeError):
        return []

def write_transactions(transactiolns):
    data = []
    for trans in transactiolns:
        data.append({
            "transaction_id":trans.transaction_id,
            "transaction_type":trans.transaction_type,
            "amount":trans.amount,
            "description":trans.description,
            "date":trans.date.strftime("%d-%m-%Y %H:%M:%S")
        })
    with open("database/transaction.json","w") as file:
        json.dump(data,file,indent=4)