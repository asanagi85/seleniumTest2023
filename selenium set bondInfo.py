import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import idAndPw
from selenium.webdriver.common.by import By
from urllib.parse import urlparse


driver = webdriver.Chrome()
URL = "https://site1.sbisec.co.jp/ETGate/WPLETmgR001Control?OutSide=on&getFlg=on&burl=search_bond&cat1=bond&cat2=foreign&dir=foreign&file=bond_foreign_02.html"

driver.get(URL)
#채권정보 일단 전부 가져오기
# table = driver.find_elements(By.CLASS_NAME,'md-l-table-01', )
table = driver.find_element(By.XPATH,'//*[@id="main"]/div[7]/table')

rows = table.find_elements(By.TAG_NAME, "tr")  # Find all the rows in the table
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")  # Find the columns in each row
    for column in columns:
        print(column.text)

            
#미국채권인지 아닌지 체크하는 메소드
#미국채권이라면 제로쿠폰인가 아닌가 체크
# 제로쿠폰이 아니라면, 채권명, 단가, 리마와리, 이자지급일, 상환일, 판매단위, 잔존년수, 등급취득
time.sleep(10)