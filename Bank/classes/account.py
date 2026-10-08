class Account:
    def __init__(self,acc_num,acc_name,acc_pass):
        self.acc_num = acc_num
        self.acc_name = acc_name
        self.acc_pass = acc_pass
        self.acc_trans = []
        self.__bal = 0.00
    def get_balance(self):
        return self.__bal

    def set_balance(self, balance):
        self.__bal = balance

    def deposit(self, password, amount,transaction):
        if self.acc_pass != password:
            return False, "Wrong password"
        if amount <= 0:
            return False, "Amount must be greater than 0"
        self.__bal += amount
        self.acc_trans.append(transaction)
        return True, "Deposit successful"

    def withdraw(self, password, amount,transaction):
        if self.acc_pass != password:
            return False, "Wrong password"
        if amount <= 0:
            return False, "Amount must be greater than 0"
        if amount > self.__bal:
            return False, "insufficient balance"
        self.__bal -= amount
        self.acc_trans.append(transaction)
        return True, "Withdraw successful"
    def transfer(self,password,amount,transaction):
        if self.acc_pass != password:
            return False, "Wrong password"
        if amount <= 0:
            return False, "Amount must be greater than 0"
        if amount > self.__bal:
            return False, "insufficient balance"
        self.__bal -= amount
        self.acc_trans.append(transaction)
        return True, "Transfer successful"
    def set_credit(self,amount):
        self.__bal+=amount