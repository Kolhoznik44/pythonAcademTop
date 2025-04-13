"""
Задание 1
Есть три кортежа целых чисел необходимо найти
элементы, которые есть во всех кортежах.



def find_common_elements(tuple1, tuple2, tuple3):
# Преобразуем кортежи в множества
    set1 = set(tuple1)
    set2 = set(tuple2)
    set3 = set(tuple3)
# Находим пересечение множеств
    common_elements = tuple(set1 & set2 & set3)
    return common_elements

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (2, 4, 6, 8)
tuple3 = (2, 3, 4, 5, 7)

result = find_common_elements(tuple1, tuple2, tuple3)
print("Общие элементы:", result)
"""


"""
Задание 2
Есть три кортежа целых чисел необходимо найти
элементы, которые уникальны для каждого списка.


def find_unique_elements(tuple1, tuple2, tuple3):
    set1 = set(tuple1)
    set2 = set(tuple2)
    set3 = set(tuple3)
    # Находим уникальные элементы для каждого множества
    unique1 = set1 - set2 - set3
    unique2 = set2 - set1 - set3
    unique3 = set3 - set1 - set2
    return unique1, unique2, unique3

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (2, 4, 6, 8)
tuple3 = (2, 3, 4, 5, 7)

result = find_unique_elements(tuple1, tuple2, tuple3
                              )
print("Уникальные элементы:")
print(f"Первый кортеж: {result[0]}")
print(f"Второй кортеж: {result[1]}")
print(f"Третий кортеж: {result[2]}")

"""
"""
Задание 3
Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и находятся
в каждом из кортежей на той же позиции.
"""

def find_common_positional_elements(tuple1, tuple2, tuple3):
    return [
        tuple1[i]
        for i in range(min(len(tuple1), len(tuple2), len(tuple3)))
        if tuple1[i] == tuple2[i] == tuple3[i]
    ]

t1 = (1, 2, 3, 4, 5)
t2 = (1, 2, 4, 4, 6)
t3 = (1, 2, 3, 4, 7)

print(find_common_positional_elements(t1, t2, t3))


