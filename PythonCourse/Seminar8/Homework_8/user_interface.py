from contacts_op import get_columns
from input_data import add_contact, input_column
from contacts_op import find_contact, read_data, add_column, write_data, delete_contact, edit_contact
from export_database import export_data
from view import show_data


def user_interface():
    data = read_data()
    columns = get_columns(data)
    flag = True
    while flag: 
        print("\n** Главное меню **\n\nВыберите пункт меню для продолжения:")
        while True:
            print("1 - Найти контакт")
            print("2 - Добавить контакт")
            print("3 - Редактировать контакт")
            print("4 - Удалить контакт")
            print("5 - Показать все контакты")
            print("6 - Добавить столбец")
            print("7 - Экспорт данных")
            print("0 - Выход")
            choice = input()
            if choice not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
                print("!!Выбран неверный пункт меню!!\nПопробуйте ещё раз")
                continue
            if choice == "1": 
                find_contact(data)
                break
            elif choice == "2":
                add_contact(data, columns)
                break
            elif choice == "3":
                edit_contact(data)
                break
            elif choice == "4":
                delete_contact(data)
                break
            elif choice == "5":
                print(*columns)
                show_data(data)
            elif choice == "6":
                column = input_column()
                data = add_column(data, column, columns)
            elif choice == "7":
                export_data(data, columns)
                break
            else: 
                flag = False
                write_data(data, columns)
                break
