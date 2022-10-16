# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'вабвг где нам гдабв неабв кнтр'
words_list = text.split()
result_list = []
for word in words_list:
    if 'абв' not in word:
        result_list.append(word)
print(" ".join(result_list))