import json
from classes.account import Account

def read_accounts(transaction):
    try:
        with open("database/account.json","r") as file:
            data = json.load(file)
            accounts = []
            for account_details in data:
                acc = Account(
                    account_details["acc_num"],
                    account_details["acc_name"],
                    account_details["acc_pass"]
                )
                for trans_id in account_details["acc_trans"]:
                    for trans in transaction:
                        if trans_id == trans.transaction_id:
                            acc.acc_trans.append(trans)
                            break
                acc.set_balance(account_details["acc_bal"])
                accounts.append(acc)
            return accounts
    except (FileNotFoundError,json.JSONDecodeError):
        return []

def write_accounts(accounts):
    data = []
    for acc in accounts:
        data.append({
            "acc_num":acc.acc_num,
            "acc_name":acc.acc_name,
            "acc_pass":acc.acc_pass,
            "acc_trans":[trans.transaction_id for trans in acc.acc_trans],
            "acc_bal":acc.get_balance()
        })
    with open("database/account.json","w") as file:
        json.dump(data,file,indent=4)