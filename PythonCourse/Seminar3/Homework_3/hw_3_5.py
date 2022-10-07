# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))
if n == 0:
    fibonacci = [0]
else:
    fibonacci = [1, 0, 1]

for i in range(1, n):
    fibonacci.append(fibonacci[i] + fibonacci[i + 1])
for j in range(-1, -n, -1):
    fibonacci.insert(0, fibonacci[1] - fibonacci[0])

print(fibonacci)

# Вариант 2 - в один цикл и без индексов
n = int(input('Введите число: '))
fibonacci = [0]
fib1 = fib2 = 1

for i in range(n):
    fibonacci.append(fib1)
    fibonacci.insert(0, fib1 * (-1) ** i)
    fib1, fib2 = fib2, fib1 + fib2

print(fibonacci)

## Вариант 3 - через рекурсию и с отдельными функциями
def fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def nega_fibonacci(n):
    list_negafibonacci = [0]
    for i in range(1, n + 1):
        list_negafibonacci.append(fibonacci(i))
        list_negafibonacci.insert(0, (fibonacci(i) * (-1) ** (i + 1)))
    return list_negafibonacci


n = int(input("Введите число: "))
print(f"Список чисел (нега)Фибоначчи для k = {n}: {nega_fibonacci(n)}")
