# Module 10: Standard Library
# solutions.py
# Розв'язки до вправ з exercises.py

print("=== Module 10 Solutions: Standard Library ===")


def task1_random_number_game():
    print("\nTask 1: Random number game")

    import random

    secret = random.randint(1, 10)
    guess_str = input("Guess a number between 1 and 10: ")

    try:
        guess = int(guess_str)
    except ValueError:
        print("Invalid number")
        return

    if guess == secret:
        print("You guessed it!")
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

    print(f"(Secret was: {secret})")  # щоб було видно при тестуванні


def task2_random_choice_from_list():
    print("\nTask 2: Random choice from list")

    import random

    options = ["rock", "paper", "scissors"]
    choice = random.choice(options)
    print("Options:", options)
    print("Random choice:", choice)


def task3_current_date_and_time():
    print("\nTask 3: Current date and time")

    import datetime

    now = datetime.datetime.now()
    print("Raw datetime:", now)

    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")

    print("Date (YYYY-MM-DD):", date_str)
    print("Time (HH:MM):", time_str)


def task4_days_until_new_year():
    print("\nTask 4: Days until New Year")

    import datetime

    today = datetime.date.today()
    year = today.year + 1  # наступний рік

    new_year = datetime.date(year, 1, 1)
    delta = new_year - today

    print("Today:", today)
    print("Next New Year:", new_year)
    print("Days until New Year:", delta.days)


def task5_list_files_in_current_directory():
    print("\nTask 5: List files in current directory")

    import os

    cwd = os.getcwd()
    print("Current working directory:", cwd)

    entries = os.listdir(cwd)
    print("Entries:")
    for name in entries:
        print("-", name)


def task6_check_if_file_exists():
    print("\nTask 6: Check if file exists")

    import os

    filename = input("Enter filename: ")

    if os.path.exists(filename):
        print("File exists")
    else:
        print("File does not exist")


def task7_save_data_to_json_file():
    print("\nTask 7: Save data to JSON file")

    import json

    user = {
        "name": "Andrii",
        "age": 20,
        "city": "Vinnytsia",
    }

    filename = input("Enter JSON filename to save (e.g. user.json): ")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(user, f, ensure_ascii=False, indent=2)

    print(f"User data saved to {filename}")


def task8_load_data_from_json_file():
    print("\nTask 8: Load data from JSON file")

    import json

    filename = input("Enter JSON filename to load: ")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found")
        return
    except json.JSONDecodeError:
        print("Invalid JSON file")
        return

    print("Loaded data:", data)
    print("Keys and values:")
    for key, value in data.items():
        print(f"- {key}: {value}")


def task9_simple_log_with_timestamp():
    print("\nTask 9 (optional): Simple log with timestamp")

    import datetime

    message = input("Enter log message: ")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"

    with open("app.log", "a", encoding="utf-8") as f:
        f.write(line + "\n")

    print("Message appended to app.log")


if __name__ == "__main__":
    task1_random_number_game()
    task2_random_choice_from_list()
    task3_current_date_and_time()
    task4_days_until_new_year()
    task5_list_files_in_current_directory()
    task6_check_if_file_exists()
    task7_save_data_to_json_file()
    task8_load_data_from_json_file()
    task9_simple_log_with_timestamp()
