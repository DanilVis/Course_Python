FILE_NAME = "Phonebook.csv"


from os.path import exists


def create_phonebook():
    if not exists(FILE_NAME):
        with open(FILE_NAME, 'w', encoding="UTF-8") as f:
            f.write("Фамилия,Имя,Телефон,Комментарий\n")


def read_from_phonebook():
    with open("G:/Seminars/Python/Phonebook.csv", 'r', encoding="UTF-8") as f:
        data = f.read().split()[1:]
        if len(data) < 1:
            return []
        data_list = []
        keys = ["Фамилия", "Имя", "Телефон", "Комментарий"]
        for line in data:
            line = line.split(",")
            data_list.append(dict(zip(keys, line)))
        return data_list


def write_in_phonebook(data):
    with open(FILE_NAME, 'a', encoding="UTF-8") as f:
        f.write(",".join(data) + "\n")
