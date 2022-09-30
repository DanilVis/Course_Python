# 3.Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('Введите число: '))
numbers = []

for i in range (1, n + 1):
    num = round((1+1/i)**i, 2)
    numbers.append(num)
print(numbers)
print(sum(numbers))