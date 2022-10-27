# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'вабвг где нам гдабв неабв кнтр абвуку впрн'.split()
result = " ".join(filter(lambda x: 'абв' not in x, text))
print(result)
