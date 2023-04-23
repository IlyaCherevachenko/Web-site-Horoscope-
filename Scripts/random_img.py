from random import randint
from flask import url_for


def random_image_horoscope_base(sign):
    number_img = 10
    number = randint(1, number_img)
    image = url_for('static', filename=f'img/image_zodiacs/{sign}/{number}.jpg')

    return image


def random_image_horoscope_personal(sign):
    images = []
    number_img = 10
    number = 2

    for i in range(1, number + 1):
        count_sign = randint(1, number_img)
        image = url_for('static', filename=f'img/image_zodiacs/{sign}/{count_sign}.jpg')

        while image in images:
            count_sign = randint(1, number_img)
            image = url_for('static', filename=f'img/image_zodiacs/{sign}/{count_sign}.jpg')

        images.append(image)

    return images
