my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
iteration = 0
while True:
    if my_list[iteration] < 0 or iteration == len(my_list):
        break
    print(my_list[iteration])
    iteration += 1
