# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

input_string = input("Введите строку:")
i = 1
for value in input_string.split():
    value = value if len(value) <= 10 else value[0:10]
    print(i, value)
    i += i