"""Задание 1
Создайте функцию, возвращающую список со всеми
простыми числами от 0 до 1000.
Используя механизм декораторов посчитайте сколько
секунд, потребовалось для вычисления всех простых чисел.
Отобразите на экран количество секунд и простые числа

import time

# Декоратор для измерения времени выполнения функции
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Время выполнения функции: {elapsed:.6f} секунд")
        return result
    return wrapper

# Функция для поиска простых чисел от 0 до 1000
@timer_decorator
def get_primes():
    primes = []
    for num in range(2, 1001):
        is_prime = True
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

primes = get_primes()
print("Простые числа от 0 до 1000:")
print(primes)
"""

"""
Добавьте к первому заданию возможность передавать
границы диапазона для поиска всех простых чисел.



import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Время выполнения функции: {elapsed:.6f} секунд")
        return result
    return wrapper

@timer_decorator
def get_primes(lower_bound, upper_bound):
    primes = []
    for num in range(max(2, lower_bound), upper_bound+1):
        is_prime = True
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

a = int(input("Введите нижнюю границу диапазона: "))
b = int(input("Введите верхнюю границу диапазона: "))

primes = get_primes(a, b)
print(f"Простые числа от {a} до {b}:")
print(primes)
"""

"""
Задание 3
Каждый год ваша компания предоставляет различным
государственным организациям финансовую отчетность.
В зависимости от организации форматы отчетности разные. Используя механизм декораторов, решите вопрос
отчетности для организаций.

"""

import json
import csv
import xml.etree.ElementTree as ET
from io import StringIO


# Декоратор для вывода отчета в формате JSON
def json_report(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        result = json.dumps(data, indent=4, ensure_ascii=False)
        print("JSON Report:\n", result)
        return result

    return wrapper


# Декоратор для вывода отчета в формате CSV
def csv_report(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)
        result = output.getvalue()
        print("CSV Report:\n", result)
        return result

    return wrapper


# Декоратор для вывода отчета в формате XML
def xml_report(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        root = ET.Element("Report")
        for key, value in data.items():
            elem = ET.SubElement(root, key)
            elem.text = str(value)
        result = ET.tostring(root, encoding="utf-8").decode("utf-8")
        print("XML Report:\n", result)
        return result

    return wrapper


# Базовая функция генерации финансовых данных
def generate_report():
    return {
        "year": 2023,
        "income": 1200000,
        "expenses": 900000,
        "tax": 120000,
        "profit": 180000,
    }


# Формируем отчет для налоговой (JSON)
@json_report
def tax_office_report():
    return generate_report()


# Для статистики (CSV)
@csv_report
def statistics_office_report():
    return generate_report()


# Для банка (XML)
@xml_report
def bank_report():
    return generate_report()


tax_office_report()
statistics_office_report()
bank_report()