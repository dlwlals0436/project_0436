from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import telegram
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
dv = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


dv.get("https://newtoki118.com/toki_free?sca=%EA%B3%B5%EC%9C%A0")

bot = telegram.Bot(token='5047253923:AAGRE6Knv20XImmA_OO-WO5x8xW9dSGD2iU')

if __name__ == '__main__':
     
    latest_num = 0
    while True:
        post_num = dv.find_element(By.CSS_SELECTOR,'div.wr-num.hidden-xs').text
    
    
        if latest_num != post_num :
            latest_num = post_num
            name =  dv.find_element(By.CSS_SELECTOR,'span.member').text
            ago =  dv.find_element(By.CSS_SELECTOR,'div.wr-date.hidden-xs').text
            text = name + '의 새 글이 올라왔어욤' + '\n' +ago
            bot.sendMessage(-1001555428405, text)
        time.sleep(30)
        print('bot 동작 중 현재 게시글 번호' + str(latest_num))
