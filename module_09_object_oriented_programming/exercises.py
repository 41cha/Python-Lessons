# Module 09: Object-Oriented Programming
# exercises.py
# Класи, об'єкти, методи, __init__, інкапсуляція, наслідування

print("=== Module 09 Exercises: Object-Oriented Programming ===")

# Task 1: Simple Person class
# Створіть клас Person, який:
# 1) у __init__ приймає name та age і зберігає їх як атрибути
# 2) має метод introduce(self), який виводить повідомлення:
#    "Hi, my name is <name> and I am <age> years old."
#
# У цій вправі в файлі exercises.py:
# - тільки ОПИС завдання (реалізація в solutions.py)
print("\nTask 1: Simple Person class")
# TODO: implement in solutions.py


# Task 2: BankAccount class
# Створіть клас BankAccount, який:
# 1) у __init__ приймає owner (ім'я власника) і optional balance (за замовчуванням 0)
# 2) має методи:
#    - deposit(self, amount): додає amount до балансу, виводить новий баланс
#    - withdraw(self, amount):
#         - якщо на рахунку достатньо коштів — знімає amount і виводить новий баланс
#         - інакше виводить "Insufficient funds"
#    - get_balance(self): повертає поточний баланс
#
# Не треба робити від'ємний баланс.
print("\nTask 2: BankAccount class")
# TODO: implement in solutions.py


# Task 3: Rectangle class with area and perimeter
# Створіть клас Rectangle, який:
# 1) у __init__ приймає width та height
# 2) має метод area(self), який повертає площу прямокутника
# 3) має метод perimeter(self), який повертає периметр
#
# Додатково (необов'язково): метод is_square(self), який повертає True, якщо width == height.
print("\nTask 3: Rectangle class with area and perimeter")
# TODO: implement in solutions.py


# Task 4: Encapsulation with getters/setters
# Створіть клас User, який:
# 1) у __init__ приймає username та password
# 2) зберігає пароль у «приватному» полі (наприклад, self._password)
# 3) має метод check_password(self, password), який повертає True/False
# 4) має метод set_password(self, old_password, new_password):
#       - якщо old_password правильний — змінює пароль
#       - інакше виводить повідомлення про помилку
#
# Тут ми тренуємо ідею інкапсуляції: доступ до паролю тільки через методи.
print("\nTask 4: Encapsulation with getters/setters")
# TODO: implement in solutions.py


# Task 5: Inheritance - Animal and Dog
# Створіть:
# 1) базовий клас Animal з:
#       - __init__(self, name)
#       - методом speak(self), який просто виводить "Some sound"
# 2) клас Dog, який наслідує Animal і:
#       - викликає __init__ батька (через super().__init__(name))
#       - перевизначає метод speak(self), щоб він виводив "Woof!"
#
# Створіть кілька об'єктів Dog і перевірте, як працює наслідування та перевизначення.
print("\nTask 5: Inheritance - Animal and Dog")
# TODO: implement in solutions.py


# Task 6: Inheritance - Vehicle and Car
# Створіть:
# 1) клас Vehicle з полями:
#       - brand
#       - model
#    та методом info(self), який виводить "<brand> <model>"
# 2) клас Car, який наслідує Vehicle, додає поле year і перевизначає info(self),
#    щоб виводити "<brand> <model> (<year>)"
#
# Продемонструйте створення Car і виклик info().
print("\nTask 6: Inheritance - Vehicle and Car")
# TODO: implement in solutions.py


# Task 7 (optional): ShoppingCart class
# Створіть клас ShoppingCart, який:
# 1) у __init__ створює порожній список/словник для товарів
# 2) має метод add_item(self, name, price, quantity=1):
#       - додає товар у кошик
#       - якщо товар уже є, збільшує кількість
# 3) має метод total(self), який повертає загальну суму по кошику
# 4) має метод show(self), який виводить усі товари й загальну суму
#
# Це хороша вправа на те, як клас може інкапсулювати дані + логіку над ними.
print("\nTask 7 (optional): ShoppingCart class")
# TODO: implement in solutions.py
