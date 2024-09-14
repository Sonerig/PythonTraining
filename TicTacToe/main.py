from game_logic import *


def main():                                                         # Главная функция
    print_welcome()
    area = [[*('#' * 3)], [*('#' * 3)], [*('#' * 3)]]               # Поле игры

    try:
        draw_area(area)                                             # Отрисовать поле игры

        for turn in range(9):
            if turn % 2 == 0:                                       # Ход крестика
                move(area, 'X')
            else:                                                   # Ход нолика
                move(area, '0')

            if turn >= 3 and check_if_win(area, "X"):               # Проверка крестика на победителя
                winner('X')
                return
            elif turn >= 3 and check_if_win(area, "0"):             # Проверка нолика на победителя
                winner('0')
                return
        print("Game over")                                          # Ничья

    except KeyboardInterrupt:                                       # Обработка исключения при досрочном выходе из игры
        print("\nBye-bye")


main()
