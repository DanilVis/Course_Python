# Напишите программу, в которой пользователь будет задавать две строки, а программа - 
# определять количество вхождений одной строки в другой.

first_str = input('Введите первую строку: ')
second_str = input('Введите вторую строку: ')
i = first_str.count(second_str)

print(f'Вторая строка входит в первую {i} раз(а)')