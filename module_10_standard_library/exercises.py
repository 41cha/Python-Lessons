# Module 10: Standard Library
# exercises.py
# Практика з модулями стандартної бібліотеки: random, datetime, os, json

print("=== Module 10 Exercises: Standard Library ===")

# У цьому модулі ми НЕ реалізуємо код тут.
# У файлі exercises.py описані лише завдання.
# Рішення дивись у solutions.py


# Task 1: Random number game
# Модуль: random
#
# Напишіть програму, яка:
# 1) генерує випадкове ціле число від 1 до 10 (включно)
# 2) запитує в користувача число
# 3) виводить:
#    - "You guessed it!", якщо користувач вгадав
#    - "Too low" або "Too high", якщо не вгадав (в залежності від того, менше чи більше)
#
# Підказка:
# - import random
# - random.randint(1, 10)
print("\nTask 1: Random number game")
# TODO: implement in solutions.py


# Task 2: Random choice from list
# Модуль: random
#
# Напишіть програму, яка:
# 1) має список варіантів, наприклад ["rock", "paper", "scissors"]
# 2) випадковим чином обирає один елемент і виводить його
#
# Підказка:
# - random.choice(sequence)
print("\nTask 2: Random choice from list")
# TODO: implement in solutions.py


# Task 3: Current date and time
# Модуль: datetime
#
# Напишіть програму, яка:
# 1) отримує поточні дату й час
# 2) виводить їх у різних форматах:
#    - "Raw" datetime-об'єкт
#    - тільки дату у форматі "YYYY-MM-DD"
#    - тільки час у форматі "HH:MM"
#
# Підказка:
# - import datetime
# - datetime.datetime.now()
# - .strftime("%Y-%m-%d")
print("\nTask 3: Current date and time")
# TODO: implement in solutions.py


# Task 4: Days until New Year
# Модуль: datetime
#
# Напишіть програму, яка:
# 1) отримує сьогоднішню дату
# 2) створює об'єкт дати для наступного 1 січня
# 3) рахує й виводить, скільки днів залишилося до Нового року
#
# Підказка:
# - datetime.date.today()
# - datetime.date(year, month, day)
# - різниця між датами -> об'єкт timedelta з полем .days
print("\nTask 4: Days until New Year")
# TODO: implement in solutions.py


# Task 5: List files in current directory
# Модуль: os
#
# Напишіть програму, яка:
# 1) виводить поточну робочу директорію
# 2) виводить список усіх файлів і папок у поточній директорії
#
# Підказка:
# - import os
# - os.getcwd()
# - os.listdir()
print("\nTask 5: List files in current directory")
# TODO: implement in solutions.py


# Task 6: Check if file exists
# Модуль: os.path
#
# Напишіть програму, яка:
# 1) запитує ім'я файлу
# 2) перевіряє, чи існує такий файл у поточній директорії
# 3) виводить "File exists" або "File does not exist"
#
# Підказка:
# - import os
# - os.path.exists("filename")
print("\nTask 6: Check if file exists")
# TODO: implement in solutions.py


# Task 7: Save data to JSON file
# Модуль: json
#
# Напишіть програму, яка:
# 1) створює словник з даними користувача, наприклад:
#       user = {"name": "Andrii", "age": 20, "city": "Vinnytsia"}
# 2) запитує ім'я файлу (наприклад, user.json)
# 3) зберігає цей словник у JSON-файл
#
# Підказка:
# - import json
# - json.dump(data, file_object, ensure_ascii=False, indent=2)
print("\nTask 7: Save data to JSON file")
# TODO: implement in solutions.py


# Task 8: Load data from JSON file
# Модуль: json
#
# Напишіть програму, яка:
# 1) запитує ім'я JSON-файлу
# 2) відкриває файл і завантажує з нього дані
# 3) виводить завантажений словник (ключі та значення)
#
# Підказка:
# - json.load(file_object)
print("\nTask 8: Load data from JSON file")
# TODO: implement in solutions.py


# Task 9 (optional): Simple log with timestamp
# Модулі: datetime, os
#
# Напишіть програму, яка:
# 1) запитує повідомлення від користувача
# 2) записує його у файл app.log у режимі дописування
# 3) перед повідомленням додає timestamp (дата + час)
#    у форматі "YYYY-MM-DD HH:MM:SS"
#
# Підказка:
# - datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("\nTask 9 (optional): Simple log with timestamp")
# TODO: implement in solutions.py
