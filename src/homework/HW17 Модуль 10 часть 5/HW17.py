"""
Задание 1
Создайте класс Circle (окружность). Для данного
класса реализуйте ряд перегруженных операторов:
■ Проверка на равенство радиусов двух окружностей
(операция = =);
■ Сравнения длин двух окружностей (операции >, <,
<=,>=);
■ Пропорциональное изменение размеров окружности,
путем изменения ее радиуса (операции + - += -=).


import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self.radius = radius

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return math.isclose(self.radius, other.radius)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.circumference < other.circumference
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.circumference <= other.circumference
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.circumference > other.circumference
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.circumference >= other.circumference
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius - value)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            self.radius -= value
            return self
        return NotImplemented

    def __str__(self):
        return f"Circle(radius={self.radius:.2f})"

if __name__ == "__main__":
    c1 = Circle(5)
    c2 = Circle(7)
    print("c1 == c2:", c1 == c2)
    print("c1 > c2:", c1 > c2)
    print("c1 < c2:", c1 < c2)

    c3 = c1 + 3
    print("c3 (c1 + 3):", c3)

    c3 -= 2
    print("c3 после -= 2:", c3)

    c3 += 10
    print("c3 после += 10:", c3)

"""

"""
Задание 2
Создайте класс Complex (комплексное число).
Создайте перегруженные операторы для реализации
арифметических операций для по работе с комплексными
числами (операции +, -, *, /).

class Complex:
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, (int, float)):
            return Complex(self.real + other, self.imag)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, (int, float)):
            return Complex(self.real - other, self.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return Complex(real, imag)
        elif isinstance(other, (int, float)):
            return Complex(self.real * other, self.imag * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denom = other.real ** 2 + other.imag ** 2
            if denom == 0:
                raise ZeroDivisionError("Деление на ноль")
            real = (self.real * other.real + self.imag * other.imag) / denom
            imag = (self.imag * other.real - self.real * other.imag) / denom
            return Complex(real, imag)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль")
            return Complex(self.real / other, self.imag / other)
        return NotImplemented

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

    __repr__ = __str__


if __name__ == "__main__":
    a = Complex(2, 3)
    b = Complex(1, -4)
    print("a = ", a)
    print("b = ", b)
    print("a + b = ", a + b)
    print("a - b = ", a - b)
    print("a * b = ", a * b)
    print("a / b = ", a / b)
    print("a + 5 = ", a + 5)
    print("a * 3 = ", a * 3)

"""
"""
Вам необходимо создать класс Airplane (самолет). 
С помощью перегрузки операторов реализовать:
■ Проверка на равенство типов самолетов (операция
= =);
■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >
< <= >=).

class Airplane:
    def __init__(self, airplane_type, max_passengers, passengers=0):
        self.airplane_type = airplane_type          # тип самолета (строка)
        self.max_passengers = max_passengers        # максимальная вместимость
        self.passengers = passengers                # текущие пассажиры

    # Проверка на равенство типов самолетов (==)
    def __eq__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.airplane_type == other.airplane_type

    # Увеличение (+)
    def __add__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        # Создаем новый объект, не меняя старый
        new_passengers = min(self.passengers + value, self.max_passengers)
        return Airplane(self.airplane_type, self.max_passengers, new_passengers)

    # Уменьшение (-)
    def __sub__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        # Создаем новый объект, не меняя старый
        new_passengers = max(self.passengers - value, 0)
        return Airplane(self.airplane_type, self.max_passengers, new_passengers)

    # +=
    def __iadd__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        self.passengers = min(self.passengers + value, self.max_passengers)
        return self

    # -=
    def __isub__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        self.passengers = max(self.passengers - value, 0)
        return self

    # Сравнение по максимальному количеству пассажиров
    def __lt__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.max_passengers >= other.max_passengers

    # Красивое строковое представление
    def __str__(self):
        return f"Airplane(type='{self.airplane_type}', max={self.max_passengers}, now={self.passengers})"

    if __name__ == "__main__":
        a1 = Airplane("Boeing 737", 200, 50)
        a2 = Airplane("Airbus A320", 180, 120)
        a3 = Airplane("Boeing 737", 215, 200)

        # Проверка равенства типов
        print(a1 == a2)  # False
        print(a1 == a3)  # True

        # Добавление и убавление пассажиров
        a4 = a1 + 30
        print(a4)  # 80 пассажиров
        a5 = a4 - 100
        print(a5)  # 0 пассажиров

        # += -=
        a2 += 50
        print(a2)  # 170 пассажиров (максимум — 180)
        a2 -= 200
        print(a2)  # 0 пассажиров

        # Сравнение по максимальной вместимости
        print(a1 > a2)  # True (200 > 180)
        print(a1 <= a3)  # True (200 <= 215)

"""

"""
Задание 4
Создать класс Flat (квартира). Реализовать перегруженные операторы:
■ Проверка на равенство площадей квартир (операция
==);
■ Проверка на неравенство площадей квартир (операция !=);
■ Сравнение двух квартир по цене (операции > < <= >=)
"""


class Flat:
    def __init__(self, area, price):
        self.area = area  # Площадь квартиры
        self.price = price  # Цена квартиры

    # Проверка на равенство площадей
    def __eq__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.area == other.area

    # Проверка на неравенство площадей
    def __ne__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.area != other.area

    # Сравнение по цене
    def __lt__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.price < other.price

    def __le__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.price <= other.price

    def __gt__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.price > other.price

    def __ge__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.price >= other.price

    def __str__(self):
        return f"Квартира: {self.area} кв.м, цена {self.price} руб."


if __name__ == "__main__":
    f1 = Flat(60, 5000000)
    f2 = Flat(45, 3500000)
    f3 = Flat(60, 5200000)

    print(f1 == f2)  # False (разные площади)
    print(f1 == f3)  # True (одинаковые площади)
    print(f1 != f2)  # True

    print(f2 < f1)  # True (по цене)
    print(f3 >= f1)  # True (по цене)
    print(f3 > f2)  # True (по цене)
    print(f1 <= f3)  # True (по цене)