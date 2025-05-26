"""
Задание 1
К уже реализованному классу «Автомобиль» добавьте
конструктор, а также необходимые перегруженныеметоды.


class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
        self._model = model
        self._year = year
        self._manufacturer = manufacturer
        self._engine_volume = engine_volume
        self._color = color
        self._price = price

    def input_data(self):
        self.model = input("Введите название модели: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_volume = float(input("Введите объем двигателя (л): "))
        self.color = input("Введите цвет машины: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume} л")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.price} руб.")

    def __str__(self):
        return (f"Модель: {self.model}\n"
                f"Год выпуска: {self.year}\n"
                f"Производитель: {self.manufacturer}\n"
                f"Объем двигателя: {self.engine_volume} л\n"
                f"Цвет: {self.color}\n"
                f"Цена: {self.price} руб.")

    def __eq__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return (self.model == other.model and
                self.year == other.year and
                self.manufacturer == other.manufacturer and
                self.engine_volume == other.engine_volume and
                self.color == other.color and
                self.price == other.price)

    def __lt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.price < other.price

    def __add__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.price + other.price

    # Свойства property
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value

    @property
    def engine_volume(self):
        return self._engine_volume

    @engine_volume.setter
    def engine_volume(self, value):
        self._engine_volume = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

if __name__ == "__main__":
    car1 = Car("Ford Focus", 2017, "Ford", 1.6, "синий", 1200000)
    car2 = Car()
    car2.input_data()
    print("\nИнформация о car1:")
    print(car1)
    print("\nИнформация о car2:")
    car2.display_data()

    print("Кар1 == Кар2?", car1 == car2)
    print("Цена car1 < Цена car2?", car1 < car2)
    print("Сумма цен:", car1 + car2)
"""

"""
Задание 2
К уже реализованному классу «Книга» добавьте конструктор, а также необходимые перегруженные методы.

class Book:
    def __init__(self,
                 title: str = "Название",
                 autor: str = "Автор",
                 genre: str = "Жанр",
                 year: int = 1970,
                 publisher: str = "Издание",
                 price: float = 0.0
                 ):
        self._title = title
        self._year = year
        self._publisher = publisher
        self._genre = genre
        self._autor = autor
        self._price = price

    def input_data(self,
                   title: str = None,
                   autor: str = None,
                   genre: str = None,
                   year: int = None,
                   publisher: str = None,
                   price: float = None
                 ):
        if title is not None:
            self.title = title
        if autor is not None:
            self.autor = autor
        if genre is not None:
            self.genre = genre
        if year is not None:
            self.year = year
        if publisher is not None:
            self.publisher = publisher
        if price is not None:
            self.price = price

    def input_from_console(self):
        self.title = input("Введите название книги: ")
        self.autor = input("Введите автора: ")
        self.genre = input("Введите жанр: ")
        self.year = int(input("Введите год: "))
        self.publisher = input("Введите издательство: ")
        self.price = float(input("Введите цену: "))

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __str__(self):
        return (f"{self.autor} - {self.title}\n"
                f"Жанр: {self.genre}\tГод: {self.year}\n"
                f"Издание: {self.publisher}\tЦена: {self.price}")

    # Перегрузка операторов
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title == other.title and
                self.autor == other.autor and
                self.year == other.year and
                self.publisher == other.publisher and
                self.genre == other.genre and
                self.price == other.price)

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price < other.price

    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price + other.price

if __name__ == "__main__":
    book1 = Book()
    book1.input_from_console()
    print("\nКнига 1:")
    print(book1)
    print("Автор:", book1.autor)
    book1.price = 999.99
    print("Новая цена книги:", book1.price)

    book2 = Book("Шерлок Холмс", "Артур Конан Дойл", "Детектив", 1887, "Penguin Books", 500.0)
    print("\nКнига 2:")
    print(book2)
    print("Сравнить по цене: Книга1 < Книга2 :", book1 < book2)
    print("Суммарная цена двух книг:", book1 + book2)
    print("Книги одинаковые:", book1 == book2)
"""

"""
Задание 3
К уже реализованному классу «Стадион» добавьте
конструктор, а также необходимые перегруженныеметоды.

"""

class Stadium:
    def __init__(self, name='', date_opened='', country='', city='', capacity=0):
        self._name = name
        self._date_opened = date_opened
        self._country = country
        self._city = city
        self._capacity = capacity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def date_opened(self):
        return self._date_opened

    @date_opened.setter
    def date_opened(self, date_opened):
        self._date_opened = date_opened

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    def set_data(self):
        self.name = input("Введите название стадиона: ")
        self.date_opened = input("Введите дату открытия: ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость: "))

    def get_data(self):
        return (f"Стадион: {self.name}\n"
                f"Дата открытия: {self.date_opened}\n"
                f"Страна: {self.country}\n"
                f"Город: {self.city}\n"
                f"Вместимость: {self.capacity}")

    # Перегрузка оператора == (равенство по вместимости)
    def __eq__(self, other):
        if isinstance(other, Stadium):
            return self.capacity == other.capacity
        return NotImplemented

    def __str__(self):
        return self.get_data()

if __name__ == '__main__':
    stadium = Stadium()
    stadium.set_data()
    print("\nИнформация о стадионе:")
    print(stadium)