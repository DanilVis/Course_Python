# 5.Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# 7x^3 + 5x^2 + 6x^1 + 9

# Решение для положительных чисел
def polynomial_r(link):
    with open(link, 'r', encoding='utf-8') as poly:
        return poly.read()


def coefficients(poly_string):
    poly_string = poly_string.replace('x ', 'x^1 ')
    poly_string = poly_string.strip().replace(' = 0', '').split(' + ')
    coeff_dict = {}
    for i in poly_string:
        a, *b = i.split('x^')
        if b:
            coeff_dict[int(b[0])] = int(a)
        else:
            coeff_dict[0] = int(a)
    return coeff_dict


def poly_sum(dict1, dict2):
    for key in dict1:
        if not key in dict2:
            dict2[key] = 0
        dict2[key] += dict1[key]
    return dict2
    
  
def polynomial(res_dict):
    res_dict = sorted(res_dict.items())
    result = ''
    for i in res_dict:
        result = f' + {i[1]}x^{i[0]}' + result
    result = result.replace('^1', '')
    return result[3: -3] + ' = 0\n'


poly1 = polynomial_r('G:/Seminars/Python/PythonCourse/Seminar4/Homework_4/poly1.txt')
poly2 = polynomial_r('G:/Seminars/Python/PythonCourse/Seminar4/Homework_4/poly2.txt')
res_poly = poly_sum(coefficients(poly1), coefficients(poly2))

with open('G:/Seminars\Python/PythonCourse/Seminar4/Homework_4/poly_results.txt', 'a', encoding='utf8') as poly:
    poly.write(polynomial(res_poly))
polynomial(res_poly)




