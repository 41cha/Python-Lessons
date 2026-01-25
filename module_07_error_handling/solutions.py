# Module 07: Error Handling
# solutions.py
# Розв'язки до вправ з exercises.py

print("=== Module 07 Solutions: Error Handling ===")


def task1_safe_division():
    print("\nTask 1: Safe division")

    a_str = input("Enter a: ")
    b_str = input("Enter b: ")

    try:
        a = float(a_str)
        b = float(b_str)
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero")


def task2_safe_integer_input():
    print("\nTask 2: Safe integer input")

    text = input("Enter an integer: ")

    try:
        value = int(text)
        print("You entered integer:", value)
    except ValueError:
        print("Invalid integer")


def task3_safe_list_index():
    print("\nTask 3: Safe list index")

    items = ["apple", "banana", "orange"]
    print("Items:", items)

    index_str = input("Enter index: ")

    try:
        index = int(index_str)
        print("Item:", items[index])
    except ValueError:
        print("Index must be an integer")
    except IndexError:
        print("Index out of range")


def task4_file_reader():
    print("\nTask 4: File reader with error handling")

    filename = input("Enter filename: ")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found")


def task5_division_with_else():
    print("\nTask 5: Division with else")

    a_str = input("Enter a: ")
    b_str = input("Enter b: ")

    try:
        a = float(a_str)
        b = float(b_str)
        result = a / b
    except ZeroDivisionError:
        print("Error: division by zero")
    else:
        print("Result:", result)


def task6_input_with_finally():
    print("\nTask 6: Input with finally")

    text = input("Enter an integer: ")

    try:
        value = int(text)
        print("You entered:", value)
    except ValueError:
        print("This is not an integer")
    finally:
        print("Done")


def task7_raise_negative_age():
    print("\nTask 7 (optional): raise ValueError for negative age")

    text = input("Enter your age: ")

    try:
        age = int(text)
        if age < 0:
            raise ValueError("Age cannot be negative")
        print("Your age:", age)
    except ValueError as e:
        # Сюди потрапляє як некоректне перетворення, так і наш власний виняток
        print("Error:", e)


if __name__ == "__main__":
    task1_safe_division()
    task2_safe_integer_input()
    task3_safe_list_index()
    task4_file_reader()
    task5_division_with_else()
    task6_input_with_finally()
    task7_raise_negative_age()
