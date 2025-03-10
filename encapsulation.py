class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if value < 0:
            print("Balance can't be negative")
        else:
            self.__balance += value

    def __display_pin(self):
        print("Pin: 1234")
    @property
    def get_pin(self):
        self.__display_pin()

account = BankAccount(1000)
print(account._BankAccount__balance)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
# account.get_pin()
account.get_pin

