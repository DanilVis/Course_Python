# Вычислить число c заданной точностью d

from decimal import Decimal


entered_num = Decimal(input('Введите число: '))
d = Decimal(input('Введите необходимую точность в формате "0.001": '))
entered_num = entered_num.quantize(d)
print(entered_num)

