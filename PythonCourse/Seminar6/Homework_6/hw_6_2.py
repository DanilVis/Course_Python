# 2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];

num_list = list(map(int, input('Введите числа через пробел: ').split()))
length = len(num_list) // 2 + len(num_list) % 2
results_list = [num_list[i] * num_list[- i - 1] for i in range(length)]

print(results_list)
