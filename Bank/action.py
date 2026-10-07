from classes.account import Account
from classes.bank import Bank
from fileop.acc_op import write_accounts,read_accounts
from fileop.tarns_op import write_transactions,read_transactions
import questionary
import random
bank = Bank()
bank.transactions = read_transactions()
bank.accounts = read_accounts(bank.transactions)

def account_number_generator():
    while True:
        account_number = random.randint(100000, 999999)
        if not any(acc.acc_num == account_number for acc in bank.accounts):
            return account_number

# check auth
def auth():
    while True:
        choice = questionary.select(
            "Select an option:",
            choices=[
                "Login",
                "SignUp",
                "Exit"
            ]
        ).ask()
        if choice is None:
            print("Goodbye!")
            exit()
        if choice == "Login":
            prompt = questionary.text(
                "Enter your account number (or q to quit):"
            ).ask()
            if prompt is None:
                print("Goodbye!")
                exit()
            if prompt.lower() == "q":
                continue
            try:
                prompt = int(prompt)
            except ValueError:
                print("Enter a valid account number")
                continue
            status, account_object = bank.fetch_account(prompt)
            if status:
                while True:
                    password = questionary.password("Enter your password").ask()
                    if password is None:
                        print("Goodbye!")
                        exit()
                    if not password:
                        print("Enter your password")
                        continue
                    if password:
                        break
                if password.lower() == 'q':
                    continue     
                status ,res = bank.account_auth(account_object,password)
                if status:
                    print(res)
                    return True, account_object
                else:
                    print(res)
            else:
                print(res)
        elif choice == "SignUp":
            while True:
                name = questionary.text("Enter your name (or q to quit):").ask()
                name = name.lower().strip()
                if name is None:
                    print("Goodbye!")
                    exit()
                if name.lower() == "q":
                    break
                if not name or not all(part.isalpha() for part in name.split()):
                    print("Enter a valid name")
                    continue
                if name :
                    break
            if name.lower() == "q":
                continue
            while True:
                password = questionary.password("Enter your password (or q to quit:)").ask()
                if password is None:
                    print("goodbye!")
                    exit()
                if password.lower() == "q":
                    break
                if not password or len(password) <= 3:
                    print("Enter a valid password")
                    continue
                if password:
                    break
            if password.lower() == "q":
                continue
            account_number = account_number_generator()
            user = Account(account_number,name,password)
            status,res = bank.create_account(user)
            if status:
                write_accounts(bank.accounts)
                print(res)
                return True,user
            else:
                print(res)

        elif choice == "Exit":
            print("Goodbye!")
            return False,"Auth Failed"
def bank_menu(details):
    while True:
        choice = questionary.select("Select an option", choices=["Deposit","Withdraw","Transfer","History","Exit"]).ask()
        if choice == "Exit":
            exit()
        elif choice == "Deposit":
            deposit(details)
        else:
            break

        break

def deposit(account):
    description = questionary.text(
        "Enter deposit description:"
    ).ask()
    if description is None:
        return
    while True:
        amount = questionary.text(
            "Enter amount:"
        ).ask()
        if amount is None:
            return
        try:
            amount = float(amount)
        except ValueError:
            print("Amount must be a number")
            continue
        break
    password = questionary.password(
        "Enter your password:"
    ).ask()
    if password is None:
        return
    status, message = bank.deposit_account(
        account,
        description,
        amount,
        password
    )
    print(message)
    if status:
        write_accounts(bank.accounts)
        write_transactions(bank.transactions)