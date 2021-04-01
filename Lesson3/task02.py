# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строк


def my_func(**kwargs):
    """
    Функция получает именнованные параметры и выводит их значения в одну строку
    :param kwargs: Словарь с данными
    :return: Строку значений словаря
    :rtype: str
    """
    return f"{kwargs.pop('name')} {kwargs.pop('surname')} {kwargs.pop('year')} {kwargs.pop('city')} {kwargs.pop('email')} {kwargs.pop('telephone')}"


name = input('Введите имя:')
surname = input('Введите фамилию:')
year = int(input('Введите год рождения:'))
city = input('Введите город проживания:')
email = input('Введите email')
telephone = input('Введимте телефон:')

print(my_func(name=name, surname=surname, year=year, city=city, email=email, telephone=telephone))
