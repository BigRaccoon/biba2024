import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

# добываем шутки с сайта и сохраняем их в "data"
url = f'https://anekdoty.ru/'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
data = soup.find_all('div', class_='holder-body')

list_for_dic = []

# с помощью цикла создаем список шуток
for jokes in data:
    name = jokes.find('p').text.replace('\n', '')
    list_for_dic.append(name)

count = len(list_for_dic)
library = {

}

# с помощью цикла преобразуем список в словарь
for i in range(count):
    library[i] = list_for_dic[i]

print(library)

with open('data_jokes.json', 'a', encoding='UTF-8') as file_out:
    json.dump(library, file_out, ensure_ascii=False, indent=2)
