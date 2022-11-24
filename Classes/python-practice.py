# class Dog():
#     def _init_(self, name, age = 0):
#         self.name = name
#         self.age = age
#         self.id = Dog.next_id
#         Dog.next_id +=1

#     def bark(self):
#         print(f"{self.name} says woof!")
#     def _str_(self):
#         return f"Dog name {self.name} is {self.age} years old"
# @classmethod
# def get_total_dogs(cls):
#     return cls.next_id -1

# spot = Dog('spot', 8)

# fluffy = Dog('fluffy', 4)
# fluffy2 = Dog('fluffy', 4)
# fluffy3 = Dog('fluffy', 4)
# print(Dog.get_total_dogs())
# spot.bark()
# print(spot)
# Pass in superclass as argument
# class ShowDog(Dog):
#   # Add additional parameters AFTER those in the superclass
#   def __init__(self, name, age = 0, total_earnings = 0):
#     # Always call the superclass's __init__ first
#      Dog.__init__(self, name, age)
#     # Now add any new attributes
#      self.total_earnings = total_earnings
  
#   # Add additional methods
#   def add_prize_money(self, amount):
#     self.total_earnings += amount
# winky = ShowDog('Winky', 3, 1000)
# print(winky) # Yay, inherited the overriden __str__
# winky.bark() # Yay, inherited the bark method
# print(winky.total_earnings) # -> 1000
# winky.add_prize_money(500) # New method that 'Dogs' don't have
# print(winky.total_earnings) # -> 1500


# checking = BankAccount('checking')
# savings = BankAccount('savings')

# print(savings.deposit(1000))

# transfer = savings.withdraw(1200)
# print(transfer)

# print(checking.deposit(transfer))

# print("checking.balance", checking.balance)
# print("savings.balance", savings.balance)

# print("checking.overdraft_fees", checking.overdraft_fees)
# print("savings.overdraft_fees", savings.overdraft_fees)

#Excersices
# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
# class Bank_Account:
#     def __init__(self):
#         self.balance=0
#         print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
#     def deposit(self):
#         amount=float(input("Enter amount to be Deposited: "))
#         self.balance += amount
#         print("\n Amount Deposited:",amount)
 
#     def withdraw(self):
#         amount = float(input("Enter amount to be Withdrawn: "))
#         if self.balance>=amount:
#             self.balance-=amount
#             print("\n You Withdrew:", amount)
#         else:
#             print("\n Insufficient balance  ")
 
#     def display(self):
#         print("\n Net Available Balance=",self.balance)
 
# # Driver code
  
# # creating an object of class
# s = Bank_Account()
  
# # Calling functions with that class object
# s.deposit()
# s.withdraw()
# s.display()


class BankAccount():
    def __init__(self):
        self.balance = 4800

    def check_balance(self):
        print(f'your balance is {self.balance}')
            
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
        print(f'your balance is {self.balance}')

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
            print(f'your balance is {self.balance}')
        else:
            print("\n Insufficient balance  ")
            

    # def overdraft_fees(self):
    #     if self.balance == 0:
    #         overdraft_fees=20
    #         # for balance y
    #         self.balance=self.balance + 20
    #         print(f'your balance is with overdraft {self.balance}')

    def accumulate_interest(self):
        self.interest = 0.02
        self.balance = self.balance + (self.interest*self.balance)

    def display(self):
        print("\n Net Available Balance with interest=",self.balance)

s = BankAccount()
s.check_balance()
s.deposit()
s.withdraw()
s.accumulate_interest()
s.overdraft_fees()
s.display()



   
    