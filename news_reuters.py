import requests
from bs4 import BeautifulSoup

def gen_news_en():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

    url = f'https://www.reuters.com/'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all(
        'h3', class_='text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_6__1qUJ5 heading__base__2T28j heading__heading_6__RtD9P')

    print(data)
    filteredNews = []




#небольшое форматирование новостей для удобства
    for new in data:
        name = new.find(
            'a').text.replace('\n', '')
        filteredNews.append(f'🌍{name}')

    return '\n'.join(filteredNews)

gen_news_en()
  