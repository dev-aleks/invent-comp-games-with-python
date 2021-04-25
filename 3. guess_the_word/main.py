import random

# Список из 7 картинок - 6 попыток
PICS = [
    """
    +---+
        |
        |
        |
       ===
    """, """
    +---+
    0   |
        |
        |
       ===
    """, """
    +---+
    0   |
    |   |
        |
       ===
    """, """
    +---+
    0   |
   /|   |
        |
       ===
    """, """
    +---+
    0   |
   /|\  |
        |
       ===
    """, """
    +---+
    0   |
   /|\  |
   /    |
       ===
    """, """
    +---+
    0   |
   /|\  |
   / \  |
       ===
    """
]

# Слова:
WORD = 'Черепаха золото яйцо питон'


def get_random_word(string):
    """
    Function for get random word from list with words
    :return:
    """
    list = string.split()
    return list[random.randint(0, len(list)-1)].upper()


def display_menu(missed_letters, secret_word, correct_letter):
    """
    Functions for show menu game and secret word
    :param missed_letters:
    :param secret_word:
    :param correct_letter:
    :return:
    """
    print(PICS[len(missed_letters)])
    print('Неправильные буквы:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()
    secret_word_underline = '_'*len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letter:
            secret_word_underline = secret_word_underline[:i] + secret_word[i] + secret_word_underline[i+1:]
    print(secret_word_underline)


def work_with_secret_word(secret_word):
    """
    Function for work with secret word. It means:
    - make underline instead of letter
    :param secret_word:
    :return:
    """
    make_secret_word = '_'*len(secret_word)
    return make_secret_word


def check_input_letter(input_list: list):
    """
    Fuction for check input letter
    :param input_list:
    :return:
    """
    while True:
        guess = input('Введите букву:\n').lower()
        if len(guess) != 1:
            print('Введите одну букву')
        elif guess in input_list:
            print('Вы уже вводили эту букву')
        if guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Введите букву (кириллица)')
        else:
            return guess.upper()


def play_again():
    """
    function for start the game again
    :return:
    """
    print('Хотите сыграть ещё раз? (да или нет)')
    return input().lower().startswith('д')

print('В И С Е Л И Ц А')
secret_word = get_random_word(WORD)
go_game = True
list_guess_letter = []
list_missed_letter = []

while go_game:
    # show interface game:
    display_menu(list_missed_letter, secret_word, list_guess_letter)
    guess_letter = check_input_letter(list_guess_letter + list_missed_letter)
    # work with letters:
    if guess_letter in secret_word:
        list_guess_letter.append(guess_letter)
        # check secret word
        game_status = True
        for i in range(len(secret_word)):
            if secret_word[i] not in list_guess_letter:
                game_status = False
                break
        if game_status:
            print(f'Поздравляю! Слово {secret_word} угадано!')
            go_game = False
    else:
        list_missed_letter.append(guess_letter)
        if len(list_missed_letter) == len(PICS)-1:
            print(PICS[len(PICS)-1])
            print('Вы израсходовали все попытки.')
            print(f'Правильное слово: {secret_word}')
            go_game = False
    # game begin?
    if not go_game:
        if play_again():
            secret_word = get_random_word(WORD)
            go_game = True
            list_guess_letter = []
            list_missed_letter = []
        else:
            break
