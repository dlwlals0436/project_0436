
import cloudscraper
import requests
import time
from bs4 import BeautifulSoup
import telegram


bot = telegram.Bot(token='5047253923:AAGRE6Knv20XImmA_OO-WO5x8xW9dSGD2iU')

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
cookies = {'cf_clearance': 'some clearance'}


if __name__ == '__main__':

    # 제일 최신 게시글의 번호 저장
    latest_num = 0
    while True:
        scraper = cloudscraper.create_scraper()
        html = scraper.get("https://newtoki119.com/toki_free?sca=%EA%B3%B5%EC%9C%A0").content
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find("li", {"class" : "list-item"})
        post_num = posts.find("div", {"class" : "wr-num hidden-xs"}).text


        if latest_num != post_num :
            latest_num = post_num
            name =  posts.find("span", {"class" : "member"}).text
            ago =  posts.find("div", {"class" : "wr-date hidden-xs"}).text
            text = "[롶]" + name + '의 새 글이 올라왔어욤' + "[" + ago + "]"
            bot.sendMessage(-1001555428405, text)
        time.sleep(15)
        print('bot 동작 중 현재 게시글 번호' + latest_num)
