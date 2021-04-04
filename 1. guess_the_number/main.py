import random

variable = random.randint(1, 20)
count = 0

name = str(input('Привет, как тебя зовут?\n'))
print(f'Что ж, {name}, я загадываю число от 1 до 20.')

while True:
    my_variable = int(input('Попробуй угадать...\n'))
    if my_variable < 0 or my_variable > 20:
        print('Промежуток чисел от 1 до 20, будь внимательнее')
    elif my_variable > 0 and my_variable < 20:
        if my_variable > variable:
            print('Число больше загаданного.')
        elif my_variable < variable:
            print('Число меньше загаданного.')
        elif my_variable == variable:
            count += 1
            print(f'Отлично, {name}! Ты справился за {count} попытки!')
            break
    count += 1
