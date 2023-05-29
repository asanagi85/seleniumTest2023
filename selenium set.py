import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import idAndPw
from selenium.webdriver.common.by import By
from urllib.parse import urlparse


driver = webdriver.Chrome()
# URL = "https://www.sbisec.co.jp/ETGate/?_ControlID=WPLEThmR001Control&_PageID=DefaultPID&_DataStoreID=DSWPLEThmR001Control&_ActionID=DefaultAID&getFlg=on"
URL = "https://site1.sbisec.co.jp/ETGate/?OutSide=on&_ControlID=WPLETsmR001Control&_DataStoreID=DSWPLETsmR001Control&_PageID=WPLETsmR001Sdtl12&sw_page=BondFx&sw_param2=02_301&cat1=home&cat2=none&getFlg=on&int_pr1=150313_cmn_gnavi:1_dmenu_04&_gl=1*hzxfuz*_gcl_au*NDYwNzUzNDkyLjE2ODIzMzAyODk."

driver.get(URL)
#로그인아이디 입력
search = driver.find_element(By.NAME,'user_id')
search.send_keys(idAndPw.id + Keys.TAB)
#로그인 패스워드 입력
search = driver.find_element(By.NAME,'user_password')
search.send_keys(idAndPw.pw)
search = driver.find_element(By.NAME,'ACT_login')
#로그인버튼 클릭
search.click()
time.sleep(1)
#기발채권 구입페이지로 이동
# driver.get('https://site1.sbisec.co.jp/ETGate/WPLETmgR001Control?OutSide=on&getFlg=on&burl=search_bond&cat1=bond&cat2=foreign&dir=foreign&file=bond_foreign_02.html')
# search = driver.find_element(By.CLASS_NAME,'btn_sbi bold alC fl01 mgt5')
# search.click()
# driver.get('https://trading0.sbisec.co.jp/bff/fbonds/BffBuyOrderList.do')

#미국채권인지 아닌지 체크하는 메소드
#미국채권이라면 제로쿠폰인가 아닌가 체크
# 제로쿠폰이 아니라면, 채권명, 단가, 리마와리, 이자지급일, 상환일, 판매단위, 잔존년수, 등급취득
driver.get('https://trading0.sbisec.co.jp/bff/fbonds/BffBuyOrderList.do?dayNightKbn=1')
#다음 채권검색
time.sleep(10)