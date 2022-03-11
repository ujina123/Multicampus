# -*- coding:utf-8 -*-

from unittest import result
import requests
import json

def getSiDo():
    # _ajaxCall("/store/getSidoList.do", {}, true, "json", "post",
    url = 'https://www.starbucks.co.kr/store/getSidoList.do'   # end point = root -> 'https://www.starbucks.co.kr/'
    resp = requests.post(url) # url을 post방식으로 요청한다. 
    # print(resp) # <Response [200]> : 성공
    # print(resp.json()) # 응답 받은 형태를 json 객체로 바꿔준다. (requests modul의 기능)

    json_data = resp.json()['list']

    # sido_code, sido_nm = [],[]
    # for i in range(len(json_data)):
    #     sido_code.append(json_data[i]['sido_cd'])
    #     sido_nm.append(json_data[i]['sido_nm'])

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
    
    return res_list


if __name__ == '__main__':
    # 전국의 모든 스타벅스 매장을 저장
    # {'list':[{s_name:'',...},{}, ...]}
    # starbucks_all.json
    list_all = []
    SiDo_all = getSiDo()
    for sido_cd in SiDo_all:
        if sido_cd == '17':
            result = getStore(sido_code=sido_cd)
            list_all.extend(result)
        else:
            gugun_all = getGuGun(sido_cd)
            for gugun in gugun_all:
                result = getStore(gugun_code=gugun)
                list_all.extend(result)

    # print(list_all)
    # print(len(list_all))
    result_dict = {
        'list': list_all
    }

    result_json = json.dumps(result_dict, ensure_ascii=False)
    with open('./stabucks_all.json','w',encoding='utf_8') as f:
        f.write(result_json)
