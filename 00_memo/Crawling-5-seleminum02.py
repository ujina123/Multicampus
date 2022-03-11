from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

input_id = input('id 입력 : ')
input_pw = input('pw 입력 : ')

# ChromeDriver 설정
service = webdriver.chrome.service.Service('./drivers/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.instagram.com/accounts/login/')
sleep(5)

id = driver.find_element(By.NAME,'username')
id.send_keys(input_id)

pw = driver.find_element(By.NAME,'password')
pw.send_keys(input_pw)
sleep(2)

driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(3)').click()

# 로딩 시, refresh() 설정
# sleep(2)
# driver.refresh()
sleep(3)
later = driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div/div/button')
later.click()

later2 = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[3]/button[2]')
later2.click()
