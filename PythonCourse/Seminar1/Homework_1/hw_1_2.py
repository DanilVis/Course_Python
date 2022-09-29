# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. (¬ отрицание, ∧ и, ∨ или)

print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            result = not (x or y or z) == (not x and not y and not z)
            print(x, y, z, result)
# ______________________________________________________

# Вариант 2 - без вывода всех значений
# i = 0
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not (not (x or y or z) == (not x and not y and not z)):
#                 i += 1
# if i: # if i != 0:
#     print('False')
# else:
#     print('All True')