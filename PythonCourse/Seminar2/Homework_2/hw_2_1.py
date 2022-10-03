# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input('Введите число: ')
result = 0

for i in number:
    if i.isdigit():
       result += int(i)
print(result)
#__________________________________________

# Вариант 2 - математически
number = float(input('Введите число: '))

if number < 0:
    number *= -1 # Убираем минус у отрицательных

l = len(str(number)) - 1
num = int(number * 10 ** l) # Помогает избавиться от дробной части
sum_num = 0

while num != 0:
    sum_num += num % 10
    num = num // 10

print(sum_num)
