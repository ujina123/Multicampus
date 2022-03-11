
'''
_ajaxCall("/store/getSidoList.do", {}, true, "json", "post", function (_response){)
# 코드 추론 : _ajaxCall(url, {보내는 데이터}, asyac, 받는 데이터 형태, 전송방식, 성공했을 때 콜백함수)
'''

# -*- coding:utf-8 -*-

import requests
import json

def getSiDo():
    # _ajaxCall("/store/getSidoList.do", {}, true, "json", "post",
    url = 'https://www.starbucks.co.kr/store/getSidoList.do'   # end point = root -> 'https://www.starbucks.co.kr/'
    resp = requests.post(url) # url을 post방식으로 요청한다. 
    # print(resp) # <Response [200]> : 성공
    # print(resp.json()) # 응답 받은 형태를 json 객체로 바꿔준다. (requests modul의 기능)

    json_data = resp.json()['list']

    sido_code = list(map(lambda x: x['sido_cd'], json_data))
    sido_nm = list(map(lambda x: x['sido_nm'], json_data))
    sido_dict = dict(zip(sido_code,sido_nm))
    # print(sido_dict)
    return sido_dict

def getGuGun(sido):
    # __ajaxCall("/store/getGugunList.do", {"sido_cd":sido}, true, "json", "post",  function (_response){}
    url = 'https://www.starbucks.co.kr/store/getGugunList.do' # post 방식이어서 뒤에 code가 들어가는 것은 좋은 방법이 아니다.
    param = {'sido_cd':sido}
    resp = requests.post(url, param)
    json_data = resp.json()['list']

    gugun_cd = list(map(lambda x:x['gugun_cd'], json_data))
    gugun_nm = list(map(lambda x:x['gugun_nm'], json_data))

    gugun_dict = dict(zip(gugun_cd,gugun_nm))
    print(gugun_dict)
    return gugun_dict

def getStore(sido_code='', gugun_code=''):
    # ajax 캐시문제를 해결하기 
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    param = {'ins_lat':'37.56682', 'ins_lng': '126.97865', 'p_sido_cd' :sido_code,
            'p_gugun_cd':gugun_code, 'in_biz_cd':'', 'set_date': ''}
    resp = requests.post(url, param)
    store_list = resp.json()['list']
    
    res_list =[]
    for store in store_list:
        store_dict={
            's_name' : store['s_name'],
            'tel' : store['tel'],
            'doro_addr' : store['doro_address'],
            'lat' : store['lat'],
            'lot' : store['lot']
        }
        res_list.append(store_dict)
    
    res_dict = dict()
    res_dict['store_list'] = res_list
    print(res_dict)

    # json 저장 
    result_json= json.dumps(res_dict, ensure_ascii = False)
    with open('starbucks01.json','w',encoding='utf-8') as f:
        f.write(result_json)

    return result_json


if __name__ == '__main__':
    print(getSiDo())
    sido = input('도시 코드를 입력해 주세요 : ')
    if sido == '17':
        getStore(sido_code=sido, gugun_code='')
    else:
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해 주세요 : ')
        getStore(gugun_code=gugun)