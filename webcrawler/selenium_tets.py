#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#設定 Chrome Driver 的執行檔路徑
options = Options() #建立Options物件
options.chrome_executable_path = "C:\Python_learning\webcrawler\chromedriver.exe"
#建立 Driver 物件實體，用程式操作gC:\Python_learning\webcrawler\chromedriver.exe
driver = webdriver.Chrome(options = options)

#連線到 PTT 籃球版
driver.get("https://www.ptt.cc/bbs/basketballTW/index.html")

#搜尋id為logo的網頁文字
logo = driver.find_element(By.ID,'logo')
print(logo.text) #注意要加text否則印出來的是WebElement物件

#使用CSS選擇搜尋任意欄位標籤
author = driver.find_element(By.CSS_SELECTOR,"[class = author]")
print(author.text)
#建立 titles 物件接收搜尋到的title串列
titles = driver.find_elements(By.CLASS_NAME,'title')
for title in titles:
    print(title.text) 

#模擬使用者點選上一頁的動作
link = driver.find_element(By.LINK_TEXT,"‹ 上頁") #找到頁面中通往上頁超連結的文字
link.click() #點擊動作
#以下就可以對上一頁進行各種操作(如上列印title等)

driver.close()

