def multi_table():
    table = []
    for i in range(1, 10):
        for j in range(1, 10):
            res = f'{i} * {j} = {i * j}'
            table.append(res)
    return table


def show_table(n, m):
    res = multi_table()
    for i in range(n):
        for j in range(m):
            print(res[i+n*j], end='   ')
        print()


show_table(9, 9)
