# Module 06: Strings
# exercises.py
# Робота з рядками: методи, перевірки, split/join, пошук, форматування

print("=== Module 06 Exercises: Strings ===")

# Task 1: Basic string info
# Напишіть програму, яка:
# 1) запитує в користувача рядок
# 2) виводить:
#    - довжину рядка
#    - цей же рядок у верхньому регістрі
#    - цей же рядок у нижньому регістрі
#
# Hint:
# - len(text), text.upper(), text.lower()
print("\nTask 1: Basic string info")
# TODO: your code here


# Task 2: Trim spaces
# Напишіть програму, яка:
# 1) зчитує рядок з пробілами на початку і в кінці
# 2) виводить:
#    - оригінальний рядок (у лапках)
#    - обрізаний рядок без зайвих пробілів (у лапках)
#
# Hint:
# - text.strip()
# - використайте f-рядок: print(f'\"{text}\"')
print("\nTask 2: Trim spaces")
# TODO: your code here


# Task 3: Count vowels
# Напишіть програму, яка:
# 1) зчитує рядок
# 2) рахує кількість голосних літер (a, e, i, o, u, y)
#    незалежно від регістру
#
# Hint:
# - перетворіть рядок у нижній регістр: text.lower()
# - перебирайте символи в циклі
# - перевіряйте, чи символ в "aeiouy"
print("\nTask 3: Count vowels")
# TODO: your code here


# Task 4: Replace word
# Є рядок:
#   text = "Python is hard, but Python is fun"
# Напишіть програму, яка:
# 1) замінює всі входження "Python" на "JavaScript"
# 2) виводить новий рядок
#
# Hint:
# - text.replace("Python", "JavaScript")
print("\nTask 4: Replace word")
# TODO: your code here


# Task 5: Split and join
# Є рядок:
#   text = "Python is fun and powerful"
# Напишіть програму, яка:
# 1) розбиває рядок на слова
# 2) збирає їх назад у один рядок, розділяючи тире "-"
#    результат: "Python-is-fun-and-powerful"
#
# Hint:
# - words = text.split()
# - "-".join(words)
print("\nTask 5: Split and join")
# TODO: your code here


# Task 6: Simple email validator (very basic)
# Напишіть програму, яка:
# 1) зчитує рядок email
# 2) перевіряє, чи:
#    - є символ "@"
#    - є хоча б одна крапка "." після "@"
# 3) виводить "Valid email" або "Invalid email"
#
# Hint:
# - використайте .find("@")
# - знайдіть позицію крапки після собаки
print("\nTask 6: Simple email validator (basic)")
# TODO: your code here


# Task 7: Palindrome checker
# Паліндром — це рядок, який читається однаково зліва направо і справа наліво
# (ігноруємо пробіли і регістр), наприклад: "level", "racecar".
#
# Напишіть програму, яка:
# 1) зчитує рядок
# 2) видаляє пробіли й переводить у нижній регістр
# 3) перевіряє, чи це паліндром
#
# Hint:
# - text.replace(" ", "").lower()
# - порівняйте очищений рядок з його розворотом [::-1]
print("\nTask 7: Palindrome checker")
# TODO: your code here


# Task 8 (optional): Character frequency
# Напишіть програму, яка:
# 1) зчитує рядок
# 2) рахує, скільки разів кожен символ зустрічається в рядку
# 3) виводить результат у вигляді:
#    символ -> кількість
#
# Hint:
# - використайте словник: dict[char] = count
# - переберіть усі символи рядка
print("\nTask 8 (optional): Character frequency")
# TODO: your code here
