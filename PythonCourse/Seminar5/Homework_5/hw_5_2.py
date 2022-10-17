# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import choice, randint


candies = 2021
print('На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет.\
    \nПобедит тот, кто сделает последний ход\n')

game_mode = input('Укажите число игроков (2 - игроков против игрока, 1 - игрок против компютера): ')
while not game_mode.isdigit() or int(game_mode) > 2 or int(game_mode) < 1:
    game_mode = input('Введите 1 или 2: ')
print('Игра началась')

# Игра с человеком
if game_mode == '2':
    while candies > 0:
        print(f'Конфет осталось: {candies}')
        first_player_turn = input('1й игрок, введите, сколько конфет хотите взять: ')
        while not first_player_turn.isdigit() or int(first_player_turn) > 28 or int(first_player_turn) < 1:
            first_player_turn = input('Неверное число, нужно взять от 1 до 28 конфет: ')
        candies -= int(first_player_turn)
        if candies > 0:
            print(f'Конфет осталось: {candies}')
            second_player_turn = input('2й игрок, введите, сколько конфет хотите взять: ')
            while not second_player_turn.isdigit() or int(second_player_turn) > 28 or int(second_player_turn) < 1:
                second_player_turn = input('Неверное число, нужно взять от 1 до 28 конфет: ')
            candies -= int(second_player_turn)
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
            print(f'Конфет осталось: {candies}')
            first_player_turn = input('Введите, сколько конфет хотите взять: ')
            while not first_player_turn.isdigit() or int(first_player_turn) > 28 or int(first_player_turn) < 1:
                first_player_turn = input('Неверное число, нужно взять от 1 до 28 конфет: ')
            candies -= int(first_player_turn)
        if candies > 0:
            print(f'Конфет осталось: {candies}')
            computer_turn = candies % 29
            if not computer_turn: # если игрок изначально взял такое кол-во конфет, что выиграет, если не ошибется
                computer_turn = randint(1, 28)
            print(f'Компьютер взял {computer_turn} конфет')
            candies -= int(computer_turn)
            if candies <= 0:
                print('Компьютер победил')
        else:
            print('Вы победили')
