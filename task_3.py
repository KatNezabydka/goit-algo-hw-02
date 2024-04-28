def check_delimiters(expression):
    """
        Напишіть програму, яка читає рядок з послідовністю символів-розділювачів,
        наприклад, ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, коли розділювачі симетричні, несиметричні,
        наприклад ( ( ( ) , або коли розділювачі різних видів стоять у парі, як-от ( }
    """
    stack = []

    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return "Несиметричні розділювачі"
            stack.pop()

    if not stack:
        return "Симетричні розділювачі"
    else:
        return "Несиметричні розділювачі"


input_string = input("Введіть рядок з послідовністю символів-розділювачів: ")
print(check_delimiters(input_string))
