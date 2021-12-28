

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
        post_num = posts.find("div", {"class": "wr-num hidden-xs"}).get_text()

        if latest_num != post_num:
            latest_num = post_num
            name = posts.find("span", {"class": "member"}).get_text()
            ago = posts.find("div", {"class": "wr-date hidden-xs"}).get_text()
            text = name + '의 새 글이 올라왔어욤' + '\n' + ago
            bot.sendMessage(-1001555428405, text)
        time.sleep(30)
        print('bot 동작 중 현재 게시글 번호' + str(latest_num))
