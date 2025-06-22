"""
строительная компания нуждается в прогармме которая бы по хотелкам клиента
прикидывала сметуи и тоговую стоимость проекта
Существуют следующие классы
1 Подвал
    - тип фундамента
    - Подводимые коммуникации
    - Площадь подвала
    - площадь входной электрики
2 Этаж
    - Площадь этажа
    - Кол-во комнат
    - Кол-во санузелов
3 Крыша
    - Наличие и площадь чердака
    - Тип Крышы
    - Спутниковая тарелка
4 дополнительные постройки на территории
    - площадь построек
    - виды построе
5 Дополнительные опции



Необходимо задать класс, который бы позволял по желанию клиента
сконфигурировать обьект Дом, внутри которого будут находиться поля-
обьекты приведенных выше классов

"""
import abc

class House(abc.ABC):
    @abc.abstractmethod
    def cost(self):
        return print(" рассчет цены")



class Basement(House): # подвал
    def __init__(self, foundation_type: str = "", communications: str = "",
                 basement_area: int = 0, input_electrical_area: int = 0):
        self.foundation_type = foundation_type                      # тип фундамента
        self.communications = communications                    # Подводимые коммуникации
        self.basement_area = basement_area                          # Площадь подвала
        self.input_electrical_area = input_electrical_area          # площадь входной электрики

    def cost(self):
        prices = {'лента': 60000, 'сваи': 40000, 'плита': 75000}
        comm_cost = 12000
        electric_cost_per_m2 = 300
        price = prices.get(self.foundation_type, 0) * self.basement_area
        price += len(self.communications) * comm_cost
        price += self.basement_area * electric_cost_per_m2
        return int(price)

    def __str__(self):
        return (f"Тип фундамента: {self.foundation_type }\n"
                f"Подводимые коммуникации: {self.ommunications}\n"
                f"Площадь подвала: {self.basement_area}"
                f"площадь входной электрики:{self.input_electrical_area} ")

class Floor(House): # Этаж
    def __init__(self, area, rooms, bathrooms):
        self.area = area            # площадь этажа
        self.rooms = rooms          # кол-во комнат
        self.bathrooms = bathrooms  # Кол-во санузелов

    def __str__(self):
        return (f"Площадь этажа: {self.area}\n"
                f"кол-во комнат: {self.rooms}\n"
                f"Кол-во санузелов: {self.bathrooms}")

    def __del__(self):
        pass

class Roof(House):  #Крыша
    def __init__(self, roof_type, attic_area, has_satellite):
        self.roof_type = roof_type              # Тип Крыши
        self.attic_area = attic_area            # площадь чердака
        self.has_satellite = has_satellite      # наличие спутника

    def __del__(self):
        pass

    def __str__(self):
        return (f"Тип крыши: {self.roof_type}\n"
                f"площадь чердака: {self.attic_area}\n"
                f"Наличие спутника: {self.has_satellite}")

class Buildings(House): # дополнительные постройки на террриториий
    def __init__(self, building_area,types_of_buildings ):
        self.building_area = building_area             # площадь построек
        self.types_of_buildings = types_of_buildings   # виды построек

    def __del__(self):
        pass

    def __str__(self):
        return (f"площадь построек: {self.building_area}\n"
                f"виды построек: {self.types_of_buildings}")

class Additional_options(House): #дополнительные опции
    pass