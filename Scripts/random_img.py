from random import randint
from flask import url_for


def random_image(number, sign):
    images = []

    for i in range(1, number + 1):
        number = randint(1, 10)
        image = url_for('static', filename=f'img/image_zodiacs/{sign}/{number}.jpg')
        while image in images:
            number = randint(1, 10)
            image = url_for('static', filename=f'img/image_zodiacs/{sign}/{number}.jpg')
        images.append(image)

    if len(images) == 1:
        return image

    return images
