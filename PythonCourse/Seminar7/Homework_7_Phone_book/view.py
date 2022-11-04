def print_phonebook():
    with open('Phonebook.csv', 'r', encoding="UTF-8") as f:
        phonebook = f.read().replace(",", " ")
        print(phonebook)

def search():
    with open('Phonebook.csv', 'r', encoding="UTF-8") as f:
        phonebook = f.read().split()[1:]
        text = input("Введите, что вы хотите найти: ")
        for line in phonebook:
            if text in line:
                print(line.replace(",", " "))
                flag = True
        if not flag:
            print("Такой записи не найдено")

