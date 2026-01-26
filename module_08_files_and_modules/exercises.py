# Module 08: Files and Modules
# exercises.py
# Робота з файлами (читання/запис) та модулями (import)

print("=== Module 08 Exercises: Files and Modules ===")

# Task 1: Read whole file
# Напишіть програму, яка:
# 1) запитує ім'я текстового файлу (наприклад, data.txt)
# 2) відкриває цей файл у режимі читання
# 3) читає весь вміст і виводить його на екран
#
# Важливо:
# - використайте конструкцію with open(..., "r", encoding="utf-8") as f:
# - поки що можна не обробляти помилки (це було в попередньому модулі)
print("\nTask 1: Read whole file")
# TODO: your code here


# Task 2: Read file line by line
# Напишіть програму, яка:
# 1) запитує ім'я файлу
# 2) читає файл по рядках у циклі
# 3) виводить кожен рядок, додаючи перед ним номер рядка (починаючи з 1)
#
# Приклад формату:
#   1: This is the first line
#   2: This is the second line
print("\nTask 2: Read file line by line")
# TODO: your code here


# Task 3: Write user input to file
# Напишіть програму, яка:
# 1) запитує ім'я файлу для запису
# 2) запитує в користувача кілька рядків тексту
# 3) записує ці рядки у файл (кожен з нового рядка)
#
# Спрощення:
# - можна, наприклад, запитати спочатку "How many lines?" і потім стільки разів зчитати текст
# - відкрийте файл у режимі "w" (перезапис файлу)
print("\nTask 3: Write user input to file")
# TODO: your code here


# Task 4: Append to log file
# Напишіть програму, яка:
# 1) завжди пише повідомлення у файл log.txt у режимі дописування ("a")
# 2) у повідомленні записує:
#    - текст, введений користувачем
# 3) після запису виводить "Message saved to log.txt"
#
# Підказка:
# - режим "a" додає нові рядки в кінець файлу, не перезаписуючи існуючий вміст
print("\nTask 4: Append to log file")
# TODO: your code here


# Task 5: Count lines in file
# Напишіть програму, яка:
# 1) запитує ім'я файлу
# 2) рахує, скільки рядків у файлі
# 3) виводить "Lines: X"
#
# Підказка:
# - можна читати по рядках у циклі та збільшувати лічильник
print("\nTask 5: Count lines in file")
# TODO: your code here


# Task 6: Import math module
# Напишіть програму, яка:
# 1) імпортує модуль math
# 2) зчитує число (float)
# 3) виводить:
#    - квадратний корінь (math.sqrt)
#    - число, округлене вниз (math.floor)
#    - число, округлене вгору (math.ceil)
#
# Підказка:
# - import math
print("\nTask 6: Import math module")
# TODO: your code here


# Task 7: Import from custom module
# Створіть ОКРЕМИЙ файл helper.py у цій самій папці.
# У helper.py створіть 2 функції:
#   - add(a, b) -> повертає суму
#   - multiply(a, b) -> повертає добуток
#
# У ЦЬОМУ файлі (exercises.py):
# 1) імпортуйте ці функції з helper.py
# 2) викличте їх з кількома тестовими значеннями
# 3) виведіть результати
#
# Підказка:
# - from helper import add, multiply
print("\nTask 7: Import from custom module")
# TODO: your code here


# Task 8 (optional): Simple CSV reader
# (Додатково, якщо цікаво йти далі)
# Створіть файл data.csv з кількома рядками, наприклад:
#   name,age
#   Andrii,20
#   Maria,19
#
# Напишіть програму, яка:
# 1) відкриває data.csv
# 2) читає файл по рядках
# 3) пропускає перший рядок (заголовки)
# 4) для кожного наступного рядка виводить "Name: <name>, Age: <age>"
#
# Підказка:
# - розбийте рядок за комою: line.strip().split(",")
print("\nTask 8 (optional): Simple CSV reader")
# TODO: your code here
