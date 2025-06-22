class HouseComponent:
    def cost(self):
        raise NotImplementedError("Реализуйте метод cost для компонента дома")

class Basement(HouseComponent):
    def __init__(self, foundation_type, area, electric_area, communications):
        self.foundation_type = foundation_type
        self.area = area
        self.electric_area = electric_area
        self.communications = communications

    def cost(self):
        prices = {'лента': 60000, 'сваи': 40000, 'плита': 75000}
        comm_cost = 12000
        electric_cost_per_m2 = 300
        price = prices.get(self.foundation_type, 0) * self.area
        price += len(self.communications) * comm_cost
        price += self.electric_area * electric_cost_per_m2
        return int(price)

class Floor(HouseComponent):
    def __init__(self, area, rooms, bathrooms):
        self.area = area
        self.rooms = rooms
        self.bathrooms = bathrooms

    def cost(self):
        price_per_m2 = 50000
        bathroom_cost = 90000
        price = self.area * price_per_m2
        price += self.bathrooms * bathroom_cost
        return int(price)

class Roof(HouseComponent):
    def __init__(self, roof_type, attic_area=0, has_satellite=False):
        self.roof_type = roof_type
        self.attic_area = attic_area
        self.has_satellite = has_satellite

    def cost(self):
        prices = {'плоская': 18000, 'двускатная': 30000, 'мансардная': 35000}
        sat_cost = 28000
        roof_area = self.attic_area if self.attic_area > 0 else 100
        price = prices.get(self.roof_type, 0) * roof_area
        if self.has_satellite:
            price += sat_cost
        return int(price)

class ExtraBuilding(HouseComponent):
    def __init__(self, building_type, area):
        self.building_type = building_type
        self.area = area

    def cost(self):
        prices = {'гараж': 45000, 'баня': 55000, 'беседка': 20000, 'летняя кухня': 30000}
        return int(prices.get(self.building_type, 0) * self.area)

class Option(HouseComponent):
    def __init__(self, name):
        self.name = name

    def cost(self):
        price_list = {'умный дом': 350000, 'солнечные панели': 450000, 'теплый пол': 120000}
        return price_list.get(self.name, 0)

class House:
    def __init__(self, basement=None, floors=None, roof=None, extra_buildings=None, options=None):
        self.basement = basement  # объект Basement
        self.floors = floors if floors is not None else []  # список Floor
        self.roof = roof  # объект Roof
        self.extra_buildings = extra_buildings if extra_buildings is not None else []  # список ExtraBuilding
        self.options = options if options is not None else []  # список Option

    def cost(self):
        total = 0
        if self.basement:
            total += self.basement.cost()
        for floor in self.floors:
            total += floor.cost()
        if self.roof:
            total += self.roof.cost()
        for b in self.extra_buildings:
            total += b.cost()
        for o in self.options:
            total += o.cost()
        return total

    def config_print(self):
        print("Конфигурация дома:")
        if self.basement:
            print(f"  Фундамент: {self.basement.foundation_type}, площадь: {self.basement.area}м², "
                  f"электро: {self.basement.electric_area}м², коммуникации: {', '.join(self.basement.communications)}")
        for i, f in enumerate(self.floors, 1):
            print(f"  Этаж {i}: площадь: {f.area}м², комнат: {f.rooms}, санузлов: {f.bathrooms}")
        if self.roof:
            print(f"  Крыша: {self.roof.roof_type}, чердак: {self.roof.attic_area}м², спутник: {self.roof.has_satellite}")
        for b in self.extra_buildings:
            print(f"  Постройка: {b.building_type}, {b.area}м²")
        for o in self.options:
            print(f"  Опция: {o.name}")

# ======== Пример использования ========
if __name__ == "__main__":
    basement = Basement("плита", 120, 12, ["газ", "вода"])
    floor1 = Floor(110, 3, 1)
    floor2 = Floor(110, 4, 2)
    roof = Roof("двускатная", attic_area=40, has_satellite=True)
    garage = ExtraBuilding("гараж", 25)
    sauna = ExtraBuilding("баня", 12)
    option1 = Option("солнечные панели")
    option2 = Option("умный дом")

    house = House(
        basement=basement,
        floors=[floor1, floor2],
        roof=roof,
        extra_buildings=[garage, sauna],
        options=[option1, option2]
    )

    house.config_print()
    print(f"\nИтоговая стоимость: {house.cost():,} руб.")