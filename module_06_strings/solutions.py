# Module 06: Strings
# solutions.py
# Розв'язки до вправ з exercises.py

print("=== Module 06 Solutions: Strings ===")


def task1_basic_string_info():
    print("\nTask 1: Basic string info")
    text = input("Enter a string: ")

    print("Length:", len(text))
    print("Upper:", text.upper())
    print("Lower:", text.lower())


def task2_trim_spaces():
    print("\nTask 2: Trim spaces")
    text = input("Enter a string with spaces: ")

    print(f'Original: "{text}"')
    trimmed = text.strip()
    print(f'Trimmed:  "{trimmed}"')


def task3_count_vowels():
    print("\nTask 3: Count vowels")
    text = input("Enter a string: ")
    vowels = "aeiouy"
    count = 0

    for ch in text.lower():
        if ch in vowels:
            count += 1

    print("Vowel count:", count)


def task4_replace_word():
    print("\nTask 4: Replace word")

    text = "Python is hard, but Python is fun"
    print("Original:", text)

    new_text = text.replace("Python", "JavaScript")
    print("Modified:", new_text)


def task5_split_and_join():
    print("\nTask 5: Split and join")

    text = "Python is fun and powerful"
    print("Original:", text)

    words = text.split()
    print("Words:", words)

    result = "-".join(words)
    print("Joined with '-':", result)


def task6_simple_email_validator():
    print("\nTask 6: Simple email validator (basic)")
    email = input("Enter email: ")

    at_index = email.find("@")

    if at_index == -1:
        print("Invalid email")
        return

    dot_index = email.find(".", at_index)

    if dot_index == -1:
        print("Invalid email")
    else:
        print("Valid email")


def task7_palindrome_checker():
    print("\nTask 7: Palindrome checker")
    text = input("Enter a string: ")

    cleaned = text.replace(" ", "").lower()
    reversed_text = cleaned[::-1]

    if cleaned == reversed_text:
        print("Palindrome")
    else:
        print("Not a palindrome")


def task8_character_frequency():
    print("\nTask 8 (optional): Character frequency")
    text = input("Enter a string: ")

    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    print("Character frequency:")
    for ch, count in freq.items():
        print(f"'{ch}' -> {count}")


if __name__ == "__main__":
    task1_basic_string_info()
    task2_trim_spaces()
    task3_count_vowels()
    task4_replace_word()
    task5_split_and_join()
    task6_simple_email_validator()
    task7_palindrome_checker()
    task8_character_frequency()
