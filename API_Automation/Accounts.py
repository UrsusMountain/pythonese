import requests,time
from API_Automation.UserList import UserList
class Accounts:

    #函数login_getsid()返回一个sid，即ndcauth，调用方式为Accounts.login_getsid()
    @staticmethod
    def login_getsid(user='jiezhou@narvii.com', passwd='test123',deviceid=UserList.DeviceId[0]):
        url='https://service.pebkit.com/api/v1/g/s/auth/login'
        header={}
        header['ndcdeviceid']=deviceid
        data = {"deviceID": deviceid}
        data['email'] = user
        data['secret'] = str(0) +' '+passwd
        r = requests.post(url, json=data, headers=header)
        response = r.json()  # or response=r.json()将response的json数据解码
        if 'sid' in response:
            sid = response['sid']  # sid=response.get('sid',-1) 获取sid的value，如果不存在则返回-1
            sid = 'sid=' + sid
            print('successful')
            return sid
        else:
            print(r.json())
    def login_getsidnarvii(user='jiezhou@narvii.com', passwd='test123',deviceid=UserList.DeviceId[2]):
        url='https://service.narvii.com/api/v1/g/s/auth/login'
        header={}
        header['ndcdeviceid']=deviceid
        data = {"deviceID": deviceid}
        data['email'] = user
        data['secret'] = str(0) +' '+passwd
        r = requests.post(url, json=data, headers=header)
        response = r.json()  # or response=r.json()将response的json数据解码
        if 'sid' in response:
            sid = response['sid']  # sid=response.get('sid',-1) 获取sid的value，如果不存在则返回-1
            sid = 'sid=' + sid
            print('successful')
            return sid
        else:
            print(r.json())

    #函数logout()用于退出登录
    @staticmethod
    def logout(user='jiezhou@narvii.com',passwd="test123",deviceid=UserList.DeviceId[0]):
        url='https://service.pebkit.com/api/v1/g/s/auth/logout'
        sid = Accounts.login_getsid(user, passwd)
        header={'ndcdeviceid':deviceid,'ndcauth':sid}
        data={
	"locale": "zh_CN",
	"bundleID": "com.pebkit.master",
	"deviceTokenType": 0,
	"clientType": 100,
	"systemPushEnabled": 1,
	"clientCallbackURL": "pebkitapp:\/\/default"
   }
        data['deviceID']=deviceid
        r=requests.post(url,headers=header,json=data)
        print(r.status_code,r.text)

    @staticmethod
    def check_in(user='jiezhou@narvii.com',passwd='test123',deviceid=UserList.DeviceId[2]):
        url_getNDC='https://service.narvii.com/api/v1/g/s/community/joined?pagingType=t&size=100'
        url_getleftNDC='https://service.narvii.com/api/v1/g/s/community/joined?size=100&stoptime=2019-06-30T14%3A23%3A43Z&pagingType=o&start=100'
        sid = Accounts.login_getsidnarvii(user, passwd)
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

Accounts.check_in()



#sid=Accounts.login_getsid('jiezhou@narvii.com','test123')
#print(sid)
#Accounts.logout()

