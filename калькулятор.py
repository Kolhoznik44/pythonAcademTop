""" калькулятор"""

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
    print(f"Результат: {num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"Результат: {num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"Результат: {num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Результат: {num1} / {num2} = {result}")
    else:
        print("Ошибка: Деление на ноль!")
else:
    print("Неверная операция!")