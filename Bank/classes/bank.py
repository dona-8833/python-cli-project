from classes.tansaction import Transaction
class Bank:
    def __init__(self):
        self.accounts = []
        self.transactions = []
    def fetch_account(self,account_number):
        for account in self.accounts:
            if account_number == account.acc_num:
                return True , account
        return False , "Account not found"
    def check_account(self,account):
        if account in self.accounts:
            return True,"Account in bank"
        return False,"Account not registered"
    def account_auth(self,account,password):
        if account in self.accounts and password == account.acc_pass:
            return True ,f"welcome {account.acc_name}"
        return False,"Wrong password"
    def create_account(self,account):
        if account in self.accounts:
            return False,"Account already registered"
        self.accounts.append(account)
        return True , "Account created successfully"
    def deposit_account(self,account,decription,amount,password):
        trans_id = max((trans.transaction_id for trans in self.transactions),default=0) + 1
        trans_type = "deposit"
        trans_amount = amount
        trans_descri = decription
        trans = Transaction(trans_id,trans_type,trans_amount,trans_descri)
        status,res = account.deposit(password,amount,trans)
        if status:
            self.transactions.append(trans)
            return True,"Deposit successful"
        return res

    