import requests
from lib.API_Automation.UserList import UserList
from lib.API_Automation.Accounts import Accounts

class community:
    @staticmethod
    def get_ndcList(user='jiezhou@narvii.com',passwd='test123',deviceid=UserList.DeviceId[2]):
        url_getNDC='https://service.narvii.com/api/v1/g/s/community/joined?pagingType=t&size=100'
        url_getleftNDC='https://service.narvii.com/api/v1/g/s/community/joined?size=100&stoptime=2019-06-30T14%3A23%3A43Z&pagingType=o&start=100'
        sid = Accounts.login_getsidnarvii(user, passwd)
        header = {'ndcdeviceid': deviceid, 'ndcauth': sid}
        r=requests.get(url_getNDC,headers=header)
        r_=requests.get(url_getleftNDC, headers=header)
        r_=r_.json()
        r=r.json()
        communityDict=r['communityList']+r_['communityList']
        ndcList=[]
        for each in communityDict:
            ndcId=str(each['ndcId'])
            ndcList.append(ndcId)
        return ndcList

#community.get_ndcList()