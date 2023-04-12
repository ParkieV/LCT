import requests
from bs4 import BeautifulSoup

address = str(input())

url_LVL1 = 'https://yandex.ru/images/search?from=tabbar&text=' + address  # объявление ссылки "первого уровня" с использованием первчиного запроса

response = requests.get(url_LVL1)
soup = BeautifulSoup(response.text, 'lxml')  # получение данных со первичной страницы

soup = str(soup)

left_border = soup.find('href="/images/search')  # левое ограничение для поиска ссылки
right_border = soup.find('">', left_border)  # правое ограничение для поиска ссылки
url_LVL2 = 'http://yandex.ru' + soup[
                                left_border + 6:right_border]  # объявление ссылки "второго уровня" на страницу содержащую оригинально изображение

# print(url_LVL2)
response = requests.get(url_LVL2)
soup = BeautifulSoup(response.text, 'lxml')  # получение данных со вторичной страницы

soup = str(soup)

left_border = soup.find('"origin"')  # левое ограничение для поиска ссылки
right_border = soup.find('"}', left_border) # правое ограничение для поиска ссылки
buff = soup.find('":"', left_border) # левое ограничение для поиска ссылки(уточнительное)
print(soup[buff + 3:right_border])

