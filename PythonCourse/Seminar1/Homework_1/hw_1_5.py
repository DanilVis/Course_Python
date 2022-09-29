# 5.Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

x_1 = float(input('Введите координату точки x1: '))
y_1 = float(input('Введите координату точки y1: '))
x_2 = float(input('Введите координату точки x2: '))
y_2 = float(input('Введите координату точки y2: '))

points_distance = ((x_1 - x_2)**2 + (y_1 - y_2)**2) **0.5
print(round(points_distance, 2))
# _______________________________________________________________________

# Вариант 2 - с использованием функции sqrt

# from math import sqrt

# ax = float(input('Enter the x coordinate of the point A: '))
# ay = float(input('Enter the y coordinate of the point A: '))

# bx = float(input('Enter the x coordinate of the point B: '))
# by = float(input('Enter the y coordinate of the point B: '))

# distance_2d = round(sqrt((bx - ax) ** 2 + (by - ay) ** 2), 2)
# print(distance_2d)