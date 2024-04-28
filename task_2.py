from collections import deque


def is_palindrome(s):
    """
        Необхідно розробити функцію, яка приймає рядок як вхідний параметр,
        додає всі його символи до двосторонньої черги (deque з модуля collections в Python),
        а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом.
        Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів,
        а також бути нечутливою до регістру та пробілів.
    """
    s = s.lower().replace(" ", "")
    queue = deque(s)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True


input_string = input("Введіть рядок: ")
if is_palindrome(input_string):
    print("Рядок - паліндром.")
else:
    print("Рядок - не паліндром.")
