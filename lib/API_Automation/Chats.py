import requests,math
from lib.API_Automation.Accounts import Accounts
from lib.API_Automation.UserList import UserList
from lib.API_Automation.community import community
class Chats:
    @staticmethod
    def sendMessage(thread=None,content='hi',user='jiezhou@narvii.com',passwd='test123',deviceid=UserList.DeviceId[0]):
        if thread is None:
            thread='e62baf30-dc13-4135-b702-807e3244b29d'  #dev Heya社区Let's chat!
        url='https://service.pebkit.com/api/v1/x1/s/chat/thread/'+thread+'/message'
        message={"type":0,"content":content,"clientRefId":108198349}
        sid = Accounts.login_getsid(user,passwd)
        header={'ndcdeviceid':deviceid,'ndcauth':sid}
        r=requests.post(url,json=message,headers=header)
        if r.ok:
            print(r.text)
        else:
            print('fail',r.text)

    #This method will help you mark all unread meaasage as read!
    @staticmethod
    def read_allchat(user='jiezhou@narvii.com', passwd='test123',deviceid=UserList.DeviceId[2]):
        ndcList=community.get_ndcList(user,passwd,deviceid)
        sid = Accounts.login_getsidnarvii(user,passwd,deviceid)
        header={'ndcdeviceid':deviceid,'ndcauth':sid}
        print('MyJoinedCommunity',ndcList)
        threadList=[]
        ndclist=[]
        for z in range(math.ceil(len(ndcList)/25)):
            url='https://service.narvii.com/api/v1/g/s/chat/thread-check/human-readable?ndcIds='+'%2C'.join(ndcList[z*25:25*(z+1)])
            r=requests.get(url,headers=header)
            r=r.json()
            communityDict=r['threadCheckResultInCommunities']
            for x in communityDict:
                if communityDict[x]:
                    threadList+=communityDict[x]
                    ndclist.append(str(x))
                else:
                    continue
        print('Unread message number is:',len(threadList))
        for i in range(len(ndclist)):
            threadId=threadList[i]['threadId']
            ndcId = ndclist[i]
            url_1 = 'https://service.narvii.com/api/v1/x' + ndcId + '/s/chat/thread/' + threadId + '/message'
            r = requests.get(url_1, headers=header).json()
            messageId = r['messageList'][0]['messageId']
            url_2 = 'https://service.narvii.com/api/v1/x' + ndcId + '/s/chat/thread/' + threadId + '/mark-as-read'
            data = {"messageId": messageId,
                    "createdTime": "2019-07-03T09:31:51Z"}
            res = requests.post(url_2, json=data, headers=header)
            if res.ok:
                print('Result is ok', res.text)
            else:
                print('Result is fail', res.text)




#Chats.read_allchat()
#Chats.read_allchat()
#for i in range(0,100):
'''while 1:  #非空字符，数字，非空列表等，都是True
    l=['hi','hello','haha','how are you','OMG','This is so cool','Great',"Well Done"]
    Chats.sendMessage(content=l[random.randint(0,len(l)-1)])
    time.sleep(0.1)
    Chats.sendMessage(content=l[random.randint(0,len(l)-1)],user=UserList.Userlist['user_2'][0],passwd=UserList.Userlist['user_2'][1])
    time.sleep(0.1)
    Chats.sendMessage(content=l[random.randint(0,len(l)-1)],user=UserList.Userlist['user_4'][0],passwd=UserList.Userlist['user_4'][1])
    time.sleep(0.1)
    Chats.sendMessage(content=l[random.randint(0,len(l)-1)],user=UserList.Userlist['user_3'][0],passwd=UserList.Userlist['user_3'][1])
    time.sleep(0.1)'''