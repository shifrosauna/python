# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

digits = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open('file_task04.txt', 'r') as my_file:
    for line in my_file:
        line = line.split(' ', 1)
        new_list.append(digits[line[0]] + ' ' + line[1])
    print(new_list)

with open('file_task04_fin.txt', 'w') as my_file:
    my_file.writelines(new_list)
