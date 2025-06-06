"""
Задание №1
На завод по производству автомобилей необходимо создать систему
классов для введения базы данных всех выпущенных авто
все автомобили обладают следующими характеристиками:
1.Цена
2.Название
3.Цвет
4.Мощность двигателя
Необходимо реализовать классы для следующиъ видов машин
-Седан
1 АКПП/МКПП
2. Количество дополнительных обций
-внедорожники
1. Рамный или нет
2. Полный привод или нет
3. блокировка
4. Вид топлива
-Грузовой
1.Тоннаж
2.Возможность установки прицепа
3.Наличие спального места
4. Количество Мест
"""
import abc

class Interface(abc.ABC):
    @abc.abstractmethod
    def forward_moving(self):
        pass

    @abc.abstractmethod
    def backward_moving(self):
        pass

    @abc.abstractmethod
    def start_engine(self):
        pass


    """def function(obj):
        obj.start_engine()
        obj.forward_moving()
        obj.backward_moving()"""

class Car(Interface):
    def __init__(self, price: int = 0, name: str = "", color: str = "", power: int = 0):
        self._price = price
        self._name = name
        self._color = color
        self._power = power

    def __str__(self):
        return (f"Название авто: {self._name}\n"
                f"Цена: {self._price}\n"
                f"Цвет: {self._color}\n"
                f"Мощность: {self._power} л.с.")

    def forward_moving(self):
        print(f"{self._name} едет вперед")

    def backward_moving(self):
        print(f"{self._name} едет назад")

    def start_engine(self):
        print(f"{self._name} завёл двигатель")

class Sedan(Car):
    def __init__(self, price, name, color, power, transmission, options_count):
        super().__init__(price, name, color, power)
        self._transmission = transmission
        self._options_count = options_count

    def __str__(self):
        base = super().__str__()
        return (f"{base}\n"
                f"Трансмиссия: {self._transmission}\n"
                f"Доп. опций: {self._options_count}")

class SUV(Car):
    def __init__(self, price, name, color, power, frame, awd, locking, fuel):
        super().__init__(price, name, color, power)
        self._frame = frame
        self._awd = awd
        self._locking = locking
        self._fuel = fuel

    def __str__(self):
        base = super().__str__()
        frame_txt = "Рамный" if self._frame else "Безрамный"
        awd_txt = "Полный привод" if self._awd else "Передний/задний привод"
        locking_txt = "Есть блокировка" if self._locking else "Без блокировки"
        return (f"{base}\n"
                f"{frame_txt}\n"
                f"{awd_txt}\n"
                f"{locking_txt}\n"
                f"Топливо: {self._fuel}")

class Cargo(Car):
    def __init__(self, price, name, color, power, tonnage, trailer, sleeper, seats):
        super().__init__(price, name, color, power)
        self._tonnage = tonnage
        self._trailer = trailer
        self._sleeper = sleeper
        self._seats = seats

    def __str__(self):
        base = super().__str__()
        trailer_txt = "Можно прицеп" if self._trailer else "Без прицепа"
        sleeper_txt = "Есть спальное место" if self._sleeper else "Нет спального"
        return (f"{base}\n"
                f"Тоннаж: {self._tonnage}\n"
                f"{trailer_txt}\n"
                f"{sleeper_txt}\n"
                f"Мест: {self._seats}")

    def start_engine(self):
        print(f"{self._name} автозапуск имеется")



""""""


def drive(obj: Interface):
    obj.start_engine()
    obj.forward_moving()
    obj.backward_moving()

if __name__ == "__main__":
    sed = Sedan(200000, "Чепырка", "салатовый", 1000, "АКПП", 5)
    suv1 = SUV(200000, "Уаз", "черный", 500, True, True, True, "бензин")
    track = Cargo(5000000, "КАМАЗ", "белый", 1000, 12, True, True, 2)

    print(sed, end='\n\n')
    print(suv1, end='\n\n')
    print(track, end='\n\n')

    sed.forward_moving()
    suv1.backward_moving()
    track.forward_moving()
    Interface.function(sed)

    drive(sed)
    drive(suv1)





