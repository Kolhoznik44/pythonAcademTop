"""
Два списка целых заполняются случайными числами.
Необходимо:
■ Сформировать третий список, содержащий элементы
обоих списков;
■ Сформировать третий список, содержащий элементы
обоих списков без повторений;
■ Сформировать третий список, содержащий элементы
общие для двух списков;
■ Сформировать третий список, содержащий только
уникальные элементы каждого из списков;
■ Сформировать третий список, содержащий только
минимальное и максимальное значение каждого из
списков
"""
import random

list1 = []
for i in range(5):
    list1.append(random.randint(1, 10))

list2 = []
for i in range(5):
    list2.append(random.randint(1, 10))

print("Первый список:", list1)
print("Второй список:", list2)

list3_all = list1 + list2
print("1. Все элементы:", list3_all)

list3_unique = list(set(list1 + list2))
print("2. Без повторений:", list3_unique)

list3_common = list(set(list1) & set(list2))
print("3. Общие элементы:", list3_common)

list3_unique_elements = list(set(list1) ^ set(list2))
print("4. Уникальные элементы:", list3_unique_elements)

list3_min_max = [min(list1), max(list1), min(list2), max(list2)]
print("5. Мин и макс значения:", list3_min_max)

