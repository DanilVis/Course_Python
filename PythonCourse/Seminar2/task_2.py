# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности
# 3n + 1.

n = int(input('Введите число N: '))
d = dict() # d = {}
j = 1
for i in range(n):
    d[j] = 3 * j + 1
    j += 1
print(d)