# Module 04: Functions
# solutions.py
# Розв'язки до вправ з exercises.py

import math

print("=== Module 04 Solutions: Functions ===")


def greet(name):
    """Task 1: Simple greeting function"""
    print(f"Hello, {name}!")


def circle_area(radius):
    """Task 2: Area of circle"""
    return math.pi * radius * radius


def factorial(n):
    """Task 3: Factorial function"""
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


def add(a, b):
    """Task 4: Calculator functions"""
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


def is_prime(n):
    """Task 5: Is prime number"""
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def info(name, age=18, city="Unknown"):
    """Task 6: Default parameters"""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


def sum_all(*numbers):
    """Task 7 (optional): Variable arguments (*args)"""
    return sum(numbers)


if __name__ == "__main__":
    # Task 1
    print("\nTask 1: Simple greeting function")
    greet("Andrii")

    # Task 2
    print("\nTask 2: Area of circle")
    print("Area for r=5:", circle_area(5))

    # Task 3
    print("\nTask 3: Factorial function")
    print("0! =", factorial(0))
    print("1! =", factorial(1))
    print("5! =", factorial(5))
    print("10! =", factorial(10))

    # Task 4
    print("\nTask 4: Calculator functions")
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))
    print("10 / 0 =", divide(10, 0))

    # Task 5
    print("\nTask 5: Is prime number")
    test_numbers = [2, 7, 17, 25, 29]
    for num in test_numbers:
        print(f"{num} is prime:", is_prime(num))

    # Task 6
    print("\nTask 6: Default parameters")
    info("Andrii")
    info("Maria", 25)
    info("Oleh", 30, "Kyiv")

    # Task 7
    print("\nTask 7 (optional): Variable arguments (*args)")
    print("sum(1, 2, 3) =", sum_all(1, 2, 3))
    print("sum(10, 20, 30, 40) =", sum_all(10, 20, 30, 40))
