# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input('Введите число: ')
result = 0

for i in number:
    if i.isdigit() == False:
       continue
    result += int(i)
print(result)
