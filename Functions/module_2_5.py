def get_matrix(n, m, value):                            # Функция создания матрицы
    matrix = list()                                     # Создание списка
    for i in range(n):
        matrix.append(list())                           # Создание вложенного списка (двумерный список)
        for j in range(m):
            matrix[i].append(value)                     # Добавление во вложенный список значение value - "#"
    return matrix                                       # Возвратное значение - готовая матрица


def print_matrix(matrix):                               # Функция вывода матрицы удобного для вида
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], ' ', sep='', end='')    # Вывод каждого элемента строки через пробел
        print('\n', end='')                             # Перевод строки


def main():                                             # Главная функция
    n = int(input("Введите количество строк: "))        # Ввод количества строк
    m = int(input("Введите количество столбцов: "))     # Ввод количества столбцов

    print_matrix(get_matrix(n, m, '#'))                 # Вызов функции вывода матрицы (в параметрах создание матрицы)


main()                                                  # Программа начинается с вызова функции "main"
