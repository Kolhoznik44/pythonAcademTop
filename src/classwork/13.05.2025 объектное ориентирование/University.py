
# Роли в Университете:
#
# Студенты      - ФИО, Возраст, Группа
# Преподаватели - ФИО, Возраст, Кафедра
# Администрация - ФИО, Возраст, Должность

# Наследование - это возможность создания новой сущности (класса) на базе
# уже существующей сущности (другого класса)
# Наследование - это механизм языка, позволяющий передать механизмы
# от classA (родительский класс/superclass) в classB (наследник)
import abc
class Person:
    __name = str()
    _age = 0
    _med_id = str()

    def __init__(self,
                 name : str = "",
                 age : int = 0,
                 med_id : str = ""):
        self.__name = name
        self._age = age
        self._med_id = med_id


    def __del__(self):
        pass

    @property
    def med_id(self):
        return  self._med_id
    @med_id.setter
    def med_id(self, new_id : str):
        if len(new_id) == 0:
            return
        self._med_id = new_id

    @abc.abstractmethod
    def getMedId(self): pass

    def __str__(self):
        return f"Имя: {self.__name}\nВозраст: {self._age}"

    def say_hello(self):
        return f"Привет, меня зовут {self.__name}"


# Класс Student наследуется от класса Person
from typing import final

class Student(Person):
    __group = str()

    def __init__(self, name : str = "",
                       age : int = 0,
                       group : str = ""
                 ):
        super().__init__(name, age)
        self.__group = group

    def __del__(self):
        pass

    def say_hello(self):
        return f"{super().say_hello()}. {self.my_group()}"

    def __str__(self):
        return f"{super().__str__()}\nГруппа: {self.__group}"

    def my_group(self):
        return f"Я из группы {self.__group}"

    def getMedId(self):
        return f"Мой ID - {self._med_id}"

    def func(self):
        self._age = 0

class Teacher(Person):
    _kafedra = str()

    def __init__(self, name : str = "",
                       age : int = 0,
                       kafedra : str = ""
                 ):
        super().__init__(name, age)
        self._kafedra = kafedra

    def __del__(self):
        pass

    def my_job(self):
        return f"Я работаю на кафедре {self._kafedra}"

    def say_hello(self):
         return f"{super().say_hello()}. {self.my_job()}"

    def getMedId(self):
        return f"Мой СНИЛС - {self._med_id}"

@final
class Aspirant(Student, Teacher):
    def __init__(self,
                 name: str = "",
                 age: int = 0,
                 group: str = "",
                 kafedra: str = "",
                 ):
        super().__init__(name, age, group)
        self._kafedra = kafedra

    def __del__(self):
        pass



class Admin(Person):
    __post = str()

    def __init__(self, name: str = "",
                 age: int = 0,
                 post: str = ""
                 ):
        super().__init__(name, age)
        self.__post = post

    def __del__(self):
        pass

    def my_post(self):
        return f"Я работаю на должности - {self.__post}"

def function(obj : Person):
    print(obj.say_hello())


pers = Person("Христофор", 35)
stud = Student("Наташа", 25, "Py42")
admin = Admin("Мария", 29, "Директор")
teacher = Teacher("Евгений Иванович", 65, "ДифУр")

print(pers)
print("-=========-")
print(stud)
print("-=========-")
print(teacher)
print("-=========-")
stud.func()
print("-=========-")
asp = Aspirant("Степан", 26, "Py42", "МатМод")
print(asp.say_hello())
asp.med_id = "NewID"
print(asp.med_id)
print("-=========-")
print(asp.getMedId())


