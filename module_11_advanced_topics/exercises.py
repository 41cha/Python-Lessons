# Module 11: Advanced Topics
# exercises.py
# Трохи «просунутих» можливостей Python: list comprehension, enumerate, zip, lambda

print("=== Module 11 Exercises: Advanced Topics ===")

# У цьому файлі тільки ОПИС завдань.
# Рішення шукай у solutions.py


# Task 1: Squares with list comprehension
# Напишіть вираз list comprehension, який створює список квадратів чисел від 1 до 10.
#
# Результат має виглядати так:
#   [1, 4, 9, 16, ..., 100]
#
# Підказка:
# - [x * x for x in range(1, 11)]
print("\nTask 1: Squares with list comprehension")
# TODO: implement in solutions.py


# Task 2: Filter even numbers with list comprehension
# Є список:
#   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Напишіть вираз list comprehension, який залишає тільки парні числа.
#
# Результат:
#   [2, 4, 6, 8, 10]
#
# Підказка:
# - [n for n in numbers if n % 2 == 0]
print("\nTask 2: Filter even numbers with list comprehension")
# TODO: implement in solutions.py


# Task 3: Transform strings with list comprehension
# Є список:
#   words = ["python", "is", "fun"]
# Напишіть вираз list comprehension, який перетворює його на:
#   ["PYTHON", "IS", "FUN"]
#
# Підказка:
# - [w.upper() for w in words]
print("\nTask 3: Transform strings with list comprehension")
# TODO: implement in solutions.py


# Task 4: Dictionary comprehension for squares
# Напишіть вираз dict comprehension, який створює словник квадратів чисел від 1 до 5:
#   {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#
# Підказка:
# - {x: x * x for x in range(1, 6)}
print("\nTask 4: Dictionary comprehension for squares")
# TODO: implement in solutions.py


# Task 5: enumerate — print list with indexes
# Використовуючи enumerate, надрукуйте елементи списку з індексами.
# Наприклад, для:
#   fruits = ["apple", "banana", "cherry"]
# виведіть:
#   0: apple
#   1: banana
#   2: cherry
#
# Підказка:
# - for index, value in enumerate(fruits):
print("\nTask 5: enumerate — print list with indexes")
# TODO: implement in solutions.py


# Task 6: zip — combine two lists
# Є два списки однакової довжини:
#   names = ["Andrii", "Maria", "Oleh"]
#   ages =  [20,       19,       22]
#
# Використовуючи zip, пройдіться по обох списках одночасно і виведіть:
#   Andrii is 20 years old
#   Maria is 19 years old
#   Oleh is 22 years old
#
# Підказка:
# - for name, age in zip(names, ages):
print("\nTask 6: zip — combine two lists")
# TODO: implement in solutions.py


# Task 7: zip + enumerate — indexed pairs
# Є два списки:
#   products = ["Apple", "Banana", "Orange"]
#   prices =   [10,       5,        7]
#
# Використовуючи одночасно zip та enumerate, виведіть:
#   0: Apple - 10
#   1: Banana - 5
#   2: Orange - 7
#
# Підказка:
# - for index, (product, price) in enumerate(zip(products, prices)):
print("\nTask 7: zip + enumerate — indexed pairs")
# TODO: implement in solutions.py


# Task 8: Simple lambda function
# Створіть lambda-функцію, яка:
# 1) приймає число
# 2) повертає його квадрат
#
# Використайте її для обчислення квадрата кількох чисел і виведіть результати.
#
# Підказка:
# - square = lambda x: x * x
print("\nTask 8: Simple lambda function")
# TODO: implement in solutions.py


# Task 9: lambda with sort
# Є список кортежів:
#   students = [("Andrii", 20), ("Maria", 19), ("Oleh", 22)]
#
# Відсортуйте цей список за віком (другий елемент кортежу) за допомогою:
#   - функції sorted(...)
#   - параметра key з lambda-функцією
#
# Результат:
#   [("Maria", 19), ("Andrii", 20), ("Oleh", 22)]
#
# Підказка:
# - sorted(students, key=lambda item: item[1])
print("\nTask 9: lambda with sort")
# TODO: implement in solutions.py


# Task 10 (optional): combine tools
# (Додатково, якщо цікаво)
#
# Є список:
#   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Зробіть наступне:
# 1) за допомогою list comprehension створіть список квадратів ТІЛЬКИ парних чисел
# 2) виведіть їх разом з індексами за допомогою enumerate
#
# Очікуваний результат:
#   0: 4
#   1: 16
#   2: 36
#   3: 64
#   4: 100
print("\nTask 10 (optional): combine tools")
# TODO: implement in solutions.py
