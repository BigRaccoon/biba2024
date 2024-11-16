import requests
from bs4 import BeautifulSoup


# функция, которая обращается к сайту и собирает главные новости в список
def gen_news():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

    url = f'https://iz.ru/news'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all(
        'div', class_='node__cart__item__inside__info__title small-title-style1')

    print(data)
    filteredNews = []

# небольшое форматирование новостей для удобства
    for new in data:
        name = new.find(
            'span').text.replace('\n', '')
        filteredNews.append(f'★{name}☆')

    return '\n'.join(filteredNews)
