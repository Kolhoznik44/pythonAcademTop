"""
Задание 1
Написать рекурсивную функцию нахождения наибольшего общего делителя двух целых чисел.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = 36
num2 = 48
result = gcd(num1, num2)
print(f"Наибольший общий делитель чисел {num1} и {num2} равен {result}")
"""

"""
Задание 2
Написать игру «Быки и коровы». Программа «загадывает» четырёхзначное число и играющий должен
угадать его. После ввода пользователем числа программа
сообщает, сколько цифр числа угадано (быки) и сколько
цифр угадано и стоит на нужном месте (коровы). После
отгадывания числа на экран необходимо вывести количество сделанных пользователем попыток. В программе
необходимо использовать рекурсию.
import random

def generate_number():
    return random.sample(range(10), 4)

def check_guess(secret_number, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return bulls, cows

def play_game(secret_number, attempts=0):
    guess = [int(x) for x in input("Введите четырехзначное число: ")]
    if len(guess) != 4:
        print("Пожалуйста, введите четырехзначное число.")
        return play_game(secret_number, attempts)
    
    bulls, cows = check_guess(secret_number, guess)
    print(f"Быки: {bulls}, Коровы: {cows}")
    
    if bulls == 4:
        print(f"Поздравляем! Вы угадали число за {attempts+1} попыток.")
    else:
        return play_game(secret_number, attempts+1)

if __name__ == "__main__":
    secret_number = generate_number()
    play_game(secret_number)
"""

"""
Задание 3
Данашахматная доска размером8×8 ишахматный конь.
Программа должна запросить у пользователя координаты
клетки поля и поставить туда коня. Задача программы
найти и вывести путь коня, при котором он обойдет все
клетки доски, становясь в каждую клетку только один
раз. (Так как процесс отыскания пути для разных начальных клеток может затянуться, то рекомендуется сначала
1
опробовать задачу на поле размером 6×6). В программе
необходимо использовать рекурсию.
def is_valid_move(board, row, col):
    if row >= 0 and row < len(board) and col >= 0 and col < len(board) and board[row][col] == -1:
        return True
    return False

def knight_tour(board, row, col, move_count):
    row_move = [2, 1, -1, -2, -2, -1, 1, 2]
    col_move = [1, 2, 2, 1, -1, -2, -2, -1]

    if move_count == len(board) * len(board):
        return True

    for i in range(8):
        new_row = row + row_move[i]
        new_col = col + col_move[i]
        if is_valid_move(board, new_row, new_col):
            board[new_row][new_col] = move_count
            if knight_tour(board, new_row, new_col, move_count+1):
                return True
            board[new_row][new_col] = -1

    return False

def print_board(board):
    for row in board:
        print(row)

# Создаем шахматную доску
n = 8
chess_board = [[-1 for _ in range(n)] for _ in range(n)]

# Устанавливаем начальные координаты коня
start_row = int(input("Введите начальную строку (0-7): "))
start_col = int(input("Введите начальный столбец (0-7): "))
chess_board[start_row][start_col] = 0

if knight_tour(chess_board, start_row, start_col, 1):
    print("Путь коня:")
    print_board(chess_board)
else:
    print("Нет решения.")
"""

"""
Задание 4
Написать игру «Пятнашки».
"""
import random

# Функция для вывода игрового поля
def print_board(board):
    for row in board:
        print(row)

# Функция для поиска пустой клетки на поле
def find_blank(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return (i, j)

# Функция для проверки допустимости хода
def is_valid_move(row, col):
    if row >= 0 and row < 4 and col >= 0 and col < 4:
        return True
    return False

# Функция для выполнения хода
def move_tile(board, row, col):
    direction = input("Введите направление (вверх, вниз, влево, вправо): ")
    if direction == "вверх":
        new_row, new_col = row - 1, col
    elif direction == "вниз":
        new_row, new_col = row + 1, col
    elif direction == "влево":
        new_row, new_col = row, col - 1
    elif direction == "вправо":
        new_row, new_col = row, col + 1
    else:
        print("Некорректное направление!")
        return False

    if is_valid_move(new_row, new_col):
        board[row][col], board[new_row][new_col] = board[new_row][new_col], board[row][col]
        return True
    else:
        print("Недопустимый ход!")
        return False

# Функция для проверки условия выигрыша
def is_winner(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] != i*4 + j + 1:
                return False
    return True

# Создаем игровое поле и расставляем числа случайным образом
board = [[0 for _ in range(4)] for _ in range(4)]
numbers = list(range(1, 16))
random.shuffle(numbers)
for i in range(4):
    for j in range(4):
        if numbers:
            board[i][j] = numbers.pop(0)

# Начало игры
print("Добро пожаловать в игру 'Пятнашки'!")
print_board(board)

# Цикл игры
while not is_winner(board):
    row, col = find_blank(board)
    if move_tile(board, row, col):
        print_board(board)

print("Поздравляем, вы выиграли!")