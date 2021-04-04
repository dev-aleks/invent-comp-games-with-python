import random
import time


def display_intro():
    print('''Вы находитель в землях, заселенных драконами.
    Перед собой вы видите две пещеры. В одной из них - дружелюбный дракон, 
    который готов поделиться с вами своими сокровищами. Во второй - 
    жадный и голодный дракон, который мигом вас съест.''')
    print()


def choose_cave():
    cave = 0
    while cave != 1 and cave != 2:
        cave = int(input('В какую пещеру войдете? (Нажмите клавишу 1 или 2)\n'))
    return cave


def check_cave(chosen_cave):
    friendly_cave = random.randint(1, 2)
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Её темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и ...')
    time.sleep(2)

    if chosen_cave == friendly_cave:
        print('... делится с вами своими сокровищами')
    else:
        print('... моментально съедает вас!')


play_again = 'yes'

while play_again == 'yes':
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)
    play_again = str(input('Ещё раз? (yes or no)\n'))
