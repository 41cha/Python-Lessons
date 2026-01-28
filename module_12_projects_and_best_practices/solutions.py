# Module 12: Projects and Best Practices
# solutions.py
# Прикладні реалізації міні-проєктів + простий рефакторинг/структура

print("=== Module 12 Solutions: Projects and Best Practices ===")


# -----------------------------
# Project 1: To-Do List (console app)
# -----------------------------
def show_todo_menu():
    print("\nTo-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if not task:
        print("Task cannot be empty")
        return
    tasks.append(task)
    print("Task added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    print("Your tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    choice_str = input("Enter task number to remove: ")

    try:
        choice = int(choice_str)
    except ValueError:
        print("Invalid number")
        return

    if 1 <= choice <= len(tasks):
        removed = tasks.pop(choice - 1)
        print(f"Removed: {removed}")
    else:
        print("No task with that number")


def todo_main():
    print("\nProject 1: To-Do List (console app)")
    tasks = []

    while True:
        show_todo_menu()
        option = input("Choose option (1-4): ").strip()

        if option == "1":
            add_task(tasks)
        elif option == "2":
            view_tasks(tasks)
        elif option == "3":
            remove_task(tasks)
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


# -----------------------------
# Project 2: Number Guessing Game
# -----------------------------
def play_game():
    import random

    secret = random.randint(1, 100)
    attempts = 0

    print("I guessed a number between 1 and 100. Try to guess it!")

    while True:
        guess_str = input("Your guess: ")

        try:
            guess = int(guess_str)
        except ValueError:
            print("Please enter an integer.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"You guessed it in {attempts} attempts!")
            break


def guessing_game_main():
    print("\nProject 2: Number Guessing Game")

    while True:
        play_game()
        again = input("Play again? (Y/N): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


# -----------------------------
# Project 3: Simple Address Book
# -----------------------------
def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    if not name:
        print("Name cannot be empty")
        return

    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts yet.")
        return

    print("Contacts:")
    for index, c in enumerate(contacts, start=1):
        print(f"{index}. {c['name']} - {c['phone']} - {c['email']}")


def find_contact(contacts):
    if not contacts:
        print("No contacts yet.")
        return

    search = input("Enter name to find: ").strip().lower()
    found = []

    for c in contacts:
        if search in c["name"].lower():
            found.append(c)

    if not found:
        print("No contacts found.")
    else:
        print("Found contacts:")
        for c in found:
            print(f"- {c['name']} - {c['phone']} - {c['email']}")


def address_book_main():
    print("\nProject 3: Simple Address Book")

    contacts = []

    while True:
        print("\nAddress Book")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Find contact by name")
        print("4. Exit")

        choice = input("Choose option (1-4): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            find_contact(contacts)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


# -----------------------------
# Project 6 (optional): Small Combined Project
# Example: Note Manager with file persistence
# -----------------------------
import json
import os


class Note:
    def __init__(self, title, body):
        self.title = title
        self.body = body


class NoteManager:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if not os.path.exists(self.filename):
            self.notes = []
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            self.notes = []
            return

        self.notes = [Note(item["title"], item["body"]) for item in data]

    def save_notes(self):
        data = [{"title": n.title, "body": n.body} for n in self.notes]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_note(self, title, body):
        self.notes.append(Note(title, body))
        self.save_notes()
        print("Note added.")

    def list_notes(self):
        if not self.notes:
            print("No notes yet.")
            return

        for index, note in enumerate(self.notes, start=1):
            print(f"{index}. {note.title}")

    def show_note(self, index):
        if 1 <= index <= len(self.notes):
            note = self.notes[index - 1]
            print(f"Title: {note.title}")
            print("Body:")
            print(note.body)
        else:
            print("Invalid note number")

    def delete_note(self, index):
        if 1 <= index <= len(self.notes):
            removed = self.notes.pop(index - 1)
            self.save_notes()
            print(f"Deleted note: {removed.title}")
        else:
            print("Invalid note number")


def note_manager_main():
    print("\nProject 6 (optional): Note Manager")

    manager = NoteManager()

    while True:
        print("\nNote Manager")
        print("1. Add note")
        print("2. List notes")
        print("3. View note")
        print("4. Delete note")
        print("5. Exit")

        choice = input("Choose option (1-5): ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            body = input("Body: ").strip()
            manager.add_note(title, body)
        elif choice == "2":
            manager.list_notes()
        elif choice == "3":
            num_str = input("Note number: ")
            try:
                num = int(num_str)
            except ValueError:
                print("Invalid number")
                continue
            manager.show_note(num)
        elif choice == "4":
            num_str = input("Note number to delete: ")
            try:
                num = int(num_str)
            except ValueError:
                print("Invalid number")
                continue
            manager.delete_note(num)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    # Тут можна запускати будь-який із проєктів для демонстрації
    todo_main()
    guessing_game_main()
    address_book_main()
    note_manager_main()
