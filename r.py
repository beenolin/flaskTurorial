import requests
import os
import sys
import datetime
import time
#pip install matplotlib
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import json
# 중국 : 112 / 일본 : 130 / 미국 : 275
url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
serviceKey = 'KpmHZAK1rNp%2FHFwSsSBW9PdRszAgJ%2FXBzDQgKRDupEDG0tz1lvwA4afI8D4OYLJuDtIG%2BYIJ2XOdz6ezzqyn3Q%3D%3D'
serviceKey = requests.utils.unquote(serviceKey) # requests의 디코딩 하는 기능

params = {
    '_type' : 'json', # json을 지원하는 경우 _type을 붙어야됨.
    'serviceKey' : serviceKey,
    'YM' : '202004',
    'NAT_CD' : '112',
    'ED_CD' : 'E'
}
response = requests.get(url, params=params)
print(response.status_code)
def get_request_url(ym, nat_cd, ed_cd='E'):
    try:
        url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
        serviceKey = 'KpmHZAK1rNp%2FHFwSsSBW9PdRszAgJ%2FXBzDQgKRDupEDG0tz1lvwA4afI8D4OYLJuDtIG%2BYIJ2XOdz6ezzqyn3Q%3D%3D'
        serviceKey = requests.utils.unquote(serviceKey) # requests의 디코딩 하는 기능

        params = {
            '_type' : 'json', # json을 지원하는 경우 _type을 붙어야됨.
            'serviceKey' : serviceKey,
            'YM' : ym,
            'NAT_CD' : nat_cd,
            'ED_CD' : ed_cd
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            rs_str = '{} Url Request Success'
            print(rs_str.format(datetime.datetime.now()))
            return response.json()
        else:
            print('status_code : '+response.status_code)
            return None

    except Exception as e:
        print(e)
        return None

ym = '202004'
nat_cd = '112'
response = get_request_url(ym, nat_cd, ed_cd='E')
print(response)
jsonResult = []


# 중국 : 112 / 일본 : 130 / 미국 : 275
nStartYear = 2005
nEndYear = 2020
nat_cd = '275'
for year in range(nStartYear, nEndYear):
    for month in range(1, 13):
        ym = '{0}{1:0>2}'.format(str(year), str(month))
        #print(ym)
        response = get_request_url(ym, nat_cd, ed_cd='E')
        check = response['response']['header']['resultMsg']
        if(check == 'OK'):
            natKorNm = response['response']['body']['items']['item']['natKorNm']
            num = response['response']['body']['items']['item']['num']
            item = {
                'nat-name': natKorNm,
                'nat_cd' : nat_cd,
                'yyyymm' : ym,
                'visit_cnt' : num
                   }
            jsonResult.append(item)
fn = '해외방문객정보.json'
with open(fn, 'w', encoding='utf-8') as outfile:
    retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(retJson)
cnVisit = []
visitYM = []
index = [] # 변수값
i = 0
for item in jsonResult:
    index.append(i)
    cnVisit.append(item['visit_cnt'])
    visitYM.append(item['yyyymm'])
    i += 1
#print(cnVisit[0], visitYM[0], index[0])
# 한글폰트설정
plt.rcParams["font.family"] = "Calibri"
font_loca = 'c:/windows/fonts/Calibri.ttf'
font_name = font_manager.FontProperties(fname=font_loca).get_name()
matplotlib.rc('font', family=font_name)

plt.xticks(index, visitYM) # x 변수값
plt.plot(index, cnVisit) # y 변수값
plt.xlabel('방문월') # x 변수명
plt.ylabel('방문객수') # y 변수명
plt.grid(True) # 선 생기게 만듬
plt.show()