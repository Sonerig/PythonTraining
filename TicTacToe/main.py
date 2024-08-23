def draw_area(area):
    print("-" * 13)
    for i in range(len(area)):
        print("|", area[i][0], "|", area[i][1], "|", area[i][2], "|")
        print("-" * 13)
    print("=" * 56)


def check_if_win(area, current_turn):

    for row_column in range(3):
        if area[row_column][row_column] != current_turn:
            break
        elif row_column == len(area) - 1:
            return True

    for row_column in range(3):
        if area[row_column][len(area) - row_column - 1] != current_turn:
            break
        elif row_column == len(area) - 1:
            return True

    for row in range(3):
        for column in range(3):
            if area[row][column] != current_turn:
                break
            elif column == len(area) - 1:
                return True

    for column in range(3):
        for row in range(3):
            if area[row][column] != current_turn:
                break
            elif row == len(area) - 1:
                return True

    return False


def update_area(area, turn):
    try:
        row = int(input("Enter the row: ")) - 1
        column = int(input("Enter the column: ")) - 1
    except ValueError:
        print("Invalid number (you can use: 1, 2, 3)")
        print("=" * 56)
        return update_area(area, turn)
    if (row < 0 or row >= 3) or (column < 0 or column >= 3):
        print("The row or column can not be more than 3 and less than 1")
        print("=" * 56)
        return update_area(area, turn)
    if area[row][column] != '#':
        print("This cell is already busy")
        print("=" * 56)
        return update_area(area, turn)

    area[row][column] = turn
    print("=" * 56)


def main():
    print("Wellcome to Tic-Tak game!")
    print("=" * 56)
    try:
        area = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]
        draw_area(area)
        for turn in range(9):
            if turn % 2 == 0:
                print("X turn!")
                print("=" * 56)
                update_area(area, 'X')
            else:
                print("0 turn!")
                print("=" * 56)
                update_area(area, '0')

            draw_area(area)

            if check_if_win(area, "X"):
                print("X win!")
                print("=" * 56)
                return
            elif check_if_win(area, "0"):
                print("0 win!")
                print("=" * 56)
                return
    except KeyboardInterrupt:
        print("\nBye-bye")
    print("Game over")


main()
