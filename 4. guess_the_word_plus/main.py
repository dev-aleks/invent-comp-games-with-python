import random

# Список из 9 картинок - 8 попыток
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
    """,  """
    +---+
   [0   |
   /|\  |
   / \  |
       ===
    """,  """
    +---+
   [0]  |
   /|\  |
   / \  |
       ===
    """
]

# Слова:
WORDS = {'животные':'черепаха питон лев тигр слон муравей ястреб'.split(),
         'геометрия':'квадрат треугольник круг ромб восьмиугольник'.split(),
         'цвета':'красный синий желтый белый коричневый'.split(),
         'фрукты':'банан яблоко апельсин лайм груша виноград'.split()}


def get_random_word(word_dict):
    """
    Function for get random word from DICT with words
    :return:
    """
    word_key = random.choice(list(word_dict.keys()))
    word_index = random.randint(0, len(word_dict[word_key])-1)
    return [word_dict[word_key][word_index].upper(), word_key]


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


def choose_difficulty(level, picture):
    """
    Function, check letter in string 'level', and change level difficulty.
    :param level:
    :return:
    """
    level_high = 4
    level_medium = 2
    if level == 'Т':
        for i in range(0, level_high, 1):
            del picture[len(picture) - 1]
        print(f'Выбран тяжелый уровень игры - попыток угадать слово стало на {level_high} меньше')
    if level == 'С':
        for i in range(0, level_medium, 1):
            del picture[len(picture) - 1]
        print(f'Выбран средний уровень игры - попыток угадать слово стало на {level_medium} меньше')
    else:
        print(f'Выбран легкий уровень игры - у вас 8 попыток')


print('В И С Е Л И Ц А')
secret_word, secret_set = get_random_word(WORDS)
go_game = True
list_guess_letter = []
list_missed_letter = []
difficulty_level = ' '

while difficulty_level not in 'ЛСТ':
    difficulty_level = input('Выберите уровень сложности: Л (легкий), С (средний), Т (тяжелый):\n').upper()
choose_difficulty(difficulty_level, PICS)

while go_game:
    print(f'Загадываемое слово из категории \'{secret_set}\'')
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
            secret_word, secret_set = get_random_word(WORDS)
            go_game = True
            list_guess_letter = []
            list_missed_letter = []
            difficulty_level = ' '
        else:
            break
