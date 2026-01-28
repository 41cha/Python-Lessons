# Module 11: Advanced Topics
# solutions.py
# Розв'язки до вправ з exercises.py

print("=== Module 11 Solutions: Advanced Topics ===")


def task1_squares_with_list_comprehension():
    print("\nTask 1: Squares with list comprehension")

    squares = [x * x for x in range(1, 11)]
    print("Squares:", squares)


def task2_filter_even_numbers():
    print("\nTask 2: Filter even numbers with list comprehension")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = [n for n in numbers if n % 2 == 0]
    print("Even numbers:", evens)


def task3_transform_strings():
    print("\nTask 3: Transform strings with list comprehension")

    words = ["python", "is", "fun"]
    upper_words = [w.upper() for w in words]
    print("Original:", words)
    print("Upper:", upper_words)


def task4_dict_comprehension_squares():
    print("\nTask 4: Dictionary comprehension for squares")

    squares_dict = {x: x * x for x in range(1, 6)}
    print("Squares dict:", squares_dict)


def task5_enumerate_print_list_with_indexes():
    print("\nTask 5: enumerate — print list with indexes")

    fruits = ["apple", "banana", "cherry"]
    for index, value in enumerate(fruits):
        print(f"{index}: {value}")


def task6_zip_combine_two_lists():
    print("\nTask 6: zip — combine two lists")

    names = ["Andrii", "Maria", "Oleh"]
    ages = [20, 19, 22]

    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")


def task7_zip_enumerate_indexed_pairs():
    print("\nTask 7: zip + enumerate — indexed pairs")

    products = ["Apple", "Banana", "Orange"]
    prices = [10, 5, 7]

    for index, (product, price) in enumerate(zip(products, prices)):
        print(f"{index}: {product} - {price}")


def task8_simple_lambda_function():
    print("\nTask 8: Simple lambda function")

    square = lambda x: x * x  # noqa: E731

    for n in [2, 3, 4, 5]:
        print(f"{n}^2 = {square(n)}")


def task9_lambda_with_sort():
    print("\nTask 9: lambda with sort")

    students = [("Andrii", 20), ("Maria", 19), ("Oleh", 22)]
    print("Original:", students)

    sorted_students = sorted(students, key=lambda item: item[1])
    print("Sorted by age:", sorted_students)


def task10_combine_tools():
    print("\nTask 10 (optional): combine tools")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_squares = [n * n for n in numbers if n % 2 == 0]

    for index, value in enumerate(even_squares):
        print(f"{index}: {value}")


if __name__ == "__main__":
    task1_squares_with_list_comprehension()
    task2_filter_even_numbers()
    task3_transform_strings()
    task4_dict_comprehension_squares()
    task5_enumerate_print_list_with_indexes()
    task6_zip_combine_two_lists()
    task7_zip_enumerate_indexed_pairs()
    task8_simple_lambda_function()
    task9_lambda_with_sort()
    task10_combine_tools()
