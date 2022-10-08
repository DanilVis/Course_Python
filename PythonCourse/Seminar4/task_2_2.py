# Найдите корни квадратного уравнения с помощью модуля.
# Уравнения и корни запишите в файл.
from math import sqrt


def abc(a, b, c):
    D = b ** 2 - 4 * a * c
    with open('G:\\Seminars\\Python\\PythonCourse\\Seminar4\\result.txt', 'a', encoding='utf8') as my_f:
        my_f.write(f'{a}x^2 + {b}x + {c} = 0\n')
        if D > 0 and a:
            my_f.write(str((-b + sqrt(D)) / (2 * a)) + '\n')
            my_f.write(str((-b - sqrt(D)) / (2 * a)) + '\n')
        elif D == 0 and a:
            my_f.write(str(-b / (2 * a)) + '\n')
        else:
            my_f.write('Нет корней\n')

for i in range(3):
    abc(int(input()), int(input()), int(input()))