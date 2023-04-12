import threading
import time
import requests
from bs4 import BeautifulSoup

url = 'https://www.irn.ru/kvartiry/moskva/ceny-po-rayonam/'


class Parser(threading.Thread):
    def __init__(self):
        super().__init__()
        self.prices_by_district = {}

    def run(self):
        while True:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            all_prices = soup.findAll('table', class_='space-medium-top list1 table-currency')[0].find_all('tr')
            for data in all_prices[2:]:
                self.prices_by_district[data.find_all('td')[3].text[1:-1].replace('\t', '')] = int(data.find_all('td')[-2].text.replace('\xa0', ''))
            time.sleep(60)


