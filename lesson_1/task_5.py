def deposit_calculation():
    print('Расчет банковского вклада.')
    rub = int(input('Введите сумму вклада: '))
    while rub < 1000 or rub > 1000000:
        print('Сумма вклада не может быть меньше 1 000 руб. и не может превышать 1 000 000 руб.')
        rub = int(input('Введите сумму вклада: '))
    period = int(input('Введите срок на который вы хотите разместить вклад.\nвведите 6 (на срок 6 месяцев)\nвведите 12 (на срок 12 месяцев)\nвведите 24 (на срок 24 месяца): '))
    while period not in [6, 12, 24]:
        print('Вы выбрали недоступный срок вклада. Доступные сроки: 6, 12 или 24.')
        period = int(input('Введите срок на который вы хотите разместить вклад.\nвведите 6 (на срок 6 месяцев)\nвведите 12 (на срок 12 месяцев)\nвведите 24 (на срок 24 месяца): '))
    deposit_options = [
        {'start_sum': 1000, 'end_sum': 10000, '6': '5%', '12': '5.5%', '24': '5%'},
        {'start_sum': 10000, 'end_sum': 100000, '6': '6%', '12': '7%', '24': '7.5%'},
        {'start_sum': 100000, 'end_sum': 1000000, '6': '7%', '12': '8%', '24': '7.5%'}
    ]

    def additional_payment(bank_rate):
        month_sum = int(input('введите сумму ежемесячного пополнения, руб.: '))
        additional_percents = 0
        payment_sum = 0
        for _ in range(1, period - 1):
            additional_percents += month_sum * bank_rate / 100
            payment_sum += month_sum + additional_percents
        print(f'сумма ежемесясных пополнений с процентами: {round(payment_sum)} руб.')
        return payment_sum

    for option in deposit_options:
        if rub in range(option['start_sum'], option['end_sum']):
            for k in option.keys():
                if str(period) == k:
                    deposit_sum = rub * (1 + int(option[k][0]) / 100 / 12)**period
                    sum_percent = round(deposit_sum) - rub
                    print(f'Результаты расчета:\nпервоначальная сумма вклада: {rub} руб;\n'
                          f'срок вклада: {period} месяцев;\nначисленные проценты: {sum_percent} руб;\n'
                          f'сумма с процентами по истечению срока вклада: {round(deposit_sum)} руб.')
                    res = additional_payment(int(option[k][0]))
                    print(f'Итогова сумма выплат: {round(deposit_sum) + round(res)} руб.')


deposit_calculation()


