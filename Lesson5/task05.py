# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open("file_task05.txt", 'w+') as my_file:
    line = input('Введите цифры через пробел \n')
    my_file.writelines(line)
    my_file.seek(0)
    numbers = my_file.readline().split()
    print(sum(map(int, numbers)))
