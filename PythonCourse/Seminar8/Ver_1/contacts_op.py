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
        if len(data.split()) < 2:
            return []
        columns = data[0].strip().split(", ")  # строка с заголовком 
        data = [{columns[i]: user.strip().split(", ")[i] for i in range(len(columns))} for user in data.split()[1:]]
        return data


def get_columns(data):
    if not data: 
        return ["Фамилия", "Имя"]
    columns = data[0].keys()
    return columns


def find_contact(data):
    column = input("Введите столбец поиска: ")
    val = input("Введите значение для поиска: ")
    flag = False
    for user in data:
        if column not in user:
            return "Такого столбца нет!"
        if user[column] == val: 
            print(user)
            flag = True
    if not flag: 
        print("Данные не найдены!")


FILE_NAME = "data_base.csv"
# valid = exists(FILE_NAME)
# if not valid:
#     creat_csv() 
