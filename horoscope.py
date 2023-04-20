from flask import Flask, render_template, request
from Parcer import parcing
from Scripts import random_img, zodiac_sign, name_zodiac, create_home
from Scripts.birthday import write_and_read_birthday
from Scripts.constructor import constructor_horoscope

app = Flask(__name__)


@app.route('/home')
def home():
    zodiac_numb = 12
    images = create_home.template_home(zodiac_numb)

    return render_template('home.html', data=images)


@app.route('/zodiac_sign/<sign>/<date>')
def gemini_data(sign, date):
    zodiac_name = name_zodiac.get_name_zodiac(sign)
    image = random_img.random_image(1, sign)

    if date == 'today' or date == 'tomorrow':
        text = parcing.get_horoscope_by_day_and_tomorrow(sign, date)

        if text is None:
            text = constructor_horoscope.create_horoscope()

        return render_template('zodiacs.html', texts=text, len_texts=len(text), name=zodiac_name,
                               sign=sign)
    else:
        texts = parcing.get_horoscope_by_week_and_month(sign, date)

        if texts is None:
            texts = constructor_horoscope.create_horoscope() # количество текстов (пока 1 - ошибка)

        return render_template('zodiacs.html', texts=texts, len_texts=len(texts), file=image,
                               name=zodiac_name, sign=sign)


@app.route('/home_filter/<date>', methods=['POST', 'GET'])
def get_data_form(date):
    if request.method == 'POST':
        name = request.form.get('text')
        birthday = request.form.get('date')

        sign = zodiac_sign.get_sign_from_form(birthday)
        image_1, image_2 = random_img.random_image(2, sign)

        if date == 'today' or 'tomorrow':
            texts = parcing.get_personal_horoscope_by_day_and_tomorrow(sign, date)
        else:
            texts = parcing.get_personal_horoscope_by_week_and_month(sign, date)

        if texts is None:
            texts = constructor_horoscope.create_horoscope()  # количество текстов (пока 1 - ошибка)

        write_and_read_birthday.write_birthday(name, birthday, sign)

        return render_template('personal_horoscope.html', name=name,  texts=texts, len_texts=len(texts),
                               file_1=image_1, file_2=image_2)
    else:
        data_user = write_and_read_birthday.read_birthday()
        image_1, image_2 = random_img.random_image(2, data_user[2])

        if date == 'today' or date == 'tomorrow':
            texts = parcing.get_personal_horoscope_by_day_and_tomorrow(data_user[2], date)
        else:
            texts = parcing.get_personal_horoscope_by_week_and_month(data_user[2], date)

        if texts is None:
            texts = constructor_horoscope.create_horoscope()

    return render_template('personal_horoscope.html', name=data_user[0],  texts=texts, len_texts=len(texts),
                           file_1=image_1, file_2=image_2)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
