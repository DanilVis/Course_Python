# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов. (умножаем на -3)
# Пример: Для N = 5: 1, -3, 9, -27, 81

# number = int(input('Введите число: '))
# result = []
# a = 1

# for i in range(number):
#     result.append(a)
#     a *= -3

# print(result)
# ________________________________________________

# Вариант 2 - вывод строкой
number = int(input('Введите число: '))
result = []
a = 1

for i in range(number):
    result.append(str(a))
    a *= -3

print(', '.join(result)) # вывод элементов массива строкой через разделитель ', '