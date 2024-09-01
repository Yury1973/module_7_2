"""
Задача "Записать и запомнить"
"""


def custom_write(file_name, strings):
    i = 0
    strings_positions = {}
    for i in range(0, len(strings)):
        i += 1
        file = open(file_name, 'a', encoding='utf-8')
        curs_pos = file.tell()
        file.write(strings[i - 1] + '\n')
        strings_positions[(i, curs_pos)] = strings[i - 1]
        file.close()
    return i and strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
