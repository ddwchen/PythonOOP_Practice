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



class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def deposit(self, amount):
        self.account.deposit(amount)
        return self

    def withdraw(self, amount):
        if self.account.withdraw(amount):
            self.account.withdraw(amount)
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.account.withdraw(5)
        return self

    def display_user_balance(self):
        print("Balance: {}".format(self.account.balance))
        return self



    
if __name__ == "__main__":
    diana = User ("Diana", "diana.d.chen@gmail.com")
    michael = User ("Michael", "michael@codingdojo.com")


    diana.deposit(200).deposit(50).deposit(33).withdraw(100).display_user_balance()
    michael.deposit(50).deposit(500).withdraw(33).withdraw(77).withdraw(10).withdraw(25).display_user_balance()
