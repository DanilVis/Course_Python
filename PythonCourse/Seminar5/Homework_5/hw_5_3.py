# 3.Создайте программу для игры в "Крестики-нолики".

def print_field(field_l):
    for i in field_l:
        print('|', end = '')
        for j in i:
            print(j, end = '|')
        print()


def valid_num(num_str):
    valid = ['1', '2', '3']
    while (not num_str.isdigit) or (num_str[0] not in valid) or (num_str[1] not in valid):
            num_str = input('Нужно указать две цифры от 1 до 3: ')
    return num_str


def valid_cell(num_str, field_l):
    a = int(num_str[0])
    b = int(num_str[1])
    while field_l[a - 1][b - 1] != '_':
        num_str = valid_num(input('Клетка уже занята, введите новое значение: '))
        a = int(num_str[0])
        b = int(num_str[1])
    return [a, b]


def check_win(win_char):
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] == win_char:
            return True
        if field[0][i] == field[1][i] == field[2][i] == win_char:
            return True
    if field[0][0] == field[1][1] == field[2][2] == win_char:
        return True
    if field[0][2] == field[1][1] == field[2][0] == win_char:
        return True
    return False


def check_tie(field_l):
    for i in field_l:
        if '_' in i:
                return False
    return True


field = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
print_field(field)

dot_char1 = 'X'
dot_char2 = 'O'
while True:
    print(f'Ходит {dot_char1}.')
    move = valid_num(input('Введите номер строчки и столбца без пробела: '))
    x, y = valid_cell(move, field)
    field[x - 1][y - 1] = dot_char1
    print_field(field)
    if check_win(dot_char1):
        print('Вы победили')
        break
    if check_tie(field):
        print('У вас ничья')
        break
    dot_char1, dot_char2 = dot_char2, dot_char1



    
