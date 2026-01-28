# Module 12: Projects and Best Practices
# exercises.py
# Міні-проєкти + базові рекомендації з якості коду

print("=== Module 12 Exercises: Projects and Best Practices ===")

# У цьому файлі тільки ОПИС завдань.
# Рішення й прикладні реалізації дивись у solutions.py


# Project 1: To-Do List (консольний застосунок)
# ----------------------------------------------
# Побудуйте простий консольний застосунок «Список справ».
#
# Вимоги:
# 1) Програма показує меню:
#       1. Add task
#       2. View tasks
#       3. Remove task
#       4. Exit
# 2) Зберігає задачі у списку (наприклад, list[str])
# 3) Поки користувач не обрав "Exit", програма повторно показує меню
#
# Best practices:
# - винесіть логіку в окремі функції (show_menu, add_task, view_tasks, remove_task, main)
# - дотримуйтесь зрозумілих імен змінних і функцій
print("\nProject 1: To-Do List (console app)")
# TODO: implement in solutions.py


# Project 2: Number Guessing Game
# -------------------------------
# Реалізуйте гру «Вгадай число»:
#
# Вимоги:
# 1) Комп'ютер «задумує» випадкове число від 1 до 100
# 2) Користувач вводить спроби вгадати число
# 3) Після кожної спроби виводиться:
#       - "Too low", якщо число менше задуманого
#       - "Too high", якщо більше
#       - "You guessed it in X attempts!", якщо вгадав
# 4) Після перемоги запропонуйте зіграти ще раз (Y/N)
#
# Best practices:
# - використовуйте окрему функцію для однієї «гри» (play_game)
# - головний цикл програми в main()
print("\nProject 2: Number Guessing Game")
# TODO: implement in solutions.py


# Project 3: Simple Address Book
# ------------------------------
# Створіть консольний «адресник», який дозволяє керувати контактами.
#
# Вимоги:
# 1) Контакт має поля: name, phone, email
# 2) Програма показує меню:
#       1. Add contact
#       2. View contacts
#       3. Find contact by name
#       4. Exit
# 3) Контакти можна зберігати в списку словників або у файлі JSON (бонус)
#
# Best practices:
# - опишіть контакт як словник або простий клас (бонус)
# - розбийте код на функції: add_contact, view_contacts, find_contact, load/save (бонус)
print("\nProject 3: Simple Address Book")
# TODO: implement in solutions.py


# Task 4: Code Style Cleanup
# --------------------------
# Візьміть один зі своїх старих коротких скриптів (наприклад, з попередніх модулів)
# і:
# 1) перейменуйте змінні на більш зрозумілі (user_input замість x тощо)
# 2) додайте порожні рядки між логічними блоками
# 3) додайте коментарі там, де логіка неочевидна
#
# Best practices:
# - спробуйте триматися стилю PEP 8: імена в snake_case, довжина рядка ≤ 79 символів
#
# (Цю вправу ви робите у власному файлі / окремому проєкті; тут лише нагадування.)
print("\nTask 4: Code Style Cleanup (self-practice)")
# TODO: do in your own script


# Task 5: Refactor into Functions
# -------------------------------
# Візьміть скрипт, у якому багато коду в глобальній області (без функцій),
# і:
# 1) виділіть окремі частини в функції (наприклад, get_input, process_data, print_result)
# 2) залиште внизу лише:
#       if __name__ == \"__main__\":
#           main()
#
# (Завдання також виконується у вашому власному файлі.)
print("\nTask 5: Refactor into Functions (self-practice)")
# TODO: do in your own script


# Project 6 (optional): Small Combined Project
# -------------------------------------------
# (Складніший проєкт, якщо хочеться практики)
#
# Ідея:
# - поєднайте кілька концепцій у одному застосунку, наприклад:
#   «Менеджер нотаток»:
#       - збереження нотаток у файлі (module_08)
#       - використання класу Note / NoteManager (module_09)
#       - просте меню для керування нотатками
#
# Тут достатньо опису; реалізація в solutions.py як приклад.
print("\nProject 6 (optional): Small Combined Project")
# TODO: implement in solutions.py
