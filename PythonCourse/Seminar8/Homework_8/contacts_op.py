from asyncio import create_subprocess_shell
from dataclasses import dataclass
from os.path import exists


def write_contact(user, data):
    data.append(user)


def write_data(data, columns):
    with open(FILE_NAME, "w", encoding="UTF-8") as f:
      f.write(", ".join(columns) + "\n")
      for user in data: 
        f.write(", ".join(user.values()) + "\n")


def add_column(data, column, columns):
    for user in data: 
        user[column] = ""
    columns.append(column)
    return data
        

def read_data():
    valid = exists(FILE_NAME)
    if not valid: 
        return []
    with open(FILE_NAME, "r", encoding="UTF-8") as f: 
        data = f.read()
        if "\n" not in data:
            return []
        columns = data.split("\n")[0].strip().split(", ")  # строка с заголовком 
        user_list = data.strip().split("\n")[1:]
        data = [{columns[i]: user.split(", ")[i] for i in range(len(columns))} for user in user_list if user]
        return data


def get_columns(data):
    if not data: 
        return ["Фамилия", "Имя"]
    columns = list(data[0].keys())
    return columns


def find_contact(data):
    column = input("Введите столбец поиска: ")
    val = input("Введите значение для поиска: ")
    # print([x for x in data if x[column] == val][0])
    flag = False
    for user in data:
        if column not in user:
            return "Такого столбца нет!"
        if user[column] == val: 
            print(user)
            flag = True
    if not flag: 
        print("Данные не найдены!")


def delete_contact(data):
    del_cont = input("Введите данные контакта, который хотите удалить: ")
    for user in data:
        if del_cont in user.values():
            confirm = input(f"{user} будет удален. Введите 1 для продолжения: ")
            if confirm == "1":
                data.remove(user)
                print("Контакт удален")
            confirm2 = input(f"Продолжить поиск? Введите 1 для продолжения: ")
            if confirm2 != "1":
                return
    print("Контакты с такими данными не найдены")


def edit_contact(data):
    ed_cont = input("Введите данные контакта, который хотите отредактировать: ")
    flag = False
    for user in data:
        if ed_cont in user.values():
            flag = True
            confirm = input(f"{user} будет отредактирован. Введите 1 для продолжения: ")
            if confirm == "1":
                while True:
                    field = input("Введите название поля, которое хотите отредактировать или 0 для выхода: ")
                    if field == "0":
                        return
                    user[field] = input("Введите новое значение: ")
    if not flag: 
        print("Данные не найдены!")

FILE_NAME = "data_base.csv"
# valid = exists(FILE_NAME)
# if not valid:
#     creat_csv() 
