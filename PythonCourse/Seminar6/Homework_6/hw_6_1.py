# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

from collections import Counter


num_list = list(map(int, input('Введите числа через пробел: ').split()))
unique_nums = [i for i, v in Counter(num_list).items() if v == 1]
print(unique_nums)