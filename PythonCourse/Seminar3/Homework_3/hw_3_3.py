# Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

num_list = [1.1, 1.2, 3.1, 5, 10.01]
max_num = num_list[0] % 1
min_num = num_list[0] % 1

for i in num_list:
    if i % 1 > max_num:
        max_num = i % 1
    elif i % 1 < min_num:
        min_num = i % 1

print(max_num - min_num)

# Вариант 2 - через функции min, max
num_list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = [round(i % 1, 2) for i in num_list] # if i%1 != 0 - можно добавить в квадратные скобки, чтобы исключить целые числа без дробной части
print(max(new_list) - min(new_list))
