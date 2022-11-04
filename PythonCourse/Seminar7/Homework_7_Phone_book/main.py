from data_op import create_phonebook, read_from_phonebook
from input import add_contact
from view import print_phonebook, search
from export import export_to_csv, export_to_txt, export_to_json


def menu():
    create_phonebook() 
    while True: 
        print("\n**Главное меню**")
        print("1 - Показать все записи")
        print("2 - Найти запись")
        print("3 - Добавить новую запись")
        print("4 - Экспортировать данные")
        print("0 - Выход")
        choice = input("Выберите пункт меню: ")
        if choice not in ["0", "1", "2", "3", "4"]:
            print("Введите правильный номер пункта меню")
            continue
        if choice == "1": 
            print_phonebook()    
        elif choice == "2":
            search()    
        elif choice == "3":
            add_contact()    
        elif choice == "4":
            print("\nЭкспорт данных")
            print("1 - Экспортировать в csv")
            print("2 - Экспортировать в txt")
            print("3 - Экспортировать в json")
            print("0 - Вернуться в главное меню")
            format_choice = input("Выберите формат: ")
            if format_choice == "1":
                export_to_csv()
            elif format_choice == "2":
                export_to_txt()
            elif format_choice == "3":
                phonebook = read_from_phonebook()
                export_to_json(phonebook)
            elif format_choice == "0":
                continue
            else:
                print("Неверное значение. Вы вернетесь в главное меню")
        else: 
            exit()


if __name__ == "__main__":
    menu()