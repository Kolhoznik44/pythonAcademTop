"""
Задание 1:
Пользователь вводит с клавиатуры арифметическое
выражение. Например, 23+12.
Необходимо вывести на экран результат выражения.
В нашем примере это 35. Арифметическое выражение
может состоять только из трёх частей: число, операция,
число. Возможные операции: +, -,*,/

"""
expression = input("Введите арифметическое выражение в формате 'число оператор число' (например, 23 + 12): ")

parsed_input = expression.split()
if len(parsed_input) != 3:
    print("Некорректный формат ввода. Пожалуйста, используйте формат 'число оператор число'.")
else:
    num1, operator, num2 = parsed_input

    num1 = int(num1)
    num2 = int(num2)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Некорректная операция")
        result = None

    if result is not None:
        print("Результат:", result)


"""
Задание 2:
В списке целых, заполненном случайными числами,
определить минимальный и максимальный элементы,
посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
количество нулей. Результаты вывести на экран.

"""

import random

random_list = [random.randint(-10, 10) for i in range(20)]
print("Исходный список:", random_list)

min_elem = min(random_list)
max_elem = max(random_list)

negatives = sum(1 for num in random_list if num < 0)
positives = sum(1 for num in random_list if num > 0)
zeros = sum(1 for num in random_list if num == 0)

print("Минимальный элемент:", min_elem)
print("Максимальный элемент:", max_elem)
print("Количество отрицательных элементов:", negatives)
print("Количество положительных элементов:", positives)
print("Количество нулей:", zeros)