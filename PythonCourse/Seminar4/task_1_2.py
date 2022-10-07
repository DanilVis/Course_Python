# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# Вариант 2

# проверка, что в списке только числа
def check(line):
    arr = line.split()
    for i in arr:
        if not i.strip('-').isdigit(): # не считать -, чтобы пропускало отрицательные числа.
            return []
    return arr


def min_max(array):
    if array:
        return min(array, key=int), max(array, key=int)
    return []


f = check('3 25 6 -5 40')
print(min_max(f))