from selenium import webdriver

# Chrome 드라이버 경로 설정 (본인 환경에 맞게 수정)
driver_path = '경로/chromedriver.exe'

# Chrome 브라우저를 열고 웹 페이지로 이동
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('웹 페이지 URL')

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
