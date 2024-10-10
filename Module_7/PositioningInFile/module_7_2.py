def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding="utf8")
    strings_positions = dict()
    for counter in range(len(strings)):
        strings_positions.update({(counter + 1, file.tell()): strings[counter]})
        file.write(strings[counter] + '\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
