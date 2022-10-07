# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# num_list = [15, 32, 18, 4, 9, -5, 32.9]
# num_list = [int(i) for i in input('Введите числа через пробел: ').split()] # list comprehension
num_list = list(map(int, input("Введите числа через пробел:\n").split()))
print(max(num_list), min(num_list))
