from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options() 
options.chrome_executable_path = "C:\Python_learning\webcrawler\chromedriver.exe"

driver = webdriver.Chrome(options = options)

driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")
#捲動到視窗底部並等待載入更多內容
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #捲動到視窗底部
time.sleep(3) #等待3秒鐘，讓他先載入新內容
jobs = driver.find_elements(By.CLASS_NAME,'base-search-card__title')
for job in jobs:
    print(job.text)
