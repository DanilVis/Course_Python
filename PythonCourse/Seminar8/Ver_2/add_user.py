

def get_add_user(data):
    if not data:
        user = {}
        user['FIO'] = input('Введите ФИО')
    else:
        a = data[0]
        user = {}
        for i in a:
            user[i] = input(f'Введите {i}')

    data.append(user)
    return data
