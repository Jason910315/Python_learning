from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options() 
options.chrome_executable_path = "C:\Python_learning\webcrawler\chromedriver.exe"

driver = webdriver.Chrome(options = options)
#連線到高醫大 wac 登入頁面網站
driver.get("https://wac.kmu.edu.tw/loginnew.php?PNO=indexstuv2.php&usertype=stu&lang=zh")
#取得帳號密碼的輸入欄位標籤
username = driver.find_element(By.ID,"userid")
userpassword = driver.find_element(By.ID,"password")
#輸入帳號密碼
username.send_keys("109029041")
userpassword.send_keys("6124NOK45")
#取得登入按鈕的標籤並自動化按下Enter建
signInbtn = driver.find_element(By.CSS_SELECTOR,"[type = submit]")
signInbtn.send_keys(Keys.ENTER)
#點選我已了解
checkbtn = driver.find_element(By.CLASS_NAME,"swal2-actions")
checkbtn.click()
time.sleep(10)
driver.close()
