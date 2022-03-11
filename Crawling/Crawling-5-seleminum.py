'''
https://www.selenium.dev/documentation/

https://chromedriver.chromium.org/

seleminum : automates browsers

> pip install seleminum

사용 : from seleminum import webdriver

ChromeDriver 설치 후, Drivers 폴더에 확장자 넣어주기
'''

from selenium import webdriver
from bs4 import BeautifulSoup

tag = input('search tags: ')
url = f'https://www.instagram.com/explore/tags/{tag}'

service = webdriver.chrome.service.Service('./drivers/chromedriver')
driver = webdriver.Chrome(ervice=service) # Chrome 객체 생성

driver.implicitly_wait(3) # 3초 기다렸다가 
driver.get(url)  # url 가지고 와주세요

soup = BeautifulSoup(driver.page_source, 'html.parser') # driver.page_source : webdriver가 현재 가지고 있는 page source
img_list = soup.find_all('div',class_='KL4Bh')

for img in img_list:
    print(img)
