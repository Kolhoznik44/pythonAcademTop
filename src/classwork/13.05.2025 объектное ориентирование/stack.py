"""
Создать класс для структуры данных Stack
класс должен иметь методы  - push, pop, top, size
push - добавляет элемент в стэк
pop - удаляет элемент из стэка и возвращает его значание
top - возвращает значение вверхнего элемента стэка
size - вохвращает количество элементов в стэке
"""
class Stack:
    __container = list()
    __size = 0

    def __init__(self):
        pass

    def __del__(self):
        if self.__size > 0:
            self.__size = 0
            self.__container.clear()

    def push(self, element):
        self.__container.append(element)
        self.__size += 1

    def pop(self):
        self.__size -= 1
        return self.__container.pop()

    def top(self):
        return self.__container[self.__size - 1]

    @property
    def size(self):
        return self.__size

    def __getitem__(self, index):
        return self.__container[index]

    def __delitem__(self, key):
        self.__container.pop(key)

    def __setitem__(self, key, value):
        if key > self.__size:
            while key != self.__size:
                self.__container.append(0)
                self.__size += 1
        elif key < 0:
            return
        self.__container.append(value)

    def __contains__(self, item):
        for elem in self.__container:
            if elem == item:
                return True
        return False

    def indexOf(self, item):
        # return self.__container.index(item)
        for i, elem in enumerate(self.__container):
            if elem == item:
                return i
        raise ValueError

    def countOf(self, item):
        # return self.__container.count(item)
        count = 0
        for elem in self.__container:
            if elem == item:
                count += 1
        return count
