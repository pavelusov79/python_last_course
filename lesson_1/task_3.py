import random


def random_numbers():
    start_range = int(input('Введите целое число - начало диапазона: '))
    while start_range == 0:
        print('Начало диапазона не может начинаться с нуля.')
        start_range = int(input('Введите целое число - начало диапазона: '))
    end_range = int(input('Введите целое число - конец диапазона: '))
    while end_range < start_range:
        print('Конец диапазона должен быть больше чем начало диапазона.')
        end_range = int(input('Введите целое число конец диапазона: '))
    random_list = []
    random_dict = {}
    for i in range(start_range, end_range):
        random_number = random.randrange(start_range, end_range)
        if random_number == 0 or i == 0:
            continue
        random_list.append(random_number)
        random_dict['elem_' + str(i)] = random_number

    print(f'случайный список чисел = {random_list}')
    print(f'случайный словарь чисел = {random_dict}')


random_numbers()
