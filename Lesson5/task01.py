# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

lines = []
line = True
while True:
    if not line:
        lines.pop(len(lines) - 1)
        break
    line = input('Введите строку\n')
    lines.append(line + '\n')

print(lines)
my_file = open('task01.txt', 'w')
my_file.writelines(lines)
my_file.close()
