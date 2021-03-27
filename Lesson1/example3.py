# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int(input("Введите число:"))

nn = int(str(n) + str(n))
nnn = int(str(nn) + str(n))
summ = n + nn + nnn
print(f"{n} + {nn} + {nnn} = {summ}")
