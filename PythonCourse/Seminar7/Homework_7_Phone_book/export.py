import json
from shutil import copyfile


def export_to_csv():
    f_name = input("Введите имя файла: ") + ".csv"
    try:
        copyfile("Phonebook.csv", f_name)
        print("Файл был сохранен.")
    except:
        print("Недопустимое имя файла")

def export_to_txt():
    f_name = input("Введите имя файла: ") + ".txt"
    try:
        copyfile("Phonebook.csv", f_name)
        print("Файл был сохранен.")
    except:
        print("Недопустимое имя файла")

def export_to_json(data):
    f_name = input("Введите имя файла: ") + ".json"
    try:
        book_data = {}
        book_data["Контакты"] = data
        with open(f_name, 'w', encoding="UTF-8") as export_file:
            json.dump(book_data, export_file, indent=4, ensure_ascii=False)
        print("Файл был сохранен.")
    except:
        print("Недопустимое имя файла")
