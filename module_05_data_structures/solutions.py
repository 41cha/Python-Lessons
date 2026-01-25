# Module 05: Data Structures
# solutions.py
# Розв'язки до вправ з exercises.py

print("=== Module 05 Solutions: Data Structures ===")


def task1_basic_list_operations():
    print("\nTask 1: Basic list operations")

    numbers = [10, 20, 30, 40]
    print("Initial list:", numbers)

    numbers.append(50)
    print("After append:", numbers)

    numbers.pop(1)  # видаляємо елемент з індексом 1 (20)
    print("After pop index 1:", numbers)

    print("Length:", len(numbers))
    print("First element:", numbers[0])
    print("Last element:", numbers[-1])


def task2_list_slicing():
    print("\nTask 2: List slicing")

    words = ["python", "is", "fun", "and", "powerful"]
    print("List:", words)

    first_three = words[:3]
    last_two = words[-2:]
    reversed_list = words[::-1]

    print("First 3:", first_three)
    print("Last 2:", last_two)
    print("Reversed:", reversed_list)


def task3_remove_duplicates_using_set():
    print("\nTask 3: Remove duplicates using set")

    nums = [1, 2, 2, 3, 4, 4, 4, 5]
    print("Original:", nums)

    unique_set = set(nums)
    unique_list = list(unique_set)

    print("Unique set:", unique_set)
    print("Unique list:", unique_list)


def task4_tuple_coordinates():
    print("\nTask 4: Tuple for coordinates")

    point = (3, 5)
    print("Point tuple:", point)

    x = point[0]
    y = point[1]
    print("x:", x)
    print("y:", y)

    # Розпакування
    x2, y2 = point
    print("Unpacked x2:", x2)
    print("Unpacked y2:", y2)


def task5_dictionary_student():
    print("\nTask 5: Dictionary of student")

    student = {
        "name": "Andrii",
        "age": 20,
        "city": "Vinnytsia",
    }

    print("Name:", student["name"])
    print("Age:", student["age"])
    print("City:", student["city"])

    student["city"] = "Kyiv"
    print("Updated city:", student["city"])

    student["grade"] = 95
    print("Student with grade:", student)


def task6_word_frequency():
    print("\nTask 6: Word frequency (dict)")

    text = "python is fun and python is easy"
    words = text.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    print("Text:", text)
    print("Frequency:", freq)


def task7_set_operations():
    print("\nTask 7: Set operations")

    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    intersection = a & b
    union = a | b
    difference = a - b

    print("a:", a)
    print("b:", b)
    print("Intersection (a & b):", intersection)
    print("Union (a | b):", union)
    print("Difference (a - b):", difference)


def task8_list_of_dictionaries():
    print("\nTask 8 (optional): List of dictionaries")

    students = [
        {"name": "Andrii", "age": 20},
        {"name": "Maria", "age": 19},
        {"name": "Oleh", "age": 22},
    ]

    print("Students:", students)

    print("Names:")
    for student in students:
        print("-", student["name"])

    total_age = 0
    for student in students:
        total_age += student["age"]

    average_age = total_age / len(students)
    print("Average age:", average_age)


if __name__ == "__main__":
    task1_basic_list_operations()
    task2_list_slicing()
    task3_remove_duplicates_using_set()
    task4_tuple_coordinates()
    task5_dictionary_student()
    task6_word_frequency()
    task7_set_operations()
    task8_list_of_dictionaries()
