# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))

factors = []
for i in range(2, n + 1):
    while n % i == 0:
        factors.append(i)
        n = n // i

print(factors)