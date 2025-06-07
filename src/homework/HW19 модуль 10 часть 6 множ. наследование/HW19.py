"""
Задание 1
Создать базовый класс Фигура с методом для подсчета
площади. Создать производные классы: прямоугольник,
круг, прямоугольный треугольник, трапеция со своими
методами для подсчета площади.

import math

# Базовый класс Фигура
class Figure:
    def area(self):
        raise NotImplementedError("Метод area должен быть переопределен!")

# Миксин для печати площади
class Printable:
    def print_area(self):
        print(f"Площадь фигуры ({self.__class__.__name__}): {self.area()}")

# Прямоугольник (множественное наследование: Figure + Printable)
class Rectangle(Figure, Printable):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Круг
class Circle(Figure, Printable):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Прямоугольный треугольник
class RightTriangle(Figure, Printable):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Трапеция
class Trapezoid(Figure, Printable):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return (self.base1 + self.base2) * self.height / 2

figures = [
    Rectangle(3, 5),
    Circle(4),
    RightTriangle(3, 6),
    Trapezoid(3, 5, 4)
]

for figure in figures:
    figure.print_area()

"""
"""
Задание 2
Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает
информацию о фигуре).


import math

class Figure:
    def area(self):
        raise NotImplementedError("Метод area должен быть переопределен!")

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Фигура типа {self.__class__.__name__}"

class Printable:
    def print_area(self):
        print(f"Площадь фигуры ({self.__class__.__name__}): {self.area()}")

class Rectangle(Figure, Printable):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Прямоугольник: ширина={self.width}, высота={self.height}, площадь={self.area()}"

class Circle(Figure, Printable):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Круг: радиус={self.radius}, площадь={self.area()}"

class RightTriangle(Figure, Printable):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Прямоугольный треугольник: основание={self.base}, высота={self.height}, площадь={self.area()}"

class Trapezoid(Figure, Printable):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return (self.base1 + self.base2) * self.height / 2

    def __str__(self):
        return f"Трапеция: основание1={self.base1}, основание2={self.base2}, высота={self.height}, площадь={self.area()}"

# Проверка:

figures = [
    Rectangle(3, 5),
    Circle(4),
    RightTriangle(3, 6),
    Trapezoid(3, 5, 4)
]

for f in figures:
    print(str(f))
    print(f"Целое значение площади: {int(f)}\n")
"""

"""
Задание 3
Создайте базовый класс Shape для рисования плоских
фигур.
Определите методы:
■ Show() — вывод на экран информации о фигуре;
■ Save() — сохранение фигуры в файл;
■ Load() — считывание фигуры из файла.
Определите производные классы:
■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
■ Circle — окружность с заданными координатами центра и радиусом;
■ Ellipse — эллипс с заданными координатами верхнего
угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат, и размерами
этого прямоугольника.
Создайте список фигур, сохраните фигуры в файл,
загрузите в другой список и отобразите информацию о
каждой из фигур.
"""
import json

class Shape:
    def __init__(self, name):
        self.name = name

    def Show(self):
        print(f"Фигура: {self.name}")

    def Save(self, file):
        json.dump(self.to_dict(), file)
        file.write('\n')

    @classmethod
    def Load(cls, file):
        data = json.loads(file.readline())
        type_ = data['type']
        if type_ == 'Square':
            return Square.from_dict(data)
        elif type_ == 'Rectangle':
            return Rectangle.from_dict(data)
        elif type_ == 'Circle':
            return Circle.from_dict(data)
        elif type_ == 'Ellipse':
            return Ellipse.from_dict(data)
        else:
            raise ValueError("Неизвестный тип фигуры")

    def to_dict(self):
        return {'type': self.__class__.__name__, 'name': self.name}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'])

class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__("Квадрат")
        self.x = x
        self.y = y
        self.side = side

    def Show(self):
        print(f"{self.name}: левый верхний угол ({self.x}, {self.y}), сторона={self.side}")

    def to_dict(self):
        d = super().to_dict()
        d.update({'x': self.x, 'y': self.y, 'side': self.side})
        return d

    @classmethod
    def from_dict(cls, data):
        return Square(data['x'], data['y'], data['side'])

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__("Прямоугольник")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"{self.name}: левый верхний угол ({self.x}, {self.y}), ширина={self.width}, высота={self.height}")

    def to_dict(self):
        d = super().to_dict()
        d.update({'x': self.x, 'y': self.y, 'width': self.width, 'height': self.height})
        return d

    @classmethod
    def from_dict(cls, data):
        return Rectangle(data['x'], data['y'], data['width'], data['height'])

class Circle(Shape):
    def __init__(self, cx, cy, radius):
        super().__init__("Окружность")
        self.cx = cx
        self.cy = cy
        self.radius = radius

    def Show(self):
        print(f"{self.name}: центр ({self.cx}, {self.cy}), радиус={self.radius}")

    def to_dict(self):
        d = super().to_dict()
        d.update({'cx': self.cx, 'cy': self.cy, 'radius': self.radius})
        return d

    @classmethod
    def from_dict(cls, data):
        return Circle(data['cx'], data['cy'], data['radius'])

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__("Эллипс")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"{self.name}: описывающий прямоугольник левый верхний угол ({self.x}, {self.y}), ширина={self.width}, высота={self.height}")

    def to_dict(self):
        d = super().to_dict()
        d.update({'x': self.x, 'y': self.y, 'width': self.width, 'height': self.height})
        return d

    @classmethod
    def from_dict(cls, data):
        return Ellipse(data['x'], data['y'], data['width'], data['height'])


# Создаём список фигур
figures = [
    Square(1, 2, 10),
    Rectangle(3, 4, 15, 5),
    Circle(12, 8, 7),
    Ellipse(5, 5, 14, 6)
]

# Сохраняем фигуры в файл
with open('shapes.txt', 'w', encoding='utf-8') as f:
    for fig in figures:
        fig.Save(f)

# Загружаем фигуры из файла в другой список
loaded_figures = []
with open('shapes.txt', 'r', encoding='utf-8') as f:
    for _ in range(4):
        loaded_figures.append(Shape.Load(f))

# Отображаем информацию о фигурах
for fig in loaded_figures:
    fig.Show()