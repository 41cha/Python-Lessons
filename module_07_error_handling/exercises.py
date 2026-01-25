# Module 07: Error Handling
# exercises.py
# try, except, else, finally, raise, базові винятки

print("=== Module 07 Exercises: Error Handling ===")

# Task 1: Safe division
# Напишіть програму, яка:
# 1) зчитує два числа (a, b)
# 2) намагається обчислити a / b
# 3) якщо b = 0 — вивести повідомлення "Cannot divide by zero"
#
# Hint:
# - використайте try/except ZeroDivisionError
print("\nTask 1: Safe division")
# TODO: your code here


# Task 2: Safe integer input
# Напишіть програму, яка:
# 1) запитує у користувача число
# 2) пробує перетворити його на int
# 3) якщо користувач ввів не число — вивести "Invalid integer"
#
# Hint:
# - int(text) може кинути ValueError
print("\nTask 2: Safe integer input")
# TODO: your code here


# Task 3: Safe list index
# Є список:
#   items = ["apple", "banana", "orange"]
# Напишіть програму, яка:
# 1) запитує індекс
# 2) пробує вивести елемент за цим індексом
# 3) якщо індекс виходить за межі — вивести "Index out of range"
#
# Hint:
# - IndexError при items[index]
print("\nTask 3: Safe list index")
# TODO: your code here


# Task 4: File reader with error handling
# Напишіть програму, яка:
# 1) запитує ім'я файлу
# 2) пробує відкрити файл і прочитати його вміст
# 3) якщо файл не знайдено — вивести "File not found"
#
# Hint:
# - використайте try/except FileNotFoundError
# - зручніше відкривати файли через with open(...)
print("\nTask 4: File reader with error handling")
# TODO: your code here


# Task 5: Custom error message with else
# Напишіть програму, яка:
# 1) зчитує два числа
# 2) пробує поділити перше на друге
# 3) якщо помилки немає — вивести результат у блоці else
# 4) якщо сталася помилка ділення на 0 — вивести повідомлення
#
# Hint:
# - структура: try / except / else
print("\nTask 5: Division with else")
# TODO: your code here


# Task 6: Finally block
# Напишіть програму, яка:
# 1) запитує число
# 2) пробує перетворити його на int
# 3) у будь-якому випадку (помилка чи ні) виводить "Done" в блоці finally
#
# Hint:
# - структура: try / except / finally
print("\nTask 6: Input with finally")
# TODO: your code here


# Task 7 (optional): raise ValueError for negative age
# Напишіть програму, яка:
# 1) зчитує вік користувача як int
# 2) якщо вік < 0 — явно кидає ValueError з повідомленням
#    "Age cannot be negative"
# 3) обробляє цей виняток і виводить повідомлення
#
# Hint:
# - використайте raise ValueError("Age cannot be negative")
# - обгорніть у try/except
print("\nTask 7 (optional): raise ValueError for negative age")
# TODO: your code here
