# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# cумму этих чисел к полученной ранее сумме и после этого завершить программу.

def summa_function(string_num):
    """
    Функция принимает строку. Переводит в список вещественных чисел до символа Q или q.
    И ссумирует данный список. Если в строке был символ Q то передает exit_code = False, иначе exit_code = True
    :param string_num: Строка
    :return: сумму чисел до символо Q и наличие символа Q в исходной строке.
    """

    numbers = string_num.split()
    fin_numbers = []
    exit_code = True
    for value in numbers:
        if value.lower() == 'q':
            exit_code = False
            break;
        else:
            fin_numbers.append(float(value))
    summa_numbers = sum(fin_numbers)
    return summa_numbers, exit_code


def main_func():
    """
    Функция которая принимает строки с числавми и суммирует их до тех пор пока не найдет символ остановки 'Q'
    :return: None
    """
    exit_code = True
    summ = 0
    while exit_code:
        string_num = input("Введите строку чисел через пробел(для выхода наберите символ 'Q' или 'q'):")
        temp_summa, exit_code = summa_function(string_num)
        summ = summ + temp_summa
        print("Сумма чисел = ", summ)


main_func()
