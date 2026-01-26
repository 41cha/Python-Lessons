# Module 08: Files and Modules
# solutions.py
# Розв'язки до вправ з exercises.py

print("=== Module 08 Solutions: Files and Modules ===")


def task1_read_whole_file():
    print("\nTask 1: Read whole file")

    filename = input("Enter filename: ")

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print("File content:")
        print(content)


def task2_read_file_line_by_line():
    print("\nTask 2: Read file line by line")

    filename = input("Enter filename: ")

    with open(filename, "r", encoding="utf-8") as f:
        line_number = 1
        for line in f:
            line = line.rstrip("\n")
            print(f"{line_number}: {line}")
            line_number += 1


def task3_write_user_input_to_file():
    print("\nTask 3: Write user input to file")

    filename = input("Enter filename to write: ")
    lines_count_str = input("How many lines do you want to write? ")

    try:
        lines_count = int(lines_count_str)
    except ValueError:
        print("Invalid number of lines")
        return

    with open(filename, "w", encoding="utf-8") as f:
        for i in range(1, lines_count + 1):
            text = input(f"Line {i}: ")
            f.write(text + "\n")

    print(f"Saved {lines_count} lines to {filename}")


def task4_append_to_log():
    print("\nTask 4: Append to log file")

    message = input("Enter message: ")

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

    print("Message saved to log.txt")


def task5_count_lines_in_file():
    print("\nTask 5: Count lines in file")

    filename = input("Enter filename: ")

    count = 0
    with open(filename, "r", encoding="utf-8") as f:
        for _ in f:
            count += 1

    print("Lines:", count)


def task6_import_math_module():
    print("\nTask 6: Import math module")

    import math

    number_str = input("Enter a number: ")

    try:
        number = float(number_str)
    except ValueError:
        print("Invalid number")
        return

    print("sqrt:", math.sqrt(number))
    print("floor:", math.floor(number))
    print("ceil:", math.ceil(number))


def task7_import_from_custom_module():
    print("\nTask 7: Import from custom module")

    from helper import add, multiply

    a = 10
    b = 5

    print("a =", a, "b =", b)
    print("add(a, b) =", add(a, b))
    print("multiply(a, b) =", multiply(a, b))


def task8_simple_csv_reader():
    print("\nTask 8 (optional): Simple CSV reader")

    filename = "data.csv"
    print(f"Reading {filename}...")

    with open(filename, "r", encoding="utf-8") as f:
        first_line = True
        for line in f:
            line = line.strip()
            if not line:
                continue  # пропустити порожні рядки

            if first_line:
                # пропускаємо заголовок "name,age"
                first_line = False
                continue

            parts = line.split(",")
            if len(parts) != 2:
                print("Invalid line:", line)
                continue

            name = parts[0]
            age = parts[1]
            print(f"Name: {name}, Age: {age}")


if __name__ == "__main__":
    task1_read_whole_file()
    task2_read_file_line_by_line()
    task3_write_user_input_to_file()
    task4_append_to_log()
    task5_count_lines_in_file()
    task6_import_math_module()
    task7_import_from_custom_module()
    task8_simple_csv_reader()
