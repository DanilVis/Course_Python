# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

num_list = list(map(int, input('Введите числа через пробел: ').split()))

unique_nums = []
for i in num_list:
    if num_list.count(i) == 1:
        unique_nums.append(i)
print(unique_nums)

