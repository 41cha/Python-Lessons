# Module 04: Functions
# exercises.py
# Створення функцій, параметри, return, область видимості

print("=== Module 04 Exercises: Functions ===")

# Task 1: Simple greeting function
# Створіть функцію greet(name), яка:
# 1) приймає параметр name (рядок)
# 2) виводить "Hello, [name]!"
# 3) викликайте функцію з вашим ім'ям
#
# Hint:
# - def greet(name):
# - print(f"Hello, {name}!")
print("\nTask 1: Simple greeting function")
# TODO: define function
# TODO: call function


# Task 2: Area of circle
# Створіть функцію circle_area(radius), яка:
# 1) приймає радіус (float)
# 2) повертає площу кола (π * r², π ≈ 3.1416)
# 3) викличте функцію та виведіть результат
#
# Hint:
# - використайте math.pi для точного π
# - return radius * radius * math.pi
print("\nTask 2: Area of circle")
# TODO: define function
# TODO: call function


# Task 3: Factorial function
# Створіть функцію factorial(n), яка:
# 1) приймає ціле число n >= 0
# 2) повертає факторіал n! (1 * 2 * ... * n)
# 3) протестуйте для n = 0, 1, 5, 10
#
# Hint:
# - для n == 0 повертайте 1
# - використайте цикл for або рекурсію
print("\nTask 3: Factorial function")
# TODO: define function
# TODO: test function


# Task 4: Calculator functions
# Створіть чотири функції:
# 1) add(a, b) — сума
# 2) subtract(a, b) — різниця
# 3) multiply(a, b) — добуток
# 4) divide(a, b) — частка (з перевіркою на 0)
#
# Викличте кожну та виведіть результат.
#
# Hint:
# - в divide() перевірте b != 0
print("\nTask 4: Calculator functions")
# TODO: define functions
# TODO: test functions


# Task 5: Is prime number
# Створіть функцію is_prime(n), яка:
# 1) приймає ціле число n > 1
# 2) повертає True, якщо n просте, False — якщо складне
# 3) протестуйте для 2, 7, 17, 25, 29
#
# Hint:
# - просте число ділиться тільки на 1 і на себе
# - перевірте ділення на числа від 2 до sqrt(n)
print("\nTask 5: Is prime number")
# TODO: define function
# TODO: test function


# Task 6: Default parameters
# Створіть функцію info(name, age=18, city="Unknown"), яка:
# 1) виводить інформацію про користувача
# 2) протестуйте з різною кількістю аргументів
#
# Hint:
# - параметри з = мають значення за замовчуванням
print("\nTask 6: Default parameters")
# TODO: define function
# TODO: test function


# Task 7 (optional): Variable arguments (*args)
# Створіть функцію sum_all(*numbers), яка:
# 1) приймає будь-яку кількість чисел
# 2) повертає їхню суму
# 3) протестуйте з 2, 3, 5 числами
#
# Hint:
# - *args перетворює аргументи на кортеж
# - використайте sum(numbers) або цикл
print("\nTask 7 (optional): Variable arguments (*args)")
# TODO: define function
# TODO: test function
