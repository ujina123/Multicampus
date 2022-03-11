# Naver Webtoons 

0. request 설치
```
>  pip install requests
```
`requests` : 사용자가 만든 모듈 <br>
`urlib.request` : python 내장 라이브러리 <br>
: 둘 다 기능은 같지만, **requests가 사용하기 더 편리** 하여 설치했음


1. 해당 python file은 utf-8로 인코딩 되게 설정해주기 
   - pyhonn file 맨 위에 아래 코드입력 
   - 형태가 # 부터 시작인거임
```python
# -*- coding : utf-8 -*-
```
<br>

2. requests 사용

```python
from bs4 import BeautifulSoup
import requests
import json

url = 'https://comic.naver.com/webtoon/weekdayList?week=wed'
resp = requests.get(url) # 해당 url로 get방식으로 요청할 것이다. / post 방식일 경우 .post
print(resp) 
print(resp.text)
```
<br>

3. BeautifulSoup  
```python
# BeautifulSoup 이 parse tree를 만들어 준다. 
soup = BeautifulSoup(resp.text, 'html.parser')
# print(type(soup)) : object type

webtoons = soup.find('ul', {'class': 'img_list'})

dl_list = webtoons.select('dl')

lst = list()
for dl in dl_list:
    title = dl.a['title']
    star = dl.strong.text

    tmp = dict()
    tmp['title'] = title
    tmp['star'] = star

    lst.append(tmp)

#print(lst)

res = dict()
res['webtoons'] = lst
```
<br>

4. json

https://www.json.org/json-en.html
```python
# json object
## json.dumps(data) 
res_json = json.dumps(res, ensure_ascii=False) # 아스키 코드 비활성화
print(res_json)

# save json object
with open('naver/webtoons.json','w',encoding='utf-8') as f: # 위에서 해당 파일을 utf-8로 지정 해줘서 안해줘도 상관없음
    f.write(res_json)
```
<br>

5. https://naver **/robots.txt**

**/robots.txt** : 크롤링 하려는 사이트의 설정을 볼 수 있다.  <br>
봇(bot) : 자동으로 작업을 수행하는 것 , 따로 접속 권한은 없음
```
User-agent: *      : 접속 ( 해당 url에 접속 가능한 user )
Disallow: /        : 금지 ( / 부터 )
Allow : /$         : 이부분만 허용 (/$ : 처음 시작 화면)
```
<br>

6. open api

: 원하는 형태로 요청하면 가지고 있는 데이터를 응답해주는 것 
```
.xml
.json
.csv
.tsv
```
