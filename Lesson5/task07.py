# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.

import json

with open('file_task07.txt', 'r') as my_file:
    tem_list = my_file.read().split('\n')

firm_dict = {}
average_profit = {}
count_firm = 0
summ_pribili = 0
for i in tem_list:
    firma = i.split()
    # Если прибыль < 0 ==> это убыток. Добавляем также в словарь.
    firm_dict[firma[0]] = (int(firma[2]) - int(firma[3]))
    if firm_dict[firma[0]] > 0:
        count_firm += 1
        summ_pribili = summ_pribili + firm_dict[firma[0]]

average_profit['average_profit'] = summ_pribili / count_firm
fin_list = [firm_dict, average_profit]
print(fin_list)

with open("my_file_task07.json", "w") as write_f:
    json.dump(fin_list, write_f)


