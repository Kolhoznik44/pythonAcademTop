"""
Задание 1
Написать рекурсивную функцию нахождения наибольшего общего делителя двух целых чисел.

"""
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

num1 = 48
num2 = 18
result = gcd(num1, num2)
print(f"Наибольший общий делитель {num1} и {num2} равен {result}")

"""

"""