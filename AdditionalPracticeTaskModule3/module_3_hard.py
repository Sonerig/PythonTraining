def sum_of_data_struct(*data, **dict_data):
    result = 0

    for key, value in dict_data.items():
        result += len(key) + value

    for i in data:
        if isinstance(i, str):
            result += len(i)
        elif isinstance(i, dict):
            result += sum_of_data_struct(**i)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            result += sum_of_data_struct(*i)
        else:
            result += i
    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(sum_of_data_struct(*data_structure))
