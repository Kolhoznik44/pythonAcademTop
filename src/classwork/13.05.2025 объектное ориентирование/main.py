# Операторы
# Операторы - это особые команды языка, которые можно вызывать
# через закрепленные за ними сиволы
# + - сложение
# - - вычитание
# Операнды - это непосредственно переменные, которые принимают участие в
# операции.
# Стандартный вид операции: <операнд> <оператор> <операнд>

# Группы операторов по кол-ву операндов:

# Унарные операторы:
# Инверсия(-var), отрицание(-var), логическое отрицание(not var),
# Проверка на True/False(var), Индексатор(var[i]),
# Присвоение по индексу(var[i] = k), Удаление по индексу(del var[i])

# Бинарные операторы:
# Математические операции(var+var, var-var, var*var, var/var, var//var)
# Логические операции(var < var,var > var, var == var, var != var)
# Присвоение (var = var, var += var, var -= var, var *= var...)

from oper import Oper
from stack import Stack

if __name__ == "__main__":
    var_1 = Oper(10)
    var_2 = Oper(0)

    if var_1:
        print(f"var_1 is True")
    if not var_2:
        print(f"var_2 is True")
    else:
        print(f"var_2 is False")

    if var_1 < "Hello":
        pass

    var_3 = var_1 + (- var_2)

    stc = Stack()
    stc.push(1)
    stc.push(2)
    stc.push(3)
    print(f"{3} = {stc.indexOf(3)} позиция")
    stc[7] = 10
    print(f"Zero-Count = {stc.countOf(0)}")
    while stc.size >= 0:
        print(stc.pop())