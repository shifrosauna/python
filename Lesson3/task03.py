# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(*args):
    """
    Принимает 3 позиционных аргумента и возвращает сумму наибольших двух
    :param args: 3 числа
    :return: сумма наибольших двух
    :rtype: str
    """
    new_list = []
    for value in args:
        new_list.append(value)
    new_list.remove(min(new_list))
    return new_list[0] + new_list[1]


a = float(input("Введите число №1:"))
b = float(input("Введите число №2:"))
c = float(input("Введите число №3:"))
print("Сумма наибольших бвух чисел:", my_func(a, b, c))
