def check_if_win(area, current_turn):                                       # Функция проверки на победителя

    for row_column in range(3):                                             # Проверка по главной диагонали
        if area[row_column][row_column] != current_turn:
            break
        elif row_column == len(area) - 1:
            return True

    for row_column in range(3):                                             # Проверка по обратной диагонали
        if area[row_column][len(area) - row_column - 1] != current_turn:
            break
        elif row_column == len(area) - 1:
            return True

    for row in range(3):                                                    # Проверка по строкам
        for column in range(3):
            if area[row][column] != current_turn:
                break
            elif column == len(area) - 1:
                return True

    for column in range(3):                                                 # Проверка по столбцам
        for row in range(3):
            if area[row][column] != current_turn:
                break
            elif row == len(area) - 1:
                return True

    return False                                                            # Вернуть ложь если нет победителя


def draw_area(area):                                                        # Функция отрисовки доски в консоль
    print("-" * 13)
    for i in range(len(area)):
        print("|", area[i][0], "|", area[i][1], "|", area[i][2], "|")
        print("-" * 13)
    print("=" * 56)


def set_in_area(area, turn):                                                # Разместить ход игрока
    try:                                                                    # Ввод строки и столбца
        row = int(input("Enter the row: ")) - 1
        column = int(input("Enter the column: ")) - 1
    except ValueError:                                                      # Обработка исключения если введено не число
        print("Invalid number (you can use: 1, 2, 3)")
        print("=" * 56)
        return set_in_area(area, turn)

    if (row < 0 or row >= 3) or (column < 0 or column >= 3):                # Обработка если число больше 3 или меньше 1
        print("The row or column can not be more than 3 and less than 1")
        print("=" * 56)
        return set_in_area(area, turn)

    if area[row][column] != '#':                                            # Обработка если ячейка уже занята
        print("This cell is already busy")
        print("=" * 56)
        return set_in_area(area, turn)

    area[row][column] = turn                                                # Поставить ход игрока
    print("=" * 56)


def print_welcome():                                                        # Приветствие
    print("Welcome to Tic-Tak-Toe game!")
    print("=" * 56)


def move(area, turn):                                                       # Ход игрока
    print(f"{turn} turn!")
    print("=" * 56)
    set_in_area(area, turn)
    draw_area(area)


def winner(turn):                                                           # Функция победителя
    print(f"{turn} win!")
    print("=" * 56)

