# Module 09: Object-Oriented Programming
# solutions.py
# Розв'язки до вправ з exercises.py

print("=== Module 09 Solutions: Object-Oriented Programming ===")


# Task 1: Simple Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


def demo_task1():
    print("\nTask 1: Simple Person class (demo)")
    p1 = Person("Andrii", 20)
    p2 = Person("Maria", 19)
    p1.introduce()
    p2.introduce()


# Task 2: BankAccount class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return

        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive")
            return

        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance


def demo_task2():
    print("\nTask 2: BankAccount class (demo)")
    acc = BankAccount("Andrii", 100)
    acc.deposit(50)
    acc.withdraw(30)
    acc.withdraw(500)
    print("Final balance:", acc.get_balance())


# Task 3: Rectangle class with area and perimeter
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


def demo_task3():
    print("\nTask 3: Rectangle class with area and perimeter (demo)")
    r1 = Rectangle(3, 5)
    r2 = Rectangle(4, 4)
    print("r1 area:", r1.area(), "perimeter:", r1.perimeter(), "is_square:", r1.is_square())
    print("r2 area:", r2.area(), "perimeter:", r2.perimeter(), "is_square:", r2.is_square())


# Task 4: Encapsulation with getters/setters
class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password  # «приватне» поле (за домовленістю)

    def check_password(self, password):
        return password == self._password

    def set_password(self, old_password, new_password):
        if self.check_password(old_password):
            self._password = new_password
            print("Password changed successfully")
        else:
            print("Error: old password is incorrect")


def demo_task4():
    print("\nTask 4: Encapsulation with getters/setters (demo)")
    user = User("andrii", "1234")
    print("Check '0000':", user.check_password("0000"))
    print("Check '1234':", user.check_password("1234"))
    user.set_password("0000", "abcd")
    user.set_password("1234", "abcd")
    print("Check 'abcd':", user.check_password("abcd"))


# Task 5: Inheritance - Animal and Dog
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Woof!")


def demo_task5():
    print("\nTask 5: Inheritance - Animal and Dog (demo)")
    a = Animal("Some animal")
    d = Dog("Rex")
    a.speak()
    d.speak()


# Task 6: Inheritance - Vehicle and Car
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"{self.brand} {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year

    def info(self):
        print(f"{self.brand} {self.model} ({self.year})")


def demo_task6():
    print("\nTask 6: Inheritance - Vehicle and Car (demo)")
    car = Car("Tesla", "Model 3", 2024)
    car.info()


# Task 7 (optional): ShoppingCart class
class ShoppingCart:
    def __init__(self):
        # name -> {"price": price, "quantity": quantity}
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if quantity <= 0 or price < 0:
            print("Invalid price or quantity")
            return

        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

        print(f"Added {quantity} x {name} at {price} each")

    def total(self):
        total_sum = 0
        for data in self.items.values():
            total_sum += data["price"] * data["quantity"]
        return total_sum

    def show(self):
        if not self.items:
            print("Cart is empty")
            return

        print("Shopping cart:")
        for name, data in self.items.items():
            price = data["price"]
            quantity = data["quantity"]
            subtotal = price * quantity
            print(f"- {name}: {quantity} x {price} = {subtotal}")
        print("Total:", self.total())


def demo_task7():
    print("\nTask 7 (optional): ShoppingCart class (demo)")
    cart = ShoppingCart()
    cart.add_item("Apple", 10, 3)
    cart.add_item("Banana", 5, 5)
    cart.add_item("Apple", 10, 2)
    cart.show()


if __name__ == "__main__":
    demo_task1()
    demo_task2()
    demo_task3()
    demo_task4()
    demo_task5()
    demo_task6()
    demo_task7()
