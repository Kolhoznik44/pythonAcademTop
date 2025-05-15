"""
Создать класс для структуры данных Stack
класс должен иметь методы  - push, pop, top, size
push - добавляет элемент в стэк
pop - удаляет элемент из стэка и возвращает его значание
top - возвращает значение вверхнего элемента стэка
size - вохвращает количество элементов в стэке
"""
class Stack:
    def __init__(self):
        self.__stack = []

    def __del__(self):
        pass

    def push(self, item):
        self.__stack.append(item)

    def size(self):
        return len(self.__stack)
    def pop(self):
        if not self.is_empty():
            return self.__stack.pop()
        return None

    def top(self):
        if not self.is_empty():
            return self.__stack[-1]
        return None