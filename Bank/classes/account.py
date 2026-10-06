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