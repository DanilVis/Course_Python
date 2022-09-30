# 4.Реализуйте алгоритм перемешивания списка.

import random

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
length = len(numbers_list)

# random.shuffle(numbers_list)
# print(numbers_list)

for i in range(length):
    r = random.randrange(length)
    (numbers_list[i], numbers_list[r]) = (numbers_list[r], numbers_list[i])
print(numbers_list)