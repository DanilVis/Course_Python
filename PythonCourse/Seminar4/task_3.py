# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
## Вариант 0
from math import gcd


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

print(num1 * num2 // gcd(num1, num2))

## Вариант 1 - через поиск делителей
def find_divisors(n):
    divisors = []
    for i in range(2, n + 1):
        while n % i == 0:
            divisors.append(i)
            n = n // i
    return divisors


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

num1_divisors = find_divisors(num1)
num2_divisors = find_divisors(num2)

res = num2
for i in num1_divisors:
    if i not in num2_divisors:
        res *= i
    elif num1_divisors.count(i) > num2_divisors.count(i):
        res *= i
        num1_divisors.remove(i)

print(res)

## Вариант 2 - перебором чисел
def calculate_lcm(x, y):
# selecting the greater number
    if x > y:
        greater = x
    else: greater = y
    while(True):
        if((greater % x == 0) and(greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


# taking input from users
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# printing the result for the users
print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2))