# Module 01: Introduction and Basics
# solutions.py
# Повні розв'язки до задач з exercises.py

print("=== Module 01 Solutions ===")

def task1_calculator():
    print("\nTask 1: Simple calculator")

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    print(f"Sum: {num1 + num2}")
    print(f"Difference: {num1 - num2}")
    print(f"Product: {num1 * num2}")

    if num2 != 0:
        print(f"Quotient: {num1 / num2}")

    else:
        print("Quotient: division by zero!")

def task2_converter():
    print("\nTask 2: Celsius to Fahrenheit converter")

    celsius = float(input("Temperature in Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32

    print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")

def task3_personal_info():
    print("\nTask 3: Personal info")
    name = input("Your name: ")
    age = int(input("Your age: "))
    height = float(input("Your height (m): "))
    print(f"Hello, {name}! You are {age} years old and {height} m tall.")

def task4_rectangle():
    print("\nTask 4: Rectangle area and perimeter")
    length = float(input("Length: "))
    width = float(input("Width: "))
    area = length * width
    perimeter = 2 * (length + width)

    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")

def task5_data_types():
    print("\nTask 5: Data types")
    integer_number = 42
    float_number = 3.14
    text_value = "Python"
    bool_value = True
    
    print(type(integer_number))
    print(type(float_number))
    print(type(text_value))
    print(type(bool_value))

if __name__ == "__main__":
    # Demo run of all tasks
    task1_calculator()
    task2_converter()
    task3_personal_info()
    task4_rectangle()
    task5_data_types()
