# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import choice, randint


def input_number():
    num_string = input('Введите, сколько конфет хотите взять: ')
    while not num_string.isdigit() or int(num_string) > 28 or int(num_string) < 1:
            num_string = input('Неверное число, нужно взять от 1 до 28 конфет: ')
    return num_string


def make_move(player, num_candies):
    print(f'Конфет осталось: {num_candies}')
    print(player, end = '')
    player_turn = input_number()
    num_candies -= int(player_turn)
    return num_candies


candies = 2021
print('На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет.\
    \nПобедит тот, кто сделает последний ход\n')

game_mode = input('Укажите число игроков (2 - игрок против игрока, 1 - игрок против компютера): ')
while not game_mode.isdigit() or int(game_mode) > 2 or int(game_mode) < 1:
    game_mode = input('Введите 1 или 2: ')
print('Игра началась')

# Игра с человеком
if game_mode == '2':
    while candies > 0:
        candies = make_move('1й игрок. ', candies)
        if candies > 0:
            candies = make_move('2й игрок. ', candies)
            if candies <= 0:
                print('Второй игрок победил')
        else:
            print('Первый игрок победил')

# Игра с компьютером - компьютер выигрывает во всех случаях, кроме одного
if game_mode == '1':
    turn = choice([1, 2])
    while candies > 0:
        if turn == 2:
            print('Компьютер начинает первым')
            turn = 1
        else:
            candies = make_move('', candies)
        if candies > 0:
            print(f'Конфет осталось: {candies}')
            computer_turn = candies % 29
            if not computer_turn: # когда игрок изначально взял такое кол-во конфет, что выиграет, если не ошибется
                computer_turn = randint(1, 28)
            print(f'Компьютер взял {computer_turn} конфет')
            candies -= int(computer_turn)
            if candies <= 0:
                print('Компьютер победил')
        else:
            print('Вы победили')
