# Входные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Перевод множества в список и его сортировка
students = list(students)
students.sort()
# Создание словаря
DictOfStudentsAVGGrades = dict()
# Рассчет среднего балла и добавление студента с оценкой в словарь
for i in range(5):
    grades[i] = sum(grades[i]) / len(grades[i])
    DictOfStudentsAVGGrades.update({students[i]: grades[i]})
# Вывод получившегося словаря
print(DictOfStudentsAVGGrades)
