import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import idAndPw
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

# Chrome 드라이버 경로 설정 (본인 환경에 맞게 수정)
# driver_path = '경로/chromedriver.exe'

# Chrome 브라우저를 열고 웹 페이지로 이동
# driver = webdriver.Chrome(executable_path=driver_path)
driver = webdriver.Chrome()
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

# 테이블의 모든 행 가져오기
table = driver.find_element_by_tag_name('table')
rows = table.find_elements_by_tag_name('tr')

# 행을 리스트로 변환하여 데이터 저장
data = []
for row in rows:
    # 행의 모든 셀 가져오기
    cells = row.find_elements_by_tag_name('td')
    row_data = []
    for cell in cells:
        row_data.append(cell.text)
    data.append(row_data)

# 데이터 출력
for row_data in data:
    print(row_data)

# 브라우저 종료
driver.quit()