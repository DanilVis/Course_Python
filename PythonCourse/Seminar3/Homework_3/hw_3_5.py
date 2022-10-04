# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))
fibonacci = [0, 1]

for i in range(1, n):
    fibonacci.append(fibonacci[i] + fibonacci[i - 1])
for j in range(-1, -n, -1):
    fibonacci.insert(0, fibonacci[1] - fibonacci[0])

print(fibonacci)
