
# class BankAccount():
#     def __init__(self, type, balance = 0, overdraft_fees = 0):
#         self.type = type
#         self.balance = balance
#         self.overdraft_fees = overdraft_fees

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance

#     def withdraw(self, amount):
#         # if our balance becomes negative, prevent withdrawing money
#         result = self.balance - amount
#         if ((result - self.overdraft_fees) < -100):
#             print("You cannot withdraw money, insufficient funds")
#             return 0

#         if (result > 0):
#             self.balance -= amount
#             return amount
#             # return self.balance
#         else:
#             self.overdraft_fees += 20
#             self.balance -= amount
#             return amount


#     def __str__(self):
#         return f"Your {self.type} account balance is: {self.balance}"

# my_savings = BankAccount('savings', 50)

# my_checking = BankAccount('checking')

# money = my_savings.withdraw(100)

# my_checking.deposit(money)

# print(my_checking)

# Practice Exercise
# Python Inheritance Lab - Banking System
class BankAccount():
    def _init_(self,balance):
        self.balance = balance
    def check_balance(self):
        return f"Your balance is: {self.balance}"
    def deposit(self, amount):
        if (amount < 0):
          return False
        else:
           self.balance += amount
           return