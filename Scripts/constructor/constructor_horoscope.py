from random import choice


def create_horoscope(status):
    small = ['today', 'tomorrow', 'day']
    big = ['month', 'week']
    first_occurrence = 0

    with open('scripts/constructor/constructor_data/part_1.txt', 'r', encoding='UTF-8') as f:
        text_1 = f.readlines()

    with open('scripts/constructor/constructor_data/part_2.txt', 'r', encoding='UTF-8') as f:
        text_2 = f.readlines()

    with open('scripts/constructor/constructor_data/part_3.txt', 'r', encoding='UTF-8') as f:
        text_3 = f.readlines()

    part_1 = text_1[first_occurrence].split('/')
    part_2 = text_2[first_occurrence].split('/')
    part_3 = text_3[first_occurrence].split('/')

    for word in small:
        if status == word:
            text = f'{choice(part_1)} {choice(part_2)} {choice(part_3)}'
            result = [text]

            return result

    for word in big:
        if status == word:
            result = [choice(part_1), f'{choice(part_2)} {choice(part_3)}']

            return result
