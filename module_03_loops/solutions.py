# Module 03: Loops
# solutions.py
# Розв'язки до задач з exercises.py

print("=== Module 03 Solutions: Loops ===")


def task1_count_to_n():
    print("\nTask 1: Count from 1 to N (while)")
    n = int(input("Enter N (> 0): "))

    i = 1
    while i <= n:
        print(i)
        i += 1


def task2_multiplication_table():
    print("\nTask 2: Multiplication table (for + range)")
    n = int(input("Enter a number: "))

    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def task3_sum_to_n():
    print("\nTask 3: Sum of numbers from 1 to N")
    n = int(input("Enter N (> 0): "))

    total = 0
    for i in range(1, n + 1):
        total += i

    print("Sum from 1 to", n, "=", total)


def task4_count_even_in_list():
    print("\nTask 4: Count even numbers in a list")
    numbers = [1, 4, 7, 10, 12, 15]
    count_even = 0

    for number in numbers:
        if number % 2 == 0:
            count_even += 1

    print("Even numbers count:", count_even)


def task5_password_attempts():
    print("\nTask 5: Password attempts (while + break)")
    secret = "python123"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        pwd = input("Enter password: ")
        if pwd == secret:
            print("Access granted")
            break
        else:
            print("Wrong password")
            attempts += 1

    if attempts == max_attempts and pwd != secret:
        print("Access denied")


def task6_skip_negative():
    print("\nTask 6: Skip negative numbers (continue)")
    nums = [3, -1, 5, -2, 0, 7]

    for num in nums:
        if num < 0:
            continue
        print(num)


def task7_guessing_game():
    print("\nTask 7 (optional): Simple guessing game")
    secret = 7

    while True:
        guess = int(input("Guess the number: "))

        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print("You guessed it!")
            break


if __name__ == "__main__":
    # Демонстраційний запуск усіх задач
    task1_count_to_n()
    task2_multiplication_table()
    task3_sum_to_n()
    task4_count_even_in_list()
    task5_password_attempts()
    task6_skip_negative()
    task7_guessing_game()
