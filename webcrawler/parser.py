import requests
from bs4 import BeautifulSoup

url = 'https://www.iana.org/domains/'
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")
#print(web.cookies)

import requests

web = requests.get('https://water.taiwanstat.com/')
#print(web.text)

#BeautifulSoup方法
import requests
from bs4 import BeautifulSoup

url = 'https://www.iana.org/domains/'
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")

#print(soup.select('#logo')) #搜尋id為logo的tag
#print('-----------')
#print(soup.find_all('div')) #搜尋所有div的tag
#print('-----------')
#print(soup.find_all('p')[1]) #搜尋所有p中的第[1]個


url = 'https://www.iana.org/domains/'
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")

#print(soup.find_all('a', string='Protocols'))   # 找出內容字串為 Domains 的 a tag
#print(soup.find_all('a')[1].get_text())
#print(soup.find('a')['href'])  

#實作，抓取各水庫的水容量
web = requests.get('https://water.taiwanstat.com/')
soup = BeautifulSoup(web.text,"html.parser")
reservoir = soup.select('.reservoir')
for i in reservoir:
    print(i.find('div', class_='name').get_text(), end=':')  # 取得內容的 class 為 name 的 div 文字
    print(i.find('h5').get_text(), end='\n')   # 取得內容 h5 tag 的文字
