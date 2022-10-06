# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

entered_num = int(input('Введите число: '))
# print(format(entered_num, 'b'))
# или
# print(bin(entered_num)[2:])

result = ''
while entered_num != 0:
    result = str(entered_num % 2) + result
    entered_num //= 2

print(result)
