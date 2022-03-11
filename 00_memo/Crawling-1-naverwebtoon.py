from bs4 import BeautifulSoup
import requests, json

# 원하는 요일의 네이버 웹툰 사이트의 제목과 평점 가지고 오기

weekday = {'월요일':'mon', '화요일':'tue','수요일':'wed','목요일':'thu','금요일':'fri','토요일':'sat','일요일':'sun'}

INPUT = input('요일을 입력해 주세요 : ')

url = f'https://comic.naver.com/webtoon/weekdayList?week='+ weekday[INPUT] # get 방식

req = requests.get(url)

soup = BeautifulSoup(req.text,'html.parser')

webtoons = soup.find('ul', {'class': 'img_list'})
dl_list = webtoons.select('dl')
# print(dl_list)

lst = list()
for dl in dl_list:
    title = dl.a['title']
    star = dl.strong.text
    tmp ={
        'title' : title,
        'star' : star
    }
    lst.append(tmp)

res = {
    'webtoons' : lst
}

# json object
## json.dumps(data) 
res_json = json.dumps(res, ensure_ascii=False) # 아스키 코드 비활성화
print(res_json)

# save json object
with open('naver/webtoons.json','w',encoding='utf-8') as f: # 위에서 해당 파일을 utf-8로 지정 해줘서 안해줘도 상관없음
    f.write(res_json)