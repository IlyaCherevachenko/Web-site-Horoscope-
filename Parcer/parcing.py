import requests
from bs4 import BeautifulSoup


def get_horoscope_by_day_and_tomorrow(zodiac_sign: str, day: str):
    if day == 'today':
        res = requests.get(f"https://horoscopes.rambler.ru/{zodiac_sign}/")
    else:
        res = requests.get(f"https://horoscopes.rambler.ru/{zodiac_sign}/{day}/")

    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': '_1E4Zo _3BLIa'})

    if data is not None:
        all_text = [data.p.text]
    else:
        all_text = None

    return all_text


def get_horoscope_by_week_and_month(zodiac_sign: str, day: str):
    texts = ''
    all_text = []
    sentece_limit = 2

    day += 'ly'

    res = requests.get(f"https://horoscopes.rambler.ru/{zodiac_sign}/{day}/")
    soup = BeautifulSoup(res.content, 'html.parser')

    data = soup.find_all('p', attrs={'class': 'mtZOt'})

    if data is not None:
        if len(data) > 2:
            for i in range(sentece_limit):
                if i == 0:
                    all_text.append(data[i].text)
                else:
                    texts += data[i].text + ' '
            all_text.append(texts)
        else:
            for i in range(len(data)):
                all_text.append(data[i].text)
    else:
        all_text = None

    return all_text


def get_personal_horoscope_by_day_and_tomorrow(zodiac_sign: str, day='today'):
    res = requests.get(f"https://horo.mail.ru/prediction/{zodiac_sign}/{day}/")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find_all('div', attrs={'class': 'article__item article__item_alignment_left article__item_html'})

    if data is None:
        return None

    texts = ''
    group_texts_1 = ''
    group_texts_2 = ''

    all_text = []

    for i in data[0]:
        texts += str(*i,)

    texts = texts.split('\n')

    for i in range(len(texts)):
        if i == 0:
            group_texts_1 += texts[i] + ' '
        else:
            group_texts_2 += texts[i] + ' '

    all_text.append(group_texts_1)
    all_text.append(group_texts_2)

    return all_text


def get_personal_horoscope_by_week_and_month(zodiac_sign: str, day='week'):
    res = requests.get(f"https://horo.mail.ru/prediction/{zodiac_sign}/{day}/")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find_all('div', attrs={'class': 'article__item article__item_alignment_left article__item_html'})

    if data is None:
        return None

    texts = ''
    group_texts_1 = ''
    group_texts_2 = ''
    group_texts_3 = ''

    all_text = []
    data = data[0]

    for i in data:
        texts += str(*i, )

    texts = texts.split('\n')

    for i in range(len(texts)):
        if day == 'month':
            if len(texts) == 3:
                if i == 0:
                    group_texts_1 += texts[i] + ' '
                elif i == 1 or i == 2:
                    group_texts_2 += texts[i] + ' '
                else:
                    group_texts_3 += texts[i] + ' '
            else:
                if i == 0:
                    group_texts_1 += texts[i] + ' '
                elif i == 1:
                    group_texts_2 += texts[i] + ' '
                else:
                    group_texts_3 += texts[i] + ' '
        else:
            if i < 1:
                group_texts_1 += texts[i] + ' '
            else:
                group_texts_2 += texts[i] + ' '

    all_text.append(group_texts_1)
    all_text.append(group_texts_2)
    if group_texts_3 != '':
        all_text.append(group_texts_3)

    return all_text
