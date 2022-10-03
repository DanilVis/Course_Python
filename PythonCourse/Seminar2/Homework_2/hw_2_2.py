# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input('Введите число: '))

# for i in range(1, n + 1):
#     result = 1
#     while i > 1:
#         result *= i
#         i -= 1
#     print(result, end = ' ')

# Исправленно:
n = int(input('Введите число: '))
result = 1

for i in range(1, n + 1):
    result *= i
    print(result, end = ' ')
#__________________________________________

# Вариант 2 - с добавлением в список (меньше операций)
# n = int(input('Введите число: '))
# prod = 1
# result_list = []

# for i in range(1, n + 1):
#     prod *= i
#     result_list.append(prod)
# print(result_list)