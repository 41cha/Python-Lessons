# Module 02: Control Flow
# solutions.py
# Готові розв'язки до задач з exercises.py

print("=== Module 02 Solutions: Control Flow ===")


def task1_even_or_odd():
    print("\nTask 1: Even or odd")
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


def task2_sign():
    print("\nTask 2: Positive, negative or zero")
    number = float(input("Enter a number: "))
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


def task3_grading_system():
    print("\nTask 3: Grading system")
    score = int(input("Enter score (0-100): "))

    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")


def task4_login_system():
    print("\nTask 4: Simple login system")

    correct_username = "admin"
    correct_password = "1234"

    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
    else:
        print("Invalid credentials")


def task5_max_of_three():
    print("\nTask 5: Max of three numbers")
    a = float(input("First number: "))
    b = float(input("Second number: "))
    c = float(input("Third number: "))

    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c

    print("Max value:", max_value)


def task6_calculator():
    print("\nTask 6 (optional): Simple calculator with operator")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    operation = input("Operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
        print("Result:", result)
    elif operation == "-":
        result = num1 - num2
        print("Result:", result)
    elif operation == "*":
        result = num1 * num2
        print("Result:", result)
    elif operation == "/":
        if num2 == 0:
            print("Error: division by zero")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Unknown operation")


if __name__ == "__main__":
    # Демонстраційний запуск усіх задач
    task1_even_or_odd()
    task2_sign()
    task3_grading_system()
    task4_login_system()
    task5_max_of_three()
    task6_calculator()
