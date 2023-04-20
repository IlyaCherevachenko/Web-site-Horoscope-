from random import choice


def create_horoscope():
    with open('constructor_data/part_1.txt', 'r', encoding='UTF-8') as f:
        text_1 = f.readlines()

    with open('constructor_data/part_2.txt', 'r', encoding='UTF-8') as f:
        text_2 = f.readlines()

    with open('constructor_data/part_3.txt', 'r', encoding='UTF-8') as f:
        text_3 = f.readlines()

    part_1 = text_1[0].split('/')
    part_2 = text_2[0].split('/')
    part_3 = text_3[0].split('/')

    return [choice(part_1), choice(part_2), choice(part_3)]
