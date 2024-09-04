import requests
from bs4 import BeautifulSoup

web = requests.get('https://invoice.etax.nat.gov.tw/index.html')
web.encoding='utf-8'       # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼
soup = BeautifulSoup(web.text, "html.parser")
td = soup.select('.container-fluid')[0].select('.etw-tbiggest') #整個中獎號碼的div
special1 = td[0].getText() #特別獎
special2 = td[1].getText() #特獎
head = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]] #取出頭獎的三組號碼

#開始兌獎
while True:
    try:
        # 對獎程式
        num = input('輸入你的發票號碼：')
        if num == special1: print('對中 1000 萬元！')
        if num == special2: print('對中 200 萬元！')
        for i in head:
            if num == i:
                print('對中 20 萬元！')
                break
            if num[-7:] == i[-7:]:
                print('對中 4 萬元！')
                break
            if num[-6:] == i[-6:]:
                print('對中 1 萬元！')
                break
            if num[-5:] == i[-5:]:
                print('對中 4000 元！')
                break
            if num[-4:] == i[-4:]:
                print('對中 1000 元！')
                break
            if num[-3:] == i[-3:]:
                print('對中 200 元！')
                break
    except: break




