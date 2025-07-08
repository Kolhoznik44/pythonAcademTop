"""Модуль 8. Упаковка данных
Тема: Упаковка данных. Часть 1
Задание 1
Есть некоторый словарь, который хранит названия
стран и столиц. Название страны используется в качестве
ключа, название столицыв качестве значения. Необходимо
реализовать: добавление данных, удаление данных, поиск
данных, редактирование данных, сохранение и загрузку
данных (используя упаковку и распаковку)."""

"""import pickle

# Исходный словарь стран и столиц
country_capital = {}

def add_country(country, capital):
    country_capital[country] = capital
    print(f'Добавлено: {country} - {capital}')

def delete_country(country):
    if country in country_capital:
        del country_capital[country]
        print(f'Удалено: {country}')
    else:
        print('Страна не найдена!')

def find_country(country):
    capital = country_capital.get(country)
    if capital:
        print(f'Столица страны {country}: {capital}')
    else:
        print('Страна не найдена!')

def edit_country(country, new_capital):
    if country in country_capital:
        country_capital[country] = new_capital
        print(f'Столица страны {country} изменена на {new_capital}')
    else:
        print('Страна не найдена!')

def save_data(filename):
    with open(filename, 'wb') as f:
        pickle.dump(country_capital, f)
    print('Данные сохранены!')

def load_data(filename):
    global country_capital
    with open(filename, 'rb') as f:
        country_capital = pickle.load(f)
    print('Данные загружены!')

# Пример использования функций:
add_country("Россия", "Москва")
add_country("Франция", "Париж")
add_country("Япония", "Токио")
find_country("Россия")
edit_country("Франция", "Париж2")
delete_country("Япония")

save_data("countries.pkl")
country_capital.clear()  # Очистим данные для проверки загрузки
load_data("countries.pkl")
print(country_capital)
"""

"""Задание 2
Есть некоторый словарь, который хранит названия
музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
альбомов в качестве значения. Необходимо реализовать:
добавление данных, удаление данных, поиск данных,
редактирование данных, сохранение и загрузку данных
(используя упаковку и распаковку)."""

import pickle

# Изначально пустой словарь
bands = {}  # группа : [альбом1, альбом2, ...]

def add_band(band, albums):
    bands[band] = albums
    print(f'Добавлено: {band} - {albums}')

def delete_band(band):
    if band in bands:
        del bands[band]
        print(f'Удалено: {band}')
    else:
        print('Группа не найдена!')

def find_band(band):
    albums = bands.get(band)
    if albums:
        print(f'Альбомы группы {band}: {albums}')
    else:
        print('Группа не найдена!')

def edit_band(band, new_albums):
    if band in bands:
        bands[band] = new_albums
        print(f'Альбомы группы {band} изменены на {new_albums}')
    else:
        print('Группа не найдена!')

def save_data(filename):
    with open(filename, 'wb') as f:
        pickle.dump(bands, f)
    print('Данные сохранены!')

def load_data(filename):
    global bands
    with open(filename, 'rb') as f:
        bands = pickle.load(f)
    print('Данные загружены!')

# Пример использования функций
add_band("Metallica", ["Master of Puppets", "Ride the Lightning"])
add_band("Nirvana", ["Nevermind", "In Utero"])
find_band("Nirvana")
edit_band("Metallica", ["Black Album", "Load"])
delete_band("Nirvana")

save_data("bands.pkl")
bands.clear()  # Очистим для проверки
load_data("bands.pkl")
print(bands)
