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
        return None

    return all_text


def get_horoscope_by_week_and_month(zodiac_sign: str, day: str):
    texts = ''
    all_text = []
    sentence_limit = 2
    sentences = 2

    day += 'ly'

    res = requests.get(f"https://horoscopes.rambler.ru/{zodiac_sign}/{day}/")
    soup = BeautifulSoup(res.content, 'html.parser')

    data = soup.find_all('p', attrs={'class': 'mtZOt'})

    if data:
        if len(data) > sentences:
            for i in range(sentence_limit):
                if i == 0:
                    all_text.append(data[i].text)
                else:
                    texts += data[i].text + ' '
            all_text.append(texts)
        else:
            for i in range(len(data)):
                all_text.append(data[i].text)
    else:
        return None

    return all_text
