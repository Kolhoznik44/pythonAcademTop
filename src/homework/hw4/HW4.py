"""
Задание 1
Напишите функцию, которая отображает на экран
форматированный текст, указанный ниже:
“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.”
Bill Gates
"""

def display_quote():
    quote = (
        "Don't compare yourself with anyone in this world...\n"
        "if you do so, you are insulting yourself."
    )
    author = "Bill Gates"

    print(quote)
    print(author)

display_quote()



""""
Задание 2
Напишите функцию, которая принимает два числа
в качестве параметра и отображает все четные числа
между ними.

"""
def print_even_numbers(start, end):

    if start > end:
        start, end = end, start

    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print_even_numbers(num1, num2)


"""
Задание 3
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.
"""

def draw_square(size, char, filled):
    if size <= 0:
        print("Длина стороны квадрата должна быть положительным числом.")
        return

    if filled:

        for i in range(size):
            print(char * size)
    else:

        for i in range(size):
            if i == 0 or i == size - 1:
                print(char * size)
            else:
                print(char + ' ' * (size - 2) + char)


side_length = int(input("Введите длину стороны квадрата: "))
symbol = input("Введите символ: ")
is_filled = input("Квадрат заполненный? (да/нет): ").strip().lower() == 'да'

draw_square(side_length, symbol, is_filled)


"""
Задание 4
Напишите функцию, которая возвращает минимальное
из пяти чисел. Числа передаются в качестве параметров.
"""
def find_minimum(a, b, c, d, e):

    return min(a, b, c, d, e)


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))
num4 = float(input("Введите четвертое число: "))
num5 = float(input("Введите пятое число: "))

minimum_value = find_minimum(num1, num2, num3, num4, num5)
print(f"Минимальное число из введенных: {minimum_value}")

"""
Задание 5
Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапазона перепутаны ( например 5 - верхняя граница, 25 -нижняя граница),
их нужно поменять местами.

"""


def product_in_range(lower, upper):

    if lower > upper:
        lower, upper = upper, lower


    product = 1


    for number in range(lower, upper + 1):
        product *= number

    return product



lower_bound = int(input("Введите нижнюю границу диапазона: "))
upper_bound = int(input("Введите верхнюю границу диапазона: "))

result = product_in_range(lower_bound, upper_bound)
print(f"Произведение чисел в диапазоне от {lower_bound} до {upper_bound}: {result}")

"""
Задание 6
Напишите функцию, которая считает количество
цифр в числе. Число передаётся в качестве параметра. Из
функции нужно вернуть полученное количество цифр.
Например, если передали 3456, количество цифр будет 4.
"""
def count_digits(number):

    return len(str(abs(number)))


number = int(input("Введите число: "))
result = count_digits(number)
print(f"Количество цифр в числе {number}: {result}")


"""
Задание 7
Напишите функцию, которая проверяет является ли
число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
true, иначе false.
«Палиндром» — это число, у которого первая часть
цифр равна второй перевернутой части цифр. Например,
123321—палиндром(первая часть 123, вторая 321, которая
после переворота становится 123), 546645 — палиндром,
а 421987 — не палиндром. 
"""


def is_palindrome(number):

    str_number = str(number)

    return str_number == str_number[::-1]

number = int(input("Введите число: "))
result = is_palindrome(number)
if result:
    print(f"Число {number} является палиндромом.")
else:
    print(f"Число {number} не является палиндромом.")