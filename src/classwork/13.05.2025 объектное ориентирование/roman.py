# Задание 1 - Необходимо создать класс, хранящий в себе Римские числа
# Класс обязан предоставлять возможность складывать, вычитать, умножать
# и делить свои объекты
# При выводе в print должна выводится именно римская запись числа
# Инициализация может быть как прямой (то есть приходит строка с
# римской записью) так и обратной (приходит число и необходимо по нему
# построить римскую запись)




class RomanNum:
    __arab_value = 0
    __roman_value = str()
    __alphabet = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100
    }

    def __init__(self, value : str = "", a_value : int = 0):
        if value:
            self.__roman_value = value
            self.__arab_value = self.__roman_to_int(value)
        elif a_value:
            self.__arab_value = a_value
            self.__roman_value = self.__int_to_roman(a_value)
        else:
            return

    def __del__(self):
        pass

    def __roman_to_int(self, value : str) -> int:
        now_lvl = 1
        val = 0
        temp = 0
        for elem in value[::-1]:
            if self.__alphabet[elem] == now_lvl:
                val += temp
                temp = 0
            elif self.__alphabet[elem] > now_lvl:
                val += temp
                now_lvl = self.__alphabet[elem]
                temp = self.__alphabet[elem]
            else:
                temp -= self.__alphabet[elem]
        val += temp
        return val

    def __int_to_roman(self, value : int) -> str:
        alpha_lst = ["C", "L", "X", "V", "I"]
        roman = str()
        for key in alpha_lst:
            while value - self.__alphabet[key] >= 0:
                value -= self.__alphabet[key]
                roman += key
        # 4
        if "IIII" in roman:
            roman = roman.replace("IIII", "IV")
        # 9
        if "VIV" in roman:
            roman = roman.replace("VIV", "IX")
        # 40
        if "XXXX" in roman:
            roman = roman.replace("XXXX", "XL")
        # 49
        if "XLIX" in roman:
            roman = roman.replace("XLIX", "IL")
        # 90
        if "LXL" in roman:
            roman = roman.replace("LXL", "XC")
        # 99
        if "XCIX" in roman:
            roman = roman.replace("XCIX", "IC")
        if "LIL" in roman:
            roman = roman.replace("LIL", "IC")
        #1000
        if "CCCCCCCCCC" in roman:
            roman = roman.replace("CCCCCCCCCC", "M")

        return roman

    def __str__(self):
        if self.__arab_value == 0:
            return "0"
        else:
            return self.__roman_value

    def __add__(self, other):
        if isinstance(other, int):
            other = RomanNum(a_value=other)
        elif not isinstance(other, RomanNum):
            raise ValueError
        return RomanNum(a_value=(self.__arab_value + other.__arab_value))

    def __sub__(self, other):
        if isinstance(other, int):
            other = RomanNum(a_value=other)
        elif not isinstance(other, RomanNum):
            raise ValueError
        return RomanNum(a_value=(self.__arab_value - other.__arab_value))

    def __mul__(self, other):
        if isinstance(other, int):
            other = RomanNum(a_value=other)
        elif not isinstance(other, RomanNum):
            raise ValueError
        return RomanNum(a_value=(self.__arab_value * other.__arab_value))

    def __truediv__(self, other):
        if isinstance(other, int):
            other = RomanNum(a_value=other)
        elif not isinstance(other, RomanNum):
            raise ValueError
        return RomanNum(a_value=(self.__arab_value / other.__arab_value))

val_1 = RomanNum(a_value=144)
val_2 = RomanNum(value=val_1.__str__())
print(f"{val_1} = {val_2}")
print(f"{val_1} + {val_2} = {val_1 + val_2}")
print(f"{val_1} - {val_2} = {val_1 - val_2}")
print(f"{val_1} * {val_2} = {val_1 * val_2}")
print(f"{val_1} / {val_2} = {val_1 / val_2}")


