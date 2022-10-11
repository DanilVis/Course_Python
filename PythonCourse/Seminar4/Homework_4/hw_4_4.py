# 4.Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint, choice


def polynomial(num_list):
    result = ''
    signs = ['+', '-']
    for i in range(len(num_list)):
        if num_list[i] != 0:
            result = f' {choice(signs)} {num_list[i]}x^{i}' + result
    result = result.replace('^1', '')
    if result[1] == '+':
        return result[3: -3] + ' = 0\n'
    elif result[1] == '-':
        return result[1: -3] + ' = 0\n'


k = int(input('Введите значение степени k: '))
coefficients = [randint(0, 101) for i in range(k + 1)]

with open('G:/Seminars/Python/PythonCourse/Seminar4/Homework_4/poly_results.txt', 'a', encoding='utf8') as poly:
    poly.write(polynomial(coefficients))
