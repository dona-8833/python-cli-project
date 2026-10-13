import json
from datetime import datetime
from classes.sales import Sales


def write_sale(sales):
    data = []
    for sale in sales:
        data.append({
            "ref":sale.ref,
            "id":sale.id,
            "name":sale.name,
            "amount":sale.amount,
            "quantity":sale.quantity,
            "date": sale.date.strftime("%d-%m-%Y %H:%M:%S")
        })
    with open("database/sales.json","w") as file:
        json.dump(data,file,indent=4)

def read_sales():
    try:
        with open("database/sales.json","r") as file:
            data = json.load(file)
            sales = []
            for sales_detail in data:
                sale = Sales(
                    sales_detail["ref"],
                    sales_detail["id"],
                    sales_detail["name"],
                    sales_detail["amount"],
                    sales_detail["quantity"],
                    datetime.strptime(sales_detail["date"],"%d-%m-%Y %H:%M:%S")
                )
                sales.append(sale)
            return sales
    except (FileNotFoundError,json.JSONDecodeError):
        print("file not found")
        return []