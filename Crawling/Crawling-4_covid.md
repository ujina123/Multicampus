## 
### endpoint
서버 : http://openapi.data.go.kr/openapi/service/rest/Covid19/
endpoint

### ServiceKey
```python
service_key='VXBYQ69L5Fwe5N6ROU%2BQDFR ... LtqMhSaBV2BfjIAhytbw2lcWmg%3D%3D' # 일반 인증키 (Encoding)
url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}'
```
### xml.etree
https://docs.python.org/3/library/xml.etree.elementtree.html?highlight=xml%20etree#xml.etree.ElementTree.XML

install 라이브러리는 pypi.doc 에서 확인 

### 정규 표현식 사용 (re)

```python
from xml.etree import ElementTree
import requests
import re

service_key='VXBYQ69L5Fwe5N6ROU%2BQDFR ... LtqMhSaBV2BfjIAhytbw2lcWmg%3D%3D' # 일반 인증키 (Encoding)
url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}'

# print(url)

resp = requests.get(url) # xml documnet로 요청
# print(resp.text)

## 객체로 만들기 (파싱) _ parse tree 만들기
tree = ElementTree.fromstring(resp.text) # resp.text : 문자열
# print(tree) # <Element 'response' at 0x10453cd60> 객체,

for item in tree[1][0]: # body > itmes
    if item.find('gubun').text =='합계':
        incDec_ = item.find('incDec').text
        localOccCnt_ = item.find('localOccCnt').text
        overFlowCnt_ = item.find('overFlowCnt').text
        stdDay_ = re.sub(r'(\D)+','',item.find('stdDay').text)

        print(f'[{stdDay_[2:4]}/{stdDay_[4:6]}/{stdDay_[6:8]}]\n'
              f'일일합계:{incDec_} \n'
              f'국내발생:{localOccCnt_} \n'
              f'해외발생:{overFlowCnt_}')
```

결과<br>
![abc](../Crawling/imags/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-03-11%20%EC%98%A4%ED%9B%84%202.56.37.png)