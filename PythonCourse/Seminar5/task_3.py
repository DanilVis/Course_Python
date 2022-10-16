# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'вабвг где нам гдабв неабв кнтр'
result = text.split()
# for i in range(len(result)):
#     if 'абв' in result[i]:
#         result[i] = ''
# result = ' '.join(result).split() # чтобы убрать лишние пробелы
# result = ' '.join(result)
# print(result)

# Вариант 2
result_list = []
for word in result:
    if 'абв' not in word:
        result_list.append(word)
print(" ".join(result_list))