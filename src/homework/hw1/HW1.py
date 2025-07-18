"""
Задание 1
Пользователь вводит с клавиатурытри числа. Необходимо найти сумму чисел, произведение чисел. Результат
вычислений вывести на экран.

# Запрашиваем у пользователя ввод трех чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

# Вычисляем сумму и произведение
sum_result = num1 + num2 + num3
product_result = num1 * num2 * num3

# Выводим результаты на экран
print(f"Сумма чисел: {sum_result}")
print(f"Произведение чисел: {product_result}")
"""
"""
Задание 2
Пользователь вводит с клавиатуры три числа. Первое
число — зарплата за месяц, второе число — сумма месячного платежа по кредиту в банке, третье число — задолженность за коммунальные услуги. Необходимо вывести
на экран сумму, которая останется у пользователя после
всех выплат.


salary = float(input("Введите вашу зарплату за месяц: "))
loan_payment = float(input("Введите сумму месячного платежа по кредиту: "))
utilities_debt = float(input("Введите задолженность за коммунальные услуги: "))

remaining_amount = salary - (loan_payment + utilities_debt)

print(f"Сумма, которая останется у пользователя после всех выплат: {remaining_amount:.2f}")

"""
"""
Задание 3
Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его
диагоналей.


IMMUTABLE_NUMBER = 2
d1 = float(input("Введите длину первой диагонали (d1): "))
d2 = float(input("Введите длину второй диагонали (d2): "))

area = (d1 * d2) / IMMUTABLE_NUMBER

print(f"Площадь ромба с диагоналями {d1} и {d2} равна: {area:.2f}")
""""""
Задание 4
Выведите на экран надпись To be or not to be на разных
строках. Пример вывода:
To be
or not
to be
"""

print("To be\nor not\nto be")

"""
Задание № 5
Выведите на экран надпись «Life is what happens when you're busy making
other plans» John Lennon на разных строках.

print("Life is what happens \n \t when \n \t \tyou're busy making other plans")
"""
def f(s, m):
    if s <= 221:
        return m % 2 == 0
    if m == 0:
        return False
    # Варианты ходов:
    moves = [f(s - 2, m - 1), f(s - 5, m - 1), f(s // 2, m - 1)]
    if m % 2 != 0:
        return any(moves)     # Ход Вани: достаточно найти ОДИН выигрышный
    else:
        return all(moves)     # Ход Пети: все его ходы должны вести к победе Вани

results = []
for S in range(222, 3000):
    # Нет выигрыша за 2 хода (f(s,2) == False)
    # Есть выигрыш на 4-ом ходу (f(s,4) == True)
    if not f(S, 2) and f(S, 4):
        results.append(S)

print(max(results))



