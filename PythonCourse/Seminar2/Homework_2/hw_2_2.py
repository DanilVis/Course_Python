# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число: '))

for i in range(1, n + 1):
    result = 1
    while i > 1:
        result *= i
        i -= 1
    print(result, end = ' ')