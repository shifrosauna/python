# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(*args):
    """
    Деление числа args[0] на число args[1]

    :param args: Делимое args[0]  типа float;  Делитель args[1] типа float
    :return: res = args[0]/args[1]
    :rtype: float
    """

    try:
        res = args[0] / args[1]
    except ZeroDivisionError:
        return "Делениена ноль!"

    return res


try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
except ValueError:
    print("Введено не число!")
    exit()

print(division(a, b))
