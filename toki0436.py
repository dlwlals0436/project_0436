

import requests

import time

from bs4 import BeautifulSoup

import telegram

bot = telegram.Bot(token='5047253923:AAGRE6Knv20XImmA_OO-WO5x8xW9dSGD2iU')

if __name__ == '__main__':

    latest_num = 0
    while True:
        req = requests.get('https://newtoki118.com/toki_free?sca=%EA%B3%B5%EC%9C%A0')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find("li", {"class": "list-item"})
        print(posts)
