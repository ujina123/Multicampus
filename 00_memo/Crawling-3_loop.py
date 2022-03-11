# crawling_loop 

from bs4 import BeautifulSoup
import requests

##1 한 페이지 제목만 크롤링
page = 1
url = f'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage={page}' # get 형식

def CrawlingTitle(url):
    req = requests.get(url)
    # print(req.text) # html documnet
    # print(type(req.text)) # str

    soup = BeautifulSoup(req.text, 'html.parser') # parse tree

    titles = soup.find_all('span',{'class':'title'}) # 해당 태그 모두 가져오기 때문에 반환 값은 리스트!

    # 리스트를 한번에 text로 변경할 수 없기 때문에 for문 사용
    res_titles = [print(title.text.strip()) for title in titles]

    return res_titles

CrawlingTitle(url)


##2 페이지 문자열 리스트로 만들기 
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser') # parse tree

page_num = soup.find('nav',{'class':'pagination'})
# print(type(page_num)) # <class 'bs4.element.Tag'>
page_list = []

for page in page_num:
    if page.text.isdigit():
        page_list.append(page.text)
print(page_list) # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


##3. url에 ['1' ~ '10']까지의 번호를 각각 붙여서 1페이지 부터 10페이지 까지의 모든 제목 출력
url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage='
total_title=[]
for page in page_list:
    url_ = url+page
    total_title.append(CrawlingTitle(url_))

##4. 11페이지부터 ~ 