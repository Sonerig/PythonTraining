def get_multiplied_number(number):
    number = str(number).replace('0', '')
    if len(number) > 1:
        return int(number[0]) * get_multiplied_number(int(number[1:]))
    return int(number[0])


print(get_multiplied_number(int(input("The num: "))))
