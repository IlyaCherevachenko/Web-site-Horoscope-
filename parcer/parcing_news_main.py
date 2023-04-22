import requests
from bs4 import BeautifulSoup


def get_links():
    links = []
    number_articles = 6

    res = requests.get("https://horoscopes.rambler.ru/longread/")
    soup = BeautifulSoup(res.content, 'html.parser')

    data_divs = soup.find_all('div', attrs={'class': '_2cl0M _1ZXA7 _3jhyD'}, limit=number_articles)

    for data_div in data_divs:
        data_a = data_div.find('a', attrs={'class': 'fZM6H'}, href=True)
        links.append(data_a['href'])

    return links


def text_handler(data_text):
    raw_text = data_text[0]
    limited = len(raw_text)

    stop_word = 'Читайте также'
    number_sentence = 0
    texts = []

    for i in raw_text:
        if number_sentence < limited:
            sentence = i.text
            if stop_word in sentence:
                break
            else:
                texts.append(sentence)
            number_sentence += 1

    return texts


def get_news_main():
    links = get_links()
    numbers = len(links)

    result = []

    for i in range(numbers):
        res = requests.get(f'https://horoscopes.rambler.ru{links[i]}')
        soup = BeautifulSoup(res.content, 'html.parser')

        data = soup.find('div', attrs={'class': ''})

        data_name_text = data.find('h1')
        data_image = data.find('img', attrs={'class': 'Vq_-k'})
        data_first_text = data.find('p')
        data_text = data.find_all('div', attrs={'class': '_3d2Ce _3dyqM'})

        texts = text_handler(data_text)

        result.append([data_name_text.text, data_first_text.text, data_image['src'], texts])

    return result
