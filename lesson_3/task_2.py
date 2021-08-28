def print_number():
    num = input('input a number: ')
    try:
        if int(num):
            print(f'You input a number: {num}')
    except ValueError:
        pass
    num_list = list(str(num))
    for i in num_list:
        if i == ".":
            try:
                float_num = float("".join(map(str, num)))
                if float_num:
                    list_from_float = str(float_num).split('.')
                    if int(list_from_float[0]) == int(list_from_float[1]):
                        print(True)
                    else:
                        print(False)
            except ValueError:
                pass


print_number()

