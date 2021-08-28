import os
import random
import re
import string


def read_file(file_name):
    with open(os.path.join(os.getcwd(), 'new.txt'), 'w', encoding='utf-8') as f:
        with open(file_name, encoding='utf-8') as old_f:
            for el in old_f:
                if re.match('^[a-z]{4,7}[0-9]{4}$', el):
                    print(f'найдены вхождения: {el}')
                    f.write(el.replace(el, '*****replaced*****'))
                    f.write('\n')
                else:
                    f.write(el)
                    f.write('\n')
    os.rename('new.txt', file_name)
    with open(file_name, 'r', encoding='utf-8') as file:
        print('вывод строк соответствующих регулярному выражению:')
        my_list = []
        for elem in file:
            if re.match('example345', elem):
                my_list.append(elem)
                print(f'вывод соответствующей строки: {elem}')
        if not my_list:
            print('соответствия регулярному выражению не найдены')


def write_file(file_name):
    path = os.path.join(os.getcwd(), file_name)
    words = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 9))) for _ in range(5)]
    for i in range(len(words)):
        words[random.randint(i, len(words)-1)] = 'example345'
    numbers = [random.randint(1000, 10000) for _ in range(5)]
    str_list = list(f"{k}{str(v)}" for k, v in zip(words, numbers))
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            for i in str_list:
                f.write(i)
                f.write('\n')

        read_file(file_name)
    else:
        print(f'File {file_name} already exists, choose another file name for writing.')


write_file('2.txt')
