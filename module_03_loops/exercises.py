# Module 03: Loops
# exercises.py
# Цикли while, for, range(), break, continue, вкладені цикли

print("=== Module 03 Exercises: Loops ===")

# Task 1: Count from 1 to N (while)
# Напишіть програму, яка:
# 1) запитує ціле число N (> 0)
# 2) виводить усі числа від 1 до N включно, по одному в рядок
#
# Hint:
# - використайте while-цикл
# - створіть лічильник i, який починається з 1
# - на кожній ітерації збільшуйте i на 1
print("\nTask 1: Count from 1 to N (while)")
# TODO: your code here


# Task 2: Multiplication table (for + range)
# Напишіть програму, яка:
# 1) запитує число n
# 2) виводить таблицю множення для n від 1 до 10
#    приклад для n = 3:
#    3 x 1 = 3
#    3 x 2 = 6
#    ...
#    3 x 10 = 30
#
# Hint:
# - використайте for з range(1, 11)
print("\nTask 2: Multiplication table (for + range)")
# TODO: your code here


# Task 3: Sum of numbers from 1 to N
# Напишіть програму, яка:
# 1) запитує N
# 2) обчислює суму всіх чисел від 1 до N
# 3) виводить результат
#
# Hint:
# - створіть змінну total = 0
# - в циклі додавайте до total поточне число
# - можна використати for або while
print("\nTask 3: Sum of numbers from 1 to N")
# TODO: your code here


# Task 4: Count even numbers in a list
# Напишіть програму, яка:
# 1) має заздалегідь створений список, наприклад:
#    numbers = [1, 4, 7, 10, 12, 15]
# 2) рахує, скільки в ньому парних чисел
# 3) виводить кількість парних
#
# Hint:
# - використайте for для проходу по списку
# - перевіряйте number % 2 == 0
print("\nTask 4: Count even numbers in a list")
# TODO: your code here


# Task 5: Password attempts (while + break)
# Напишіть програму, яка:
# 1) має захардкоджений правильний пароль, наприклад: secret = "python123"
# 2) дозволяє користувачу вводити пароль до 3 разів
# 3) якщо пароль вірний — вивести "Access granted" і завершити цикл
# 4) якщо після 3 спроб пароль не вгадано — вивести "Access denied"
#
# Hint:
# - використайте while з лічильником спроб або while True з break
# - кожного разу збільшуйте кількість спроб на 1
print("\nTask 5: Password attempts (while + break)")
# TODO: your code here


# Task 6: Skip negative numbers (continue)
# Напишіть програму, яка:
# 1) має список чисел, наприклад:
#    nums = [3, -1, 5, -2, 0, 7]
# 2) виводить тільки НЕвід’ємні числа (>= 0)
#
# Hint:
# - використайте for по списку
# - якщо число негативне — зробіть continue, щоб пропустити вивід
print("\nTask 6: Skip negative numbers (continue)")
# TODO: your code here


# Task 7 (optional): Simple guessing game
# Напишіть просту гру:
# 1) захардкодьте секретне число, наприклад: secret = 7
# 2) у циклі запитуйте число у користувача, поки він не вгадає
# 3) якщо введене число менше — виведіть "Too low"
#    якщо більше — "Too high"
#    якщо дорівнює — "You guessed it!" і вийдіть з циклу
#
# Hint:
# - використайте while True
# - виходьте з циклу через break, коли користувач вгадав
print("\nTask 7 (optional): Simple guessing game")
# TODO: your code here
