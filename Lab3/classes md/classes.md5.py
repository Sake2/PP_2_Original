class Bank_Account():
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self,dep):
        self.balance  += dep
    def withdraw(self,money) :
        if money <= self.balance :
            self.balance -= money

first_acc = Bank_Account("Baurjan Momichulu",0)
print(first_acc.balance)
first_acc.deposit(123)
print(first_acc.balance)
first_acc.withdraw(21)
print(first_acc.balance)
first_acc.withdraw(1234)
print(first_acc.balance)