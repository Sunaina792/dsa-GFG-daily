## object oriented programming
#Encapsulation
class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number  # Public attribute
        self.account_holder = account_holder  # Public attribute
        self.__balance = initial_balance      # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance  # Controlled access to the balance

# Example Usage
account = BankAccount("1234567890", "sunaina", 1000)
print(f"Account Holder: {account.account_holder}") # Accessing public attribute
account.deposit(500)
account.withdraw(200)
print(f"Current Balance: {account.get_balance()}") # Accessing balance through a method
# print(account.__balance) # This will raise an AttributeError because __balance is "private"
print(account._BankAccount__balance) 

#Inheritance
class Vehicle:  # Base class
    def __init__(self, make, model, color):
        self.make = make  # Public attribute
        self.model = model  # Public attribute
        self.color = color  # Public attribute

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

class Car(Vehicle):  # Derived class inheriting from Vehicle
    def __init__(self, make, model, color, num_doors):
        super().__init__(make, model, color)  # Call the superclass's constructor
        self.num_doors = num_doors

    def drive(self):
        print("Driving the car.")


# Example Usage
my_car = Car("Toyota", "Camry", "Silver", 4)
print(f"My car is a {my_car.color} {my_car.make} {my_car.model} with {my_car.num_doors} doors.")
my_car.start_engine()
my_car.drive()
my_car.stop_engine()
 
 # Polymorphism
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):  # Method overriding
        print("Woof!")

class Cat(Animal):
    def speak(self):  # Method overriding
        print("Meow!")

# Example Usage
animal1 = Animal("Generic Animal")
animal2 = Dog("Buddy")
animal3 = Cat("Whiskers")

animal1.speak()
animal2.speak()
animal3.speak()

# Duck Typing Example
class Book:
    def read(self):
        print("Reading a book")

class Screen:
    def read(self):
        print("Reading from a screen")

def read_item(item):
    item.read() # Doesn't care about the type, only that it has a read() method

my_book = Book()
my_screen = Screen()

read_item(my_book)
read_item(my_screen)