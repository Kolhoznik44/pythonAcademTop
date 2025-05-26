# Лямбда-выражения aka Анонимные функции
# Это функции у которых нет привычного имени и объявления.
# Они создаются в одной конкретной переменной и могут вызываться ТОЛЬКО
# через эту переменную
# Синтаксис:
# <переменная> = lambda <список параметров> : <тело функции>
import random

square = lambda numer: numer * numer
print(square(2))

def Equals(first : int, func) -> str:
    return f"{first} ** 2 = {func(first)}"

print(Equals(4, lambda numer: numer*numer))


# Сортировки
# Сортировка пузырьком

def BubbleSort(lst : list) -> list:
    i = 1
    while i < len(lst):
        if lst[i] < lst[i-1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            j = i - 1
            while j > 0:
                if lst[j] < lst[j-1]:
                    lst[j], lst[j-1] = lst[j-1], lst[j]
                else:
                     break
                j -= 1
            i -= 1
        i += 1
    return lst

def SelectionSort(lst : list) -> list:
    for i in range(len(lst)):
        minElem = i
        for j in range(i, len(lst)):
            if lst[minElem] > lst[j]:
                minElem = j
        lst[minElem], lst[i] = lst[i],lst[minElem]
    return lst

def merge(leftList : list, rightList: list):
    mergeList = list()
    left = right = 0
    for _ in range(0, len(leftList) + len(rightList)):
        if left < len(leftList) and right < len(rightList):
            if leftList[left] < rightList[right]:
                mergeList.append(leftList[left])
                left += 1
            else:
                mergeList.append(rightList[right])
                right += 1
            elif left == len(leftList):
                mergeList.append(rightList[right])
                right += 1
            elif right == len(rightList):
                mergeList.append(leftList[left])
                left += 1
            return mergeList

        def MergeSort(lst: list) -> list:
            if len(lst) <= 1:
                return lst
            mid = len(lst) // 2
            leftList = MergeSort(lst[0:mid])
            rightList = MergeSort(lst[mid:])
            return merge(leftList, rightList)

        lst = [1, 6, 2, 26, 87, 5, 4, 120, -161, 59, 48, -3, 36, 0]
        lst_2 = list()
        for i in range(0, 10000):
            lst_2.append(random.randint(-32567, 32567))
        print(BubbleSort(lst_2))
        print("-======-")
        print(SelectionSort(lst_2))
        print("-======-")
        print(MergeSort(lst_2))

# Задача 2 - RomanToInt
# Дана строка, в которой содержится 1 число, записанное римскими цифрами
# Необходимо вывести строку вида: {римская запись} = {арабская запись}
# Римские цифры имеют следующие правила
# I - 1   D = 500
# V - 5   M = 1000
# X - 10
# L - 50
# C - 100
# НО, для описания некоторых чисел вводится операция вычитания - IV = 4
# У римских чисел имеются следующие правила:
# При записи числа ВСЕГДА впереди идет самый большой порядок, за исключением
# следующих ситуаций
# 1. Перед C и L может быть записано несколько X для обозначения вычитания
# 2. Перед X может быть записано V или I для обозначения вычитания
# 3. Перед V может быть записано I для обозначения вычитания
# Примеры для расшифроки:
# CLXVIII = 168
# CXLIV = 144
# LXXXVIII = 88

def romanToInt(roman : str) -> int:
    arabian = list()
    for elem in roman:
        match elem:
            case "I":
                arabian.append(1)
            case "V":
                arabian.append(5)
            case "X":
                arabian.append(10)
            case "L":
                arabian.append(50)
            case "C":
                arabian.append(100)
    result = 0
    lvl = 1
    temp = 0
    for arab in arabian[::-1]:
        if arab == lvl:
            temp += lvl
        elif arab < lvl:
            temp -= arab
        elif arab > lvl:
            result += temp
            temp = lvl = arab
    result += temp
    return result
    # romanToDigit = {
    #     "I" : 1,
    #     "V" : 5,
    #     "X" : 10,
    #     "L" : 50,
    #     "C" : 100
    # }
    # levels = "IVXLC"
    # lvl = 0
    # temp = 0
    # result = 0
    # for elem in roman[::-1]:
    #     pass
    # result += temp
    # return result

print(romanToInt("IVXCVXXL"))