def draw_area(area):                                                        # Функция отрисовки в консоль доски
    print("-" * 13)
    for i in range(len(area)):
        print("|", area[i][0], "|", area[i][1], "|", area[i][2], "|")
        print("-" * 13)
    print("=" * 56)


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


def set_in_area(area, turn):                                                # Ход игрока
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

    area[row][column] = turn                                                # Постваить ход игрока
    print("=" * 56)


def main():                                                         # Главная функция
    print("Wellcome to Tic-Tak game!")                              # Приветствие
    print("=" * 56)
    area = [[*('#' * 3)], [*('#' * 3)], [*('#' * 3)]]               # Поле игры

    try:
        draw_area(area)                                             # Отрисовать поле игры

        for turn in range(9):
            if turn % 2 == 0:                                       # Ход крестика
                print("X turn!")
                print("=" * 56)
                set_in_area(area, 'X')
            else:                                                   # Ход нолика
                print("0 turn!")
                print("=" * 56)
                set_in_area(area, '0')

            draw_area(area)                                         # Отрисовать поле игры

            if check_if_win(area, "X") and turn >= 3:               # Проверка крестика на победителя
                print("X win!")
                print("=" * 56)
                return
            elif check_if_win(area, "0") and turn >= 3:             # Проверка нолика на победителя
                print("0 win!")
                print("=" * 56)
                return
        print("Game over")                                          # Ничья

    except KeyboardInterrupt:                                       # Обработка исключения при досрочном выходе из игры
        print("\nBye-bye")


main()
