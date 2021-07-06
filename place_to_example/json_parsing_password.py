#Пример парсинга паролей со статичной страницы
#использется библиотека lxml
#
#
#

import requests
from lxml import html

response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")

tree = html.fromstring(response.text)

locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'
passwords = tree.xpath(locator)

for password in passwords:
    password = str(password).strip()
    print(password)