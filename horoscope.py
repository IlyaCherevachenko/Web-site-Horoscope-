from flask import Flask, render_template, request
from parcer import parcing_base_horoscope, parcing_personal_horoscope
from scripts import random_img, zodiac_sign, name_zodiac, create_home
from scripts.birthday import write_and_read_birthday
from scripts.constructor import constructor_horoscope
from scripts.db_for_news import create_db

app = Flask(__name__)


@app.route('/home')
def home():
    zodiac_numb = 12
    images = create_home.template_home(zodiac_numb)

    return render_template('home.html', data=images)


@app.route('/zodiac_sign/<sign>/<date>')
def gemini_data(sign, date):
    zodiac_name = name_zodiac.get_name_zodiac(sign)
    image = random_img.random_image_horoscope_base(sign)

    if date == 'today' or date == 'tomorrow':
        text = parcing_base_horoscope.get_horoscope_by_day_and_tomorrow(sign, date)

        if text is None:
            text = constructor_horoscope.create_horoscope(date)

        return render_template('zodiacs.html', texts=text, len_texts=len(text), name=zodiac_name,
                               sign=sign)
    else:
        texts = parcing_base_horoscope.get_horoscope_by_week_and_month(sign, date)

        if texts is None:
            texts = constructor_horoscope.create_horoscope(date)  # количество текстов (нужно добавить ещё)

        return render_template('zodiacs.html', texts=texts, len_texts=len(texts), file=image,
                               name=zodiac_name, sign=sign)


@app.route('/home_filter/<date>', methods=['POST', 'GET'])
def get_data_form(date):
    if request.method == 'POST':
        name = request.form.get('text')
        birthday = request.form.get('date')

        sign = zodiac_sign.get_sign_from_form(birthday)
        image_1, image_2 = random_img.random_image_horoscope_personal(sign)

        if date == 'today' or 'tomorrow':
            texts = parcing_personal_horoscope.get_personal_horoscope_by_day_and_tomorrow(sign, date)

        else:
            texts = parcing_personal_horoscope.get_personal_horoscope_by_week_and_month(sign, date)

        if texts is None:
            texts = constructor_horoscope.create_horoscope(date)

        write_and_read_birthday.write_birthday(name, birthday, sign)

        return render_template('personal_horoscope.html', name=name,  texts=texts, len_texts=len(texts),
                               file_1=image_1, file_2=image_2)
    else:
        name, birthday, sign = write_and_read_birthday.read_birthday()
        image_1, image_2 = random_img.random_image_horoscope_personal(sign)

        if date == 'today' or date == 'tomorrow':
            texts = parcing_personal_horoscope.get_personal_horoscope_by_day_and_tomorrow(sign, date)
        else:
            texts = parcing_personal_horoscope.get_personal_horoscope_by_week_and_month(sign, date)

        if texts is None:
            texts = constructor_horoscope.create_horoscope(date)

    return render_template('personal_horoscope.html', name=name,  texts=texts, len_texts=len(texts),
                           file_1=image_1, file_2=image_2)


@app.route('/news')
def news():
    result = create_db.main_db()
    return render_template('news.html', result=result)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
