"""Домашнеее задание работа с ветками"""

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
flowerbed = [0, 1, 1, 0, 0, 0, 1, 0, 0]
print(max_flowers(flowerbed))