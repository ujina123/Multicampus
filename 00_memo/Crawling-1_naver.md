# Naver movies 

1. 가상환경 만들기  <br>
```
conda create -n mycrawling python==3.9 
conda activate mycrawling
```

1. Pycharm project open

    방법 1) Pycharm -> new project -> previously configured interpreter (가상환경 설정) -> … 클릭 -> Conda environment -> 해당 가상환경 선택 

    방법 2) 만약 바로 파일을 open 했다면 오른쪽 아래 python3.9 클릭 후, 가상환경 설정
<br>
<br>

2. beautifulsoup4 설치 <br>
    beautifulsoup? HTML이나 XML 형태의 데이터를 가져오는 라이브러리 
```
(mycrawling) ~ workspace_crawling >  pip install beautifulsoup4
```
https://www.crummy.com/software/BeautifulSoup/bs4/doc/



<br>
<br>
3. Parser / ParserTree 란?

— ```Parser```
컴파일러의 일부로서 원시 프로그램 
컴파일러나 인터프리터에서 원시 프로그램을 읽어 들여, 그 문장의 구조를 알아내는 구문 분석(pasing)을 행하는 프로그램
내가 원하는 것을 가져오기 위해서 이걸 바꿔 주는 것을 paser라고 한다. 

— ```Parser Tree```
객체로 구조화 
<br>
<br>
4. 크롤링 / 스크래핑 이란 ?

— ```크롤링``` : 다 가지고 오는 것

— ```스크래핑``` : 크롤링 한 것에서 내가 필요한 것만 가지고 오는 것
<br>
<br>
5. 사용방법 
```python
from bs4 import BeautifulSoup

BeautifulSoup(markup, "html.parser")
```
* PyCharm 실행 : control + shift + R
---

<br>

0. Naver 폴더 생성 -> movies.py 생성
네이버 영화의 상영작,예정작에서 영화제목과 평점을 가지고 오기 
**movies.py**
```python
from bs4 import BeatifulSoup
import urllib.request # 클라이언트 역할을 한다. 서버에 요청하면 요청한 응답을 받는다. 

# request가 있으면 무조건 서버로 요청했다고 생각하면 된다. 
# urllib이 가진 request로 urlopen 함수를 실행했더니 url를 열어서 request가 서버로 요청한다. 서버는 object로 응답(response => document type)!
resp = urllib.request.urlopen('movie.naver.com/movie/running/current.naver')
print(resp) # http response object, documnet type이 포함되어 있다. 

# BeautifulSoup(가져올 document, 누가 가져올 것인지)
soup = BeautifulSoup(resp, 'html.parser')
print(type(soup))
'''
1. 해당 url에 요청했더니 서버가 응답
2. BeautifulSoup을 통해 응답된 것을 파이썬 내장 parser을 통해 parse tree(노드 구조)를 만들어준다. 
'''

movies = soup.find_all('dl',class_='lst_dcs')
# print(movies)
# print(movies[0])

# 방법1)
for movie in movies:
    title = movie.a.string
    star = movie.find_all('span',class_='num')[0].string
    print(f'{title} [{star}]')

# 방법2)
for movie in movies:
    title = movie.find('a').get_text()
    star = movie.find('span', class_='num').text
    print(f'{title} [{star}])
```

```
.find : 가장 처음 찾아 주는 애를 응답 <br>
.find_all : 다 찾아라 <br>
=> find_all이 가장 최근이다. 
```