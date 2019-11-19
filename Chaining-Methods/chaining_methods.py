class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self): 
        print("User: {}, Balance: {}".format(self.name, self.account_balance))
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

if __name__ == "__main__":
    diana = User("Diana", "diana.d.chen@gmail.com")
    michael = User("Michael", "michael@codingdojo.com")
    devon = User("Devon", "devon@codingdojo.com")

    diana.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(150).display_user_balance()

    michael.make_deposit(200).make_deposit(100).make_withdrawal(50).make_withdrawal(25).display_user_balance()

    devon.make_deposit(300).make_withdrawal(100).make_withdrawal(50).make_withdrawal(25).display_user_balance()

    diana.transfer_money(michael, 20).display_user_balance()
    michael.display_user_balance()


