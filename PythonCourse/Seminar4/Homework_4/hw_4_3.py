# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

# Вариант 1 - через список
# num_list = list(map(int, input('Введите числа через пробел: ').split()))

# unique_nums = []
# for i in num_list:
#     if num_list.count(i) == 1:
#         unique_nums.append(i)
# print(unique_nums)

# Вариант 2 - через словарь, более оптимально
from collections import Counter


num_list = list(map(int, input('Введите числа через пробел: ').split()))

# count_dict = {}
# for i in num_list:
#     if not i in count_dict:
#         count_dict[i] = 0
#     count_dict[i] += 1
count_dict = Counter(num_list)

# res_list = []
# for i in count_dict:
#     if count_dict[i] == 1:
#         res_list.append(i)
res_list = [i for i in count_dict if count_dict[i] == 1]
print(res_list)

# 3 Вариант
from collections import Counter


num_list = list(map(int, input('Введите числа через пробел: ').split()))
output_list = [k for k, v in Counter(num_list).items() if v == 1]
print(output_list)
