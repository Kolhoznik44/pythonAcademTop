"""
Задание 1
Создайте класс Device, который содержит информацию об устройстве.
Спомощью механизма наследования, реализуйте класс
CoffeMachine (содержит информацию о кофемашине)
класс Blender (содержит информацию о блендере), класс
MeatGrinder (содержит информацию о мясорубке).
Каждый из классов должен содержать необходимые
для работы методы.

# Базовый класс для устройств
class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power  # в ваттах

    def device_info(self):
        return f"{self.brand} {self.model}, мощность: {self.power} Вт"

    def turn_on(self):
        print(f"{self.device_info()} включено.")

    def turn_off(self):
        print(f"{self.device_info()} выключено.")


# Кофемашина
class CoffeeMachine(Device):
    def __init__(self, brand, model, power, coffee_type):
        super().__init__(brand, model, power)
        self.coffee_type = coffee_type

    def make_coffee(self):
        print(f"{self.device_info()} готовит {self.coffee_type} кофе.")


# Блендер
class Blender(Device):
    def __init__(self, brand, model, power, speed_modes):
        super().__init__(brand, model, power)
        self.speed_modes = speed_modes  # количество скоростей

    def blend(self):
        print(f"{self.device_info()} работает на {self.speed_modes} скоростях. Взбивание началось.")


# Мясорубка
class MeatGrinder(Device):
    def __init__(self, brand, model, power, productivity):
        super().__init__(brand, model, power)
        self.productivity = productivity  # кг/мин

    def grind_meat(self):
        print(f"{self.device_info()} измельчает мясо с производительностью {self.productivity} кг/мин.")


# Пример использования:
if __name__ == "__main__":
    coffee = CoffeeMachine("Philips", "HD8827", 1850, "эспрессо")
    blender = Blender("Bosch", "MSM66150", 600, 12)
    meat_grinder = MeatGrinder("Moulinex", "ME2051", 1300, 1.5)

    coffee.turn_on()
    coffee.make_coffee()
    coffee.turn_off()

    blender.turn_on()
    blender.blend()
    blender.turn_off()

    meat_grinder.turn_on()
    meat_grinder.grind_meat()
    meat_grinder.turn_off()
"""

"""
Задание 2
Создайте класс Ship, который содержит информацию
о корабле.
С помощью механизма наследования, реализуйте
класс Frigate (содержит информацию о фрегате), класс
Destroyer (содержит информацию об эсминце), класс
Cruiser (содержит информацию о крейсере).
Каждый из классов должен содержать необходимые
для работы методы.


# Базовый класс Корабль
class Ship:
    def __init__(self, name, country, displacement):
        self.name = name
        self.country = country
        self.displacement = displacement  # водоизмещение в тоннах

    def info(self):
        return (f"Корабль: {self.name}\n"
                f"Страна: {self.country}\n"
                f"Водоизмещение: {self.displacement} тонн")

    def sail(self):
        print(f"{self.name} вышел в море.")

    def dock(self):
        print(f"{self.name} пришвартован в порту.")


class Frigate(Ship):
    def __init__(self, name, country, displacement, missile_count):
        super().__init__(name, country, displacement)
        self.missile_count = missile_count

    def info(self):
        base_info = super().info()
        return f"{base_info}\nТип: Фрегат\nРакет на борту: {self.missile_count}"

    def anti_submarine_warfare(self):
        print(f"Фрегат {self.name} ведет противолодочную оборону.")


class Destroyer(Ship):
    def __init__(self, name, country, displacement, torpedo_count):
        super().__init__(name, country, displacement)
        self.torpedo_count = torpedo_count

    def info(self):
        base_info = super().info()
        return f"{base_info}\nТип: Эсминец\nТорпед на борту: {self.torpedo_count}"

    def launch_torpedo(self):
        if self.torpedo_count > 0:
            self.torpedo_count -= 1
            print(f"Эсминец {self.name} запускает торпеду! Осталось торпед: {self.torpedo_count}")
        else:
            print(f"На эсминце {self.name} нет торпед!")


class Cruiser(Ship):
    def __init__(self, name, country, displacement, gun_caliber):
        super().__init__(name, country, displacement)
        self.gun_caliber = gun_caliber  # калибр главных орудий в мм

    def info(self):
        base_info = super().info()
        return f"{base_info}\nТип: Крейсер\nКалибр орудий: {self.gun_caliber} мм"

    def fire_salvo(self):
        print(f"Крейсер {self.name} производит залп главного калибра {self.gun_caliber} мм!")


# Пример использования:
if __name__ == "__main__":
    ship = Ship("Nevsky", "Россия", 9000)
    print(ship.info())
    ship.sail()
    ship.dock()
    print("—" * 30)

    frigate = Frigate("Адмирал Григорович", "Россия", 4000, 24)
    print(frigate.info())
    frigate.sail()
    frigate.anti_submarine_warfare()
    frigate.dock()
    print("—" * 30)

    destroyer = Destroyer("Arleigh Burke", "USA", 8300, 8)
    print(destroyer.info())
    destroyer.sail()
    destroyer.launch_torpedo()
    destroyer.dock()
    print("—" * 30)

    cruiser = Cruiser("Moskva", "Россия", 11380, 130)
    print(cruiser.info())
    cruiser.sail()
    cruiser.fire_salvo()
    cruiser.dock()
"""

"""
Задание 3
Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
поле для хранения копеек (центы, евроценты, копейки
и т.д.).
Реализовать методы для вывода суммы на экран, задания значений для частей. 

"""

class Money:
    def __init__(self, units=0, coins=0, currency='руб'):
        """
        units — целая часть (например, рубли, доллары)
        coins — дробная часть (например, копейки, центы)
        currency — строка, название валюты
        """
        self.currency = currency
        # Приведение coins к диапазону 0..99 и корректировка единиц
        self.units = units + coins // 100
        self.coins = coins % 100

    def set_units(self, units):
        self.units = units

    def set_coins(self, coins):
        # Корректируем на весь диапазон копеек
        self.units += coins // 100
        self.coins = coins % 100

    def set_money(self, units, coins):
        self.units = units + coins // 100
        self.coins = coins % 100

    def display(self):
        # 02d — вывод двух знаков для копеек, например 07
        print(f"{self.units} {self.currency} {self.coins:02d} коп.")

# Пример использования
if __name__ == "__main__":
    wallet = Money(5, 75, "руб")
    wallet.display()        # 5 руб 75 коп.
    wallet.set_coins(135)
    wallet.display()        # 6 руб 35 коп.
    wallet.set_money(3, 12)
    wallet.display()        # 3 руб 12 коп.
    wallet.set_units(10)
    wallet.display()        # 10 руб 12 коп.