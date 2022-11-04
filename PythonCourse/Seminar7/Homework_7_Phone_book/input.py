from data_op import write_in_phonebook


def add_contact():
    while True:
        contact = {}
        contact["Фамилия"] = input("Введите фамилию: ")
        contact["Имя"] = input("Введите имя: ")
        contact["Телефон"] = input("Введите телефон: ")
        contact["Комментарий"] = input("Введите комментарий: ")
        for k, v in contact.items():
            if not v:
                contact[k] = "-"
        write_in_phonebook(contact.values())
        new_contact = input("Если хотите добавить еще одну запись, введите 1: ")
        if new_contact:
            continue
        else:
            return
