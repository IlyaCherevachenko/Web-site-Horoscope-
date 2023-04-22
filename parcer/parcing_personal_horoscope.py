import requests
from bs4 import BeautifulSoup


def result_process(data_list):
    texts = ''

    for item in data_list:
        for i in item:
            texts += str(*i, )

    texts = texts.split('\n')

    return texts


def get_personal_horoscope_by_day_and_tomorrow(zodiac_sign: str, day='today'):
    res = requests.get(f"https://horo.mail.ru/prediction/{zodiac_sign}/{day}/")
    soup = BeautifulSoup(res.content, 'html.parser')
    list_data = soup.find_all('div', attrs={'class': 'article__item article__item_alignment_left article__item_html'})

    group_texts_1 = ''
    group_texts_2 = ''

    all_text = []
    delimiter = 0

    if list_data:
        texts = result_process(list_data)

        for i in range(len(texts)):
            if i == delimiter:
                group_texts_1 += texts[i] + ' '
            else:
                group_texts_2 += texts[i] + ' '

        all_text.append(group_texts_1[:-1])
        all_text.append(group_texts_2[:-1])
    else:
        return None

    return all_text


def get_personal_horoscope_by_week_and_month(zodiac_sign: str, day='week'):
    res = requests.get(f"https://horo.mail.ru/prediction/{zodiac_sign}/{day}/")
    soup = BeautifulSoup(res.content, 'html.parser')
    data_list = soup.find_all('div', attrs={'class': 'article__item article__item_alignment_left article__item_html'})

    group_texts_1 = ''
    group_texts_2 = ''
    group_texts_3 = ''

    all_text = []
    delimiter = 0
    sentence_limit = 3

    if data_list:
        texts = result_process(data_list)
        sentences = len(texts)

        for i in range(sentences):
            if day == 'month':
                if sentences == sentence_limit:
                    if i == delimiter:
                        group_texts_1 += texts[i] + ' '
                    elif i == delimiter + 1 or i == delimiter + 2:
                        group_texts_2 += texts[i] + ' '
                    else:
                        group_texts_3 += texts[i] + ' '
                else:
                    if i == delimiter:
                        group_texts_1 += texts[i] + ' '
                    elif i == delimiter + 1:
                        group_texts_2 += texts[i] + ' '
                    else:
                        group_texts_3 += texts[i] + ' '
            else:
                if i == delimiter:
                    group_texts_1 += texts[i] + ' '
                else:
                    group_texts_2 += texts[i] + ' '

        all_text.append(group_texts_1)
        all_text.append(group_texts_2)

        if group_texts_3 != '':
            all_text.append(group_texts_3)
    else:
        return None

    return all_text
