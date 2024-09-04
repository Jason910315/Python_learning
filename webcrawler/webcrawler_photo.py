import requests
from bs4 import BeautifulSoup
web = requests.get('https://www.ptt.cc/bbs/SuperHeroes/M.1715013458.A.948.html')
soup = BeautifulSoup(web.text,"html.parser")
imgs = soup.find_all('img')
name = 0
for i in imgs:
    print(i['src'])
    jpg = requests.get(i['src'])
    f = open(f'C:/Python_learning/webcrawler/test_{name}.jpg','wb')
    f.write(jpg.content)
    f.close()
    name = name +1

