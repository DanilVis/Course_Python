import menu
import jf
import add_key as ak


def data_comm():
    data = jf.read_file()
    exit = True
    while exit:
        what = menu.menu()
        if what == 1:
            get_выводить_базу()
        elif what == 2:
            ak.get_add_key(data)
        elif what == 3:
            get_add_user(data)
        elif what == 4:
            get_изменить_данные_пользователя()
        elif what == 5:
            get_поиск_данные_пользователя()
        else:
            jf.write_in_file(data)
            exit = False
