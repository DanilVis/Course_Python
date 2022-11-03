

def get_add_key(data):
    user = input('Введите название нового поля')
    for x in data:
        x[user] = '*'
    return data
