# 1. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
lines = ['Egor Иванович Иванов\n', 'Kagor сладкое вино\n', 'Minor мажор \n']
with open("file_task02.txt", 'w+') as my_file:
    my_file.writelines(lines)
with open("file_task02.txt") as my_file:
    lines = 0
    words_in_line = 0
    for line in my_file:
        print(f"В строке № {lines + 1} содержится {len(line.split())} слов.")
        lines += 1
    print(f"Строк в файле: {lines}")
