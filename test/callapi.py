'''from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from pandas import ExcelWriter
import json
import requests

def get_movies():
    headers={'Host':'movie.douban.com','user-agaent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    link='https://movie.douban.com/top250?start=0'
    r=requests.get(link,headers=headers,timeout=10)
    print(type(r.text))
    soup=BeautifulSoup(r.text,features='html.parser')
    print(soup)'''
'''import requests,json
file=open('/Users/zhoujessie/Desktop/timg.jpg','rb').read()
url='https://service.pebkit.com/api/v1/x1/s/media/upload'
header={'content-type':'application/x-www-form-urlencoded','ndcdeviceid':'016add5aea38c14d3d518df24552bc498d5ae1f3276eb264e0090d9b249b24635e00d09ef92f4eccee','auid':'c62800ec-2076-4733-8983-1f4ebccec99f','ndcauth':'sid=AYACfXEBKEsASwFLAU5LAooRn8nOvE4fg4kzR3Yg7AAoxgBLA0sASwRVBIvGeORLBUq3uQhdSwZLZHUuNZywxfiLV1QUdB9fV5AhPcQOUzY'}


r=requests.post(url,data=file,headers=header)
print(json.loads(r.text))'''
import requests,time
from API_Automation.UserList import UserList

def check_in(deviceid=UserList.DeviceId[1],sid=None):
        url_getNDC='https://service.narvii.com/api/v1/g/s/community/joined?pagingType=t&size=100'
        url_getleftNDC='https://service.narvii.com/api/v1/g/s/community/joined?size=100&stoptime=2019-06-30T14%3A23%3A43Z&pagingType=o&start=100'
        if sid is None:
            sid='sid=AYACfXEBKEsASwFLAU5LAooR4i1bMClVy47FQvtcZDtg-ABLA0sASwRVBAAAAABLBUopZxldSwZLZHUuNLmGYmMYRYxSnNCifc3iaJQPMy4'
        else:
            sid='sid='+sid
        header = {'ndcdeviceid': deviceid, 'ndcauth': sid}
        r=requests.get(url_getNDC,headers=header)
        r_=requests.get(url_getleftNDC, headers=header)
        r_=r_.json()
        r=r.json()
        communityList=r['communityList']+r_['communityList']
        print('Total number of community is:',len(communityList))
        for each in communityList:
            ndcId=str(each['ndcId'])
            url = 'https://service.narvii.com/api/v1/x' + ndcId + '/s/check-in'
            print(url)
            data={
	            "timezone": 480,
	            "timestamp": int(time.time()) #1561899474692
            }
            r=requests.post(url,headers=header,json=data)
            if r.ok:
                print('ok',r.text)
            else:
                print('fail',r.text)

check_in(sid='AYACfXEBKEsASwFLAU5LAooQGib4IKGYtK6cTtexKFkUVksDSwBLBFUEAAAAAEsFSn9sGV1LBktkdS7SkQR78yctGC_fNQI6PXa-Kv3caw')