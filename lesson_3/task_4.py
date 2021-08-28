import os
import random
import string


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            print(line)


def write_file(file_name):
    path = os.path.join(os.getcwd(), file_name)
    words = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(4, 10))) for _ in range(5)]
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


write_file('1.txt')
