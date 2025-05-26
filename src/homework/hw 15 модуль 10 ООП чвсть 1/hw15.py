"""
Задание 1
Реализуйте класс «Автомобиль». Необходимо хранить
в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.


class Car:
    def __init__(self):
        self.model = ""
        self.year = 0
        self.manufacturer = ""
        self.engine_volume = 0.0
        self.color = ""
        self.price = 0.0

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

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_manufacturer(self):
        return self.manufacturer

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_engine_volume(self):
        return self.engine_volume

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

car = Car()
car.input_data()
car.display_data()


print("Год выпуска:", car.get_year())
car.set_price(1500000)
print("Новая цена:", car.get_price())
"""

"""
Реализуйте класс «Книга». Необходимо хранить в
полях класса: название книги, год выпуска, издателя,
жанр, автора, цену. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса



class Book:
    __title = str()
    __year = 1970
    __publisher = str()
    __genre = str()
    __autor = str()
    __price = 0.0

    def __init__(self,  title : str = "Название",
                        autor : str = "Автор",
                        genre : str = "Жанр",
                        year : int = 1970,
                        publisher : str = "Издание",
                        price : float = 0.0
                 ):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__autor = autor
        self.__price = price

    def __del__(self):
        pass

    def input_data(self,
                        title : str = None,
                        autor : str = None,
                        genre : str = None,
                        year : int = None,
                        publisher : str = None,
                        price : float = None
                 ):
        self.__title = title if title != None else self.__title
        self.__year = year if year != None else self.__year
        self.__publisher = publisher if publisher != None else self.__publisher
        self.__genre = genre if genre != None else self.__genre
        self.__autor = autor if autor != None else self.__autor
        self.__price = price if price != None else self.__price

    def get_data(self):
        return (f"{self.__autor} - {self.__title}\n"
                f"Жанр: {self.__genre}\tГод: {self.__year}\n"
                f"Издание: {self.__publisher}\tЦена: {self.__price}")

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor : str = None):
        if autor != None:
            self.__autor = autor

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str = None):
        if title != None:
            self.__title = title

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str = None):
        if year != None:
            self.__year = year

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: str = None):
        if price != None:
            self.__price = price

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre: str = None):
        if genre != None:
            self.__genre = genre

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str = None):
        if publisher != None:
            self.__publisher = publisher

    def input_from_console(self):

        self.title = input("Введите название книги: ")
        self.autor = input("Введите автора: ")
        self.genre = input("Введите жанр: ")
        self.year = int(input("Введите год: "))
        self.publisher = input("Введите издательство: ")
        self.price = float(input("Введите цену: "))


    def __str__(self):
        return self.get_data()

if __name__ == "__main__":
    book = Book()
    book.input_from_console()
    print(book)
    print("Автор:", book.autor)
    book.price = 999.99
    print("Новая цена книги:", book.price)

"""

"""
Реализуйте класс «Стадион». Необходимо хранить в
полях класса: название стадиона, дату открытия, страну,
город, вместимость. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса.

"""

class Stadium:
    def __init__(self, name='', date_opened='', country='', city='', capacity=0):
        self.__name = name
        self.__date_opened = date_opened
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    # Метод для ввода данных
    def set_data(self):
        self.__name = input("Введите название стадиона: ")
        self.__date_opened = input("Введите дату открытия: ")
        self.__country = input("Введите страну: ")
        self.__city = input("Введите город: ")
        self.__capacity = int(input("Введите вместимость: "))

    # Метод для вывода данных
    def get_data(self):
        return (f"Стадион: {self.__name}\n"
                f"Дата открытия: {self.__date_opened}\n"
                f"Страна: {self.__country}\n"
                f"Город: {self.__city}\n"
                f"Вместимость: {self.__capacity}")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_date_opened(self):
        return self.__date_opened

    def set_date_opened(self, date_opened):
        self.__date_opened = date_opened

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def __str__(self):
        return self.get_data()

if __name__ == '__main__':
    stadium = Stadium()
    stadium.set_data()
    print("\nИнформация о стадионе:")
    print(stadium)