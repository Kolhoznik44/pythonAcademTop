"""
Задание 1
Есть четыре списка целых. Необходимо их объединить
в пятом списке. Полученный результат в зависимости от
выбора пользователя отсортировать по убыванию или
возрастанию. Найти значение, введенное пользователем,
с использованием линейного поиска.


print("Задано четыре списка целых чисел.")
a = [3, 1, 7, 9]
b = [8, 2]
c = [6, 4, 5]
d = [10]

combined = []
for lst in (a, b, c, d):
    combined += lst

print("Объединённый список:", combined)

order = input("Сортировать по возрастанию (v) или по убыванию (u)? Введите 'v' или 'u': ").strip().lower()
if order not in ("v", "u"):
    print("Неверный выбор, сортировка будет по возрастанию.")
    order = "v"

combined = sorted(combined, reverse=(order == "u"))
print("Отсортированный список:", combined)

value = int(input("Введите значение для поиска: "))  # Без try...except

# Линейный поиск
idx = -1
for i, val in enumerate(combined):
    if val == value:
        idx = i
        break

if idx == -1:
    print(f"Значение {value} не найдено в списке.")
else:
    print(f"Значение {value} найдено на позиции {idx}.")

"""

"""
Задание 2
Есть четыре списка целых. Необходимо объединить
в пятом списке только те элементы, которые уникальны
для каждого списка. Полученный результат в зависимости
от выбора пользователя отсортировать по убыванию или
возрастанию. Найти значение, введенное пользователем,
с использованием бинарного поиска.
"""

def get_unique_elements(lists):
    """Возвращает элементы, которые встречаются только в одном подсписке из списка списков."""
    all_elems = []
    for lst in lists:
        all_elems.extend(lst)
    unique_elems = []
    for i, lst in enumerate(lists):
        others = lists[:i] + lists[i+1:]
        for elem in lst:
            found = False
            for other in others:
                if elem in other:
                    found = True
                    break
            if not found and elem not in unique_elems:
                unique_elems.append(elem)
    return unique_elems

def sort_elements(elements, order):
    """Сортирует элементы по возрастанию ('v') или убыванию ('u')."""
    reverse = order == 'u'
    return sorted(elements, reverse=reverse)

def binary_search(lst, target):
    """Выполняет бинарный поиск target в отсортированном списке lst."""
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Основная программа
a = [3, 1, 7, 9]
b = [8, 2]
c = [6, 4, 5]
d = [10, 2, 3]
all_lists = [a, b, c, d]

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

unique = get_unique_elements(all_lists)
print("Уникальные элементы:", unique)

order = input("Сортировать по возрастанию (v) или убыванию (u)? Введите 'v' или 'u': ").strip().lower()
unique_sorted = sort_elements(unique, order)
print("Отсортированный список уникальных элементов:", unique_sorted)

x = int(input("Введите целое число для поиска в списке: "))
pos = binary_search(unique_sorted, x)
if pos != -1:
    print(f"Значение {x} найдено на позиции {pos}")
else:
    print(f"Значение {x} не найдено.")