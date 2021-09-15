my_dictionary = {
    "some_key": "some value"
}

my_dictionary['some_key']

class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hi my name is {self.name}')

me = User('Michael')
bob = User('Bob')
sally = User('Sally')

me.greet()
print(me)
print(me.name)

####################################################
# Exercise
# Create a BankAccount class that takes in a type
class BankAccount:
    def __init__(self, type):
        self.type = type
        self.balance = 0

    def deposit(self, amount):
        print('depositting money!')
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('You dont have enough funds! Please add some money')
        else:    
            self.balance = self.balance - amount



my_checking = BankAccount('checking')
my_savings = BankAccount('savings')

my_checking.deposit(200)