"""

задача 1
представьте что у вас есть длинная клумба. На этой клумбе выложены разные цветы. Есть места под новые,
однако цветы не могут ужиться друг с другом если между ними нет расстояния хотя б в одно посадочное место
Вам передается строка из 0 и 1 где 0 - пустое место
1 - занятое место
Необходимо реализовать функцию которая вернет максимальное количество цветов которые можно посадить на эту клумбу при
условии что они буду посажены одной не разрывной клумбой
пример [1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0] ->2
        [1,0,1,0,1,0,0,0,1,0,1,0] ->1
"""


def max_flowers(flowerbed):
    count = 0
    size = len(flowerbed)

    for i in range(size):
        if flowerbed[i] == 0:
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            right_empty = (i == size - 1) or (flowerbed[i + 1] == 0)

            if left_empty and right_empty:
                flowerbed[i] = 1
                count += 1

    return count

flowerbed1 = [0, 1, 1, 0, 0, 0, 1, 0, 0]
flowerbed2 = [0, 0, 0]
flowerbed3 = [1,1,0,0,0,0,0,1]

print(max_flowers(flowerbed1))
print(max_flowers(flowerbed2))
print(max_flowers(flowerbed3))


