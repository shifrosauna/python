# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

while True:
    length_list = input('Введите количество элементов списка:')
    if length_list.isdigit():
        length_list = int(length_list)
        break
    print('ошибка ввода, это не число')
i = 0
j = 0
first_list = []
while i < length_list:
    first_list.append(input(f"Введите {i} элемент списка:"))
    i += 1
print("Исходный список:\n", first_list)

for j in range(1, len(first_list), 2):
    first_list[j - 1], first_list[j] = first_list[j], first_list[j - 1]

print("Измененный список:\n", first_list)
