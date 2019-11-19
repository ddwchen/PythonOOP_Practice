class BankAccount:
    def __init__ (self, init_balance=0):
        self.int_rate = .03
        self.balance = init_balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Balance: {}".format(self.balance))
        return self

    def yield_interest(self):
        self.balance = (1+self.int_rate) * self.balance
        return self

    
if __name__ == "__main__":
    diana = BankAccount (100)
    michael = BankAccount (50)


    diana.deposit(200).deposit(50).deposit(33).withdraw(100).yield_interest().display_account_info()
    michael.deposit(50).deposit(500).withdraw(33).withdraw(77).withdraw(10).withdraw(25).yield_interest().display_account_info()
