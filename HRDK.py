from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.q-net.or.kr/man001.do?id=man00103&gSite=Q&gId=&login=Y"

driver.get(url)
driver.find_element(By.ID, "mem_id").send_keys(str(input("큐넷 아이디를 입력하세요 : ")))
time.sleep(1)
driver.find_element(By.ID, "mem_pswd").send_keys(str(input("큐넷 비밀번호를 입력하세요 : ")))
time.sleep(1)
driver.find_element(By.CLASS_NAME, "btn_login").click()
time.sleep(1) 
try:
    driver.get("https://www.q-net.or.kr/myp003.do?id=myp00301&gSite=Q&gId=")
    time.sleep(1) 
except:
    driver.close()
    print("로그인에 실패 했습니다.")
try:
    info1 = driver.find_element(By.XPATH, "//*[@id=\"content\"]/div[2]/div[2]/table/tbody").text
    info1 = info1.split("\n")
    for i in info1:
        a = i.split(" ")
        try:
            if (a[4] == "실기" and a[6] == "정보기기운용기능사" and a[7] == "합격") and (a[4] == "실기" and a[6] == "정보처리기능사" and a[7] == "합격"):
                print("정보처리기능사, 정보기기운용기능사 취득 확인")
            if a[4] == "실기" and a[6] == "정보처리기능사" and a[7] == "합격":
                print("정보처리기능사 취득 확인")
            if a[4] == "실기" and a[6] == "정보기기운용기능사" and a[7] == "합격":
                print("정보기기운용기능사 취득 확인")
        except:
            pass
    print("취득 내역이 없습니다.")
except:
    print("취득 내역이 없습니다.")

driver.close()