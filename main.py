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
        print('depositing money!')
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('You dont have enough funds! Please add some money')
        else:    
            self.balance = self.balance - amount



my_checking = BankAccount('checking')
my_savings = BankAccount('savings')

my_checking.deposit(200)

#########################################################

# Exercise
# Create a Phone class and give 2 methods
# - make_call
# - send_text

class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def make_call(self, recipient):
        print(f'Calling {recipient} from {self.phone_number}!')

    def send_text(self, recipient):
        print(f'Sending text to {recipient}!')

my_phone = Phone('555-5555')
my_friends_phone = Phone('333-3333')

friends_number = my_friends_phone.phone_number
my_phone_number = my_phone.phone_number

my_phone.make_call(friends_number)
my_friends_phone.make_call(my_phone_number)

##########################################################
