"""
Задание 1
Необходимо отсортировать первые две трети списка
в порядке возрастания, если среднее арифметическое
всех элементов больше нуля; иначе — лишь первую треть.
Остальную часть списка не сортировать, а расположить
в обратном порядке.


import random

def custom_sort(input_list):
    average = sum(input_list) / len(input_list)
    if average > 0:
        sorted_first_two_thirds = sorted(input_list[:int(2 / 3 * len(input_list))])
        rest_of_list = input_list[int(2 / 3 * len(input_list)):]
        rest_of_list.reverse()
    else:
        sorted_first_two_thirds = sorted(input_list[:int(1 / 3 * len(input_list))])
        rest_of_list = input_list[int(1 / 3 * len(input_list)):]
        rest_of_list.reverse()

    sorted_list = sorted_first_two_thirds + rest_of_list
    return sorted_list


random_list = [random.randint(-10, 10) for _ in range(20)]
print("Исходный список:", random_list)

sorted_list = custom_sort(random_list)
print("Отсортированный список:", sorted_list)
"""

"""
Задание 2
Написать программу «успеваемость». Пользователь
вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
меню для пользователя:
Вывод оценок (вывод содержимого списка);
Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
■ Выходит ли стипендия (стипендия выходит, если
средний бал не ниже 10.7);
■ Вывод отсортированного списка оценок: по возрастанию или убыванию.


def print_grades(grades):
    print("Оценки студента:")
    for i, grade in enumerate(grades, 1):
        print(f"Оценка {i}: {grade}")

def retake_exam(grades):
    index = int(input("Введите номер оценки для пересдачи (1-10): ")) - 1
    new_grade = int(input("Введите новую оценку (1-12): "))
    grades[index] = new_grade

def check_scholarship(grades):
    average_grade = sum(grades) / len(grades)
    if average_grade >= 10.7:
        print("Студент получает стипендию!")
    else:
        print("Студент не получает стипендию.")

def sort_grades(grades, reverse=False):
    sorted_grades = sorted(grades, reverse=reverse)
    return sorted_grades

grades = []
for i in range(10):
    grade = int(input(f"Введите оценку студента {i+1} (1-12): "))
    grades.append(grade)

while True:
    print("\nМеню:")
    print("1. Вывод оценок")
    print("2. Пересдача экзамена")
    print("3. Проверка стипендии")
    print("4. Вывод отсортированного списка оценок")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        print_grades(grades)
    elif choice == "2":
        retake_exam(grades)
    elif choice == "3":
        check_scholarship(grades)
    elif choice == "4":
        order = input("Выберите порядок сортировки (asc/desc): ")
        sorted_grades = sort_grades(grades, reverse=order == "desc")
        print_grades(sorted_grades)
    elif choice == "5":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")

"""

"""
Задание 3
Написать программу, реализующую сортировку списка
методом усовершенствованной сортировки пузырьковым
методом. Усовершенствование состоит в том, чтобы анализировать количество перестановок на каждом шагу, если
это количество равно нулю, то продолжать сортировку
нет смысла — список отсортирован.

"""

def improved_bubble_sort(arr):
    n = len(arr)
    swapped = True  # Флаг, показывающий были ли перестановки на текущем шаге

    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True

        if not swapped:
            break
    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = improved_bubble_sort(arr)
print("Отсортированный список:", sorted_arr)