# 2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];

num_list = [2, 3, 4, 5, 6, 7, 8]
length = len(num_list) // 2 + 1
results_list = []

for i in range(length):
    nums_product = num_list[i] * num_list[- i - 1]
    results_list.append(nums_product)

print(results_list)
