from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time, re

options = Options()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://license.kpc.or.kr/uat/uia/LoginView.do"

driver.get(url)

driver.find_element(By.ID, "id").send_keys(str(input("KPC자격 아이디를 입력하세요 : ")))
time.sleep(1)
driver.find_element(By.ID, "password").send_keys(str(input("KPC자격 아이디를 입력하세요 : ")))
time.sleep(1)
driver.find_element(By.ID, "loginBtn").click()
time.sleep(1) 
try:
    driver.get("https://license.kpc.or.kr/myqlf/scrcrqfemanage/selectApyexmsttusall.do")
    time.sleep(1) 
    select=Select(driver.find_element(By.ID, "certiCode"))
    select.select_by_value("ITQ") # Select option value
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"comDefaultVO\"]/table/tbody/tr/td[2]/button").click()
    time.sleep(1) 
    try:
        info1 = driver.find_element(By.XPATH, "//*[@id=\"content\"]/div[2]/div[2]/table/tbody").text
        info1 = info1.replace("\n"," ")
        p = re.compile("한글엑셀 합격")
        m = p.search(info1) #주어진 문자열의 중에 일치하는지 확인
        if m:
           print("한글엑셀 취득 확인")

        p = re.compile("한글파워포인트 합격")
        m = p.search(info1) #주어진 문자열의 중에 일치하는지 확인
        if m:
            print("한글파워포인트 취득 확인")
        
        p = re.compile("아래한글 합격")
        m = p.search(info1) #주어진 문자열의 중에 일치하는지 확인
        if m:
            print("아래한글 취득 확인")
    except:
        print("취득 내역 없음")
    driver.close()
except:
    driver.close()
    print("로그인 실패")