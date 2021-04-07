def salary(hours, rate, bonus):
    try:
        hours = int(hours)
        rate = int(rate)
        bonus = int(bonus)
        return hours * rate + bonus

    except ValueError:
        print('Не целое число!')
        exit()
