# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

first_list = [1, 2.568, "test string", None, True, [5, 6, 9], (1, 0, 8), {2, 3, 6}, {'key_1': '1', 'key_2': '2'}]
print(first_list)
for i in first_list:
    print(type(i))
