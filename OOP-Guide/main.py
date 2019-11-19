class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.acount_balance += amount

michael.make_deposit(100)
michael.make_deposit(200)
anna.make_deposit(50)
print(michael.account_balance)
print(anna.account_balance)

michael = User("Michael", "michael@codingdojo.com")
anna = User("Anna", "anna@codingdojo.com")
print(anna.name)
print(michael.name)
