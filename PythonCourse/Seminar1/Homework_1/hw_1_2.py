# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. (¬ отрицание, ∧ и, ∨ или)

print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            result = not (x or y or z) == (not x and not y and not z)
            print(x, y, z, result)
