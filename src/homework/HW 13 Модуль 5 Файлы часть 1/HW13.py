#readline позволяет вернуть одну строку  вашего текстового файла
# переносит курсор на следующукую строку
# seek(<position>) позволяет перемещать курсор внутри текстового файла
# position - нужная нам позиция
#tell - возвращает текущее положение курсора в файле считает с 1
# read - позволяет читать определенное количество элементов, но от последнего положения курсора в файле
# close -закрывает поток ваших данных, потоки которые остаются открытыми после завершенияоперации могут вести  к
# утечке данных или к проблемам  в работе ПО
# write(<"">) - позволяет записать строку  в ваш файл
#print(stream.read(13))
#arr = stream.readline()
#print(stream.readline())
#print(stream.readline())
#stream.seek(0)
#print(stream.readline())
#stream.write(" World")

"""
моды работ с файлами
 1. 'r'(read)- файл доступен только для чтения
 2. 'w' (write)- доступен только для записи ( постоянная перезапись)
 создает файл если его нет в диррективе

 3. 'a' - файл доступен только для записи, но запись производится в конец файла
  создает файл если его нет в диррективе
 4. '+'- разрешено и чтение и запись (r+,w+,a+)
 5. t -  мы работаем с текстовым файлом
 6. b - мы работаем с бинарных файлом
"""
"""
Задание 1
Дано два текстовых файла. Выяснить, совпадают ли
их строки. Если нет, то вывести несовпадающую строку
из каждого файла.



def compare_files(file1, file2):
    with open(file1, encoding='utf-8') as f1, open(file2, encoding='utf-8') as f2:
        lines1 = [line.rstrip('\r\n') for line in f1]
        lines2 = [line.rstrip('\r\n') for line in f2]

    max_len = max(len(lines1), len(lines2))
    match = True
    for i in range(max_len):
        line1 = lines1[i] if i < len(lines1) else '<Пустая строка>'
        line2 = lines2[i] if i < len(lines2) else '<Пустая строка>'
        if line1 != line2:
            print(f'Строка {i+1} не совпадает:')
            print(f'  {file1}: {line1}')
            print(f'  {file2}: {line2}')
            match = False
    if match:
        print('Все строки совпадают!')

# Пример использования:
compare_files('file1.txt', 'file2.txt')

"""

"""
Задание 2
Дан текстовый файл. Необходимо создать новый файл
и записать в него следующую статистику по исходному
файлу:
■ Количество символов;
■ Количество строк;
■ Количество гласных букв;
■ Количество согласных букв;
■ Количество цифр.


# Имя исходного и выходного файлов
input_file = "input.txt"
output_file = "output.txt"

# Русские и английские гласные и согласные (можете расширить при необходимости)
vowels = "аеёиоуыэюяaeiouy"
consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz"
vowels += vowels.upper()
consonants += consonants.upper()

# Счётчики
chars_count = 0
lines_count = 0
vowels_count = 0
consonants_count = 0
digits_count = 0

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        lines_count += 1
        chars_count += len(line)
        for ch in line:
            if ch in vowels:
                vowels_count += 1
            elif ch in consonants:
                consonants_count += 1
            elif ch.isdigit():
                digits_count += 1

# Запись статистики в новый файл
with open(output_file, 'w', encoding='utf-8') as out:
    out.write(f"Количество символов: {chars_count}\n")
    out.write(f"Количество строк: {lines_count}\n")
    out.write(f"Количество гласных букв: {vowels_count}\n")
    out.write(f"Количество согласных букв: {consonants_count}\n")
    out.write(f"Количество цифр: {digits_count}\n")

print(f"Статистика записана в файл {output_file}")

"""

"""
Задание 3
Дан текстовый файл. Удалить из него последнюю
строку. Результат записать в другой файл.


# Пути к файлам
input_file = "input1.txt"
output_file = "output1.txt"

# Чтение всех строк из файла
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Запись всех строк, кроме последней, в новый файл
with open(output_file, 'w', encoding='utf-8') as out:
    out.writelines(lines[:-1])  # lines[:-1] — все строки, кроме последней

print(f"Результат записан в файл {output_file}")

"""

"""
Задание 4
Дан текстовый файл. Найти длину самой длинной
строки.

# Пути к файлу
input_file = "input.txt"

max_length = 0

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        line_length = len(line.rstrip('\n'))  # Убираем символ перевода строки
        if line_length > max_length:
            max_length = line_length

print(f"Длина самой длинной строки: {max_length}")
"""


"""
Задание 5
Дан текстовый файл. Посчитать сколько раз в нем
встречается заданное пользователем слово.

file_name = "input.txt"

word = input("Введите слово для поиска: ")
count = 0  # Счётчик
with open(file_name, 'r', encoding='utf-8') as f:
    for line in f:
        words = line.split()  # Разбиваем строку на отдельные слова
        for w in words:
            if w == word:
                count += 1

print(f'Слово "{word}" встречается {count} раз(а) в файле.')
"""

"""
Задание 6
Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется
пользователем.
"""
def replace_in_file(filename, find_word, replace_word):
    # Считываем r
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    # Заменяем слово
    new_text = text.replace(find_word, replace_word)
    # Записываем w
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_text)
    print(f'Все вхождения "{find_word}" заменены на "{replace_word}".')

filename = "input.txt"
find_word = input("Какое слово найти? ")
replace_word = input("На какое слово заменить? ")
replace_in_file(filename, find_word, replace_word)