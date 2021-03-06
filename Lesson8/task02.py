# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    pass


def get_numerator() -> int:
    return int(input("Введите числитель:"))


def get_denominator() -> int:
    value = int(input("Введите знаменатель:"))

    if value == 0:
        raise MyZeroDivisionError

    return value


try:
    numerator = get_numerator()
    denominator = get_denominator()
    print(f"{numerator}/{denominator} = {numerator / denominator}")
except MyZeroDivisionError:
    print("Делить на ноль нельзя!")
