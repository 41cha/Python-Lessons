# Module 05: Data Structures
# exercises.py
# Lists, tuples, sets, dictionaries, basic operations

print("=== Module 05 Exercises: Data Structures ===")

# Task 1: Basic list operations
# Створіть список numbers з кількох цілих чисел.
# 1) додайте новий елемент у кінець
# 2) видаліть один елемент
# 3) виведіть:
#    - довжину списку
#    - перший та останній елементи
#
# Hint:
# - .append(), .pop() або del
# - len(numbers), numbers[0], numbers[-1]
print("\nTask 1: Basic list operations")
# TODO: your code here


# Task 2: List slicing
# Створіть список words з кількох рядків.
# 1) виведіть перші 3 елементи (як підсписок)
# 2) виведіть останні 2 елементи
# 3) виведіть список у зворотному порядку
#
# Hint:
# - words[:3], words[-2:], words[::-1]
print("\nTask 2: List slicing")
# TODO: your code here


# Task 3: Remove duplicates using set
# Є список з повтореннями, наприклад:
#   nums = [1, 2, 2, 3, 4, 4, 4, 5]
# 1) створіть множину з цього списку (щоб прибрати дублікати)
# 2) перетворіть множину назад у список
# 3) виведіть результат
#
# Hint:
# - set(nums), list(my_set)
print("\nTask 3: Remove duplicates using set")
# TODO: your code here


# Task 4: Tuple for coordinates
# Створіть кортеж point, який зберігає координати (x, y), наприклад (3, 5).
# 1) виведіть x та y окремо
# 2) розпакуйте кортеж у дві змінні: x, y = point
#
# Hint:
# - доступ по індексу: point[0], point[1]
# - розпакування: x, y = point
print("\nTask 4: Tuple for coordinates")
# TODO: your code here


# Task 5: Dictionary of student
# Створіть словник student з полями:
#   name, age, city
# 1) виведіть значення кожного поля
# 2) змініть місто
# 3) додайте поле "grade"
#
# Hint:
# - student["name"], student["age"]
# - student["city"] = "New City"
# - student["grade"] = 95
print("\nTask 5: Dictionary of student")
# TODO: your code here


# Task 6: Word frequency (dict)
# Є рядок:
#   text = "python is fun and python is easy"
# 1) розбийте рядок на слова
# 2) порахуйте, скільки разів кожне слово зустрічається
# 3) збережіть результати у словнику:
#    ключ — слово, значення — кількість
#
# Hint:
# - text.split()
# - перевіряйте, чи слово вже є в словнику, перед збільшенням лічильника
print("\nTask 6: Word frequency (dict)")
# TODO: your code here


# Task 7: Set operations
# Є дві множини:
#   a = {1, 2, 3, 4}
#   b = {3, 4, 5, 6}
# 1) знайдіть перетин (спільні елементи)
# 2) об'єднання
# 3) різницю a - b
#
# Hint:
# - a & b, a | b, a - b
print("\nTask 7: Set operations")
# TODO: your code here


# Task 8 (optional): List of dictionaries
# Створіть список students, де кожен елемент — словник з полями:
#   name, age
# Наприклад:
#   {"name": "Andrii", "age": 20}
#   {"name": "Maria", "age": 19}
# 1) виведіть імена всіх студентів
# 2) знайдіть середній вік
#
# Hint:
# - for student in students: student["name"]
# - рахуйте суму віків і поділіть на кількість
print("\nTask 8 (optional): List of dictionaries")
# TODO: your code here
