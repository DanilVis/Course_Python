# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0, и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите координату x: '))
y = int(input('Введите координату y: '))

if x > 0 and y > 0:
    print(f'x = {x}, y = {y} -> I')
elif x < 0 and y > 0:
    print(f'x = {x}, y = {y} -> II')
elif x < 0 and y < 0:
    print(f'x = {x}, y = {y} -> III')
elif x > 0 and y < 0:
    print(f'x = {x}, y = {y} -> IV')
else:
    print('Ошибка')