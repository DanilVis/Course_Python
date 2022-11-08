import json


def export_data(data, columns):
    new_file_name = input("Введите имя файла: ")
    file_format = input("Введите нужный формат файла (csv, txt, json): ")
    if file_format == "csv" or file_format == "txt":
        export_text(new_file_name, file_format, data, columns)
    if file_format == "json":
        export_json(new_file_name, data)
    else:
        print("Формат файла введен неверно или не поддерживается")


def export_json(name, data):
    f_name = name + ".json"
    try:
        data_dict = {}
        data_dict["Contacts"] = data
        with open(f_name, 'w', encoding="UTF-8") as export_file:
            json.dump(data_dict, export_file, indent=4, ensure_ascii=False)
        print("Файл был сохранен.")
    except:
        print("Недопустимое имя файла")


def export_text(name, format, data, columns):
    f_name = name + "." + format
    try:
        with open(f_name, "w", encoding="UTF-8") as f:
            f.write(", ".join(columns) + "\n")
            for user in data: 
                f.write(", ".join(user.values()) + "\n")
        print("Файл был сохранен.")
    except:
        print("Недопустимое имя файла.")
