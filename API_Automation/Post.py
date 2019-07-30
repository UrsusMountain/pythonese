import json,requests,random,time
from API_Automation.ImgURL import Imgurl
from API_Automation.Accounts import Accounts
from API_Automation.NDCID import NDCID
from API_Automation.UserList import UserList


class Post:
    #函数Post.uploadImage_getImageUrl()返回一个图片的url，可用于post发送图片
    @staticmethod
    def uploadImage_getImageUrl(imge='/Users/zhoujessie/Desktop/e.jpg', user='jiezhou@narvii.com', passwd='test123', community='x1'):
    #imge=‘/.../.../xx.jpg’，为文件的路径
        img = open(imge,'rb').read()
        url = 'https://service.pebkit.com/api/v1/'+community+'/s/media/upload'
        sid = Accounts.login_getsid(user, passwd)
        header={'ndcdeviceid':'016add5aea38c14d3d518df24552bc498d5ae1f3276eb264e0090d9b249b24635e00d09ef92f4eccee','ndcauth':sid}
        r = requests.post(url, data=img, headers=header)
        if r.ok:
            print(r.status_code)
            r=json.loads(r.text)
            img_url=r['mediaValue']
            print(img_url)
            return img_url
        else:
            print(r.text)


    #函数createimageBlog()会自动创建带图片（一张）的blog，也可自定义图片和content，title，其中img必须为url
    @staticmethod
    def createImageBlog(content='Test', title='Test',img=None):
        if img is None:
            img = Imgurl.URLs[random.randint(0, (len(Imgurl.URLs) - 1))]
        else:
            img = img
        data = {  # data的数据类型为字典
            "taggedBlogCategoryIdList": [],
            "mediaList": [
                [100, img, None, None, None, None]
            ],
            "content": "Test",
            "keywords": None,
            "eventSource": "GlobalComposeMenu",
            "contentLanguage": "en",
            "title": "Test",
            "type": 0,
            "timestamp": 1560950520872,
            "extensions": {
                "promoteInfo": None,
                "quizPlayedTimes": 0,
                "style": {
                    "coverMediaIndexList": None
                },
                "pollSettings": None,
                "__disabledLevel__": 0,
                "quizInBestQuizzes": False,
                "pageSnippet": None,
                "fansOnly": False,
                "quizTotalQuestionCount": 0,
                "headlineStyle": None,
                "featuredType": 0
            }
        }
        data['mediaList'][0][1] = img
        data['content'] = content
        data['title'] = title
        sid = Accounts.login_getsid()
        header = {"ndcdeviceid": UserList.DeviceId[0],
                  'ndcauth': sid}
        url = 'https://service.pebkit.com/api/v1/x1/s/blog'
        r = requests.post(url, json=data, headers=header)
        print(r.ok)
        print(r.json())  # 将返回的json格式的内容解码为字典

    @staticmethod
    def comment(user='jiezhou@narvii.com',passwd='test123',content='This is comment',ndcid=NDCID.NDC_dev['Heya'],followingfeed=False,latestfeed=True):
        if followingfeed is True:
            type='blog-following'
        elif latestfeed is True:
            type='blog-all'
        else:
            print('attribute followingfeed and latestfeed is needed at least one of them')
            return
        url='https://service.pebkit.com/api/v1/'+ndcid+'/s/feed/'+type+'?pagingType=t&size=25'
        sid=Accounts.login_getsid(user,passwd)
        header={"ndcdeviceid": UserList.DeviceId[0],'ndcauth': sid}
        r=requests.get(url,headers=header)
        response=r.json()
        blogList=response['blogList']
        while True:
            for i in range(0,len(blogList)):
                blogId=response['blogList'][i]['blogId']
                commentContent={
                 "timestamp": 1561294641324,
                 "type": 0,
                 "mediaList": None,
                 "eventSource": "PostDetailView"
                  }
                commentContent['content']=content+str(i+1)
                url2='https://service.pebkit.com/api/v1/'+ndcid+'/s/blog/'+blogId+'/comment'
                r=requests.post(url2,headers=header,json=commentContent)
                if r.ok:
                 print('ok',r.text)
                else:
                 print(r.status_code,r.text)
                 break

    @staticmethod
    def discover_comment(user='jiezhou@narvii.com',passwd='test123'):
        url = 'https://service.pebkit.com/api/v1/g/s/topic/0/feed/story?size=5&language=en&type=discover-list&pagingType=t&v=2.0.0'
        sid=Accounts.login_getsid(user,passwd)
        header={"ndcdeviceid": UserList.DeviceId[0],'ndcauth': sid}
        r=requests.get(url,headers=header)
        response=r.json()
        blogList=response['blogList']
        for blog in blogList:
            blogId=blog['blogId']
            url_comment = 'https://service.pebkit.com/api/v1/g/s/blog/' + blogId + '/g-comment'
            data={
                "content": "this is a serious comment",
                "type": 0,
                "mediaList": None,
                "eventSource": "CommentDetailView"
               }
            r=requests.post(url_comment,headers=header,json=data)
            if r.ok:
                print(r.status_code,r.text)
            else:
                print('fail',r.text)

    #upload a video to story, will return the url of the video
    @staticmethod
    def upload_video(user='jiezhou@narvii.com',passwd='test123',file='/Users/zhoujessie/Desktop/12.mp4'):
        fo={'video.mp4':open(file,'rb')}
        url='https://up1.pebkit.com/api/v1/g/s/media/upload/target/story'
        deviceid='016DEEDA0CC959DFAA51E71348B5F16D1E6B3D0FEA1FF26BE9BC5603E97A12A86BE34EECB5BC0CB407'
        sid=Accounts.login_getsid(user,passwd)
        header = {'ndcdeviceid': deviceid, 'ndcauth': sid}
        r=requests.post(url,files=fo,headers=header)
        if r.ok:
            print('ok',r.text)
            videoUrl = r.json()['mediaValue']
            return videoUrl
        else:
            print('fail',r.text)

    #get cover image for story
    @staticmethod
    def upload_coverimage(user='jiezhou@narvii.com',passwd='test123',file='/Users/zhoujessie/Desktop/timg.jpg'):
        url='https://service.pebkit.com/api/v1/g/s/media/upload'
        deviceid='016DEEDA0CC959DFAA51E71348B5F16D1E6B3D0FEA1FF26BE9BC5603E97A12A86BE34EECB5BC0CB407'
        sid=Accounts.login_getsid(user,passwd)
        header={'ndcdeviceid': deviceid, 'ndcauth': sid,'content-type':'application/octet-stream','content-type':'image/jpg'}
        data=open(file,'rb').read()
        r=requests.post(url,headers=header,data=data)
        if r.ok:
            print('ok',r.text)
            imageUrl=r.json()['mediaValue']
            return imageUrl
        else:
            print('fail',r.text)

    @staticmethod
    def create_story(videoFile='/Users/zhoujessie/Desktop/12.mp4',imageFile='/Users/zhoujessie/Desktop/timg.jpg',user='jiezhou@narvii.com',passwd='test123'):
        '''imageList=[x for x in os.listdir('/Users/zhoujessie/Desktop/videospic/pics') if os.path.splitext(x)[1]=='.jpg']
        videoList=[x for x in os.listdir('/Users/zhoujessie/Desktop/videospic/videosfortest') if os.path.splitext(x)[1]=='.mp4']
        imageFile='/Users/zhoujessie/Desktop/videospic/pics/'+imageList[random.randint(0,len(imageList)-1)]
        videoFile='/Users/zhoujessie/Desktop/videospic/videosfortest/'+videoList[random.randint(0,len(videoList)-1)]
        print(imageFile,videoFile)'''
        coverimageUrl=Post.upload_coverimage(file=imageFile)
        videoUrl=Post.upload_video(file=videoFile)
        print('coverimage',type(coverimageUrl),coverimageUrl)
        print('videourl',type(videoUrl),videoUrl)
        url='https://service.pebkit.com/api/v1/x1/s/blog'
        deviceid = '016DEEDA0CC959DFAA51E71348B5F16D1E6B3D0FEA1FF26BE9BC5603E97A12A86BE34EECB5BC0CB407'
        sid=Accounts.login_getsid(user,passwd,deviceid)
        header={'ndcdeviceid':deviceid,'ndcauth':sid}
        data={
            "extensions": {
                "fansOnly": False,
                "style": {
                    "coverMediaList": [
                        [100,
                         'coverurl',
                         None]
                    ]
                }
            },
            "duration": 0,
            "publishToGlobal": True,
            "sceneList": [{
                "media": [123,
                          'videourl',
                          None, None, None, {
                              "coverImage":'image',
                              "duration": 7.386000156402588
                          }],
                "metadata": {
                    "targetWidth": 720,
                    "targetHeight": 1280,
                    "videoClipList": [{
                        "backgroundColor": "#000000",
                        "childClips": [{
                            "rawWidth": 1080,
                            "rawHeight": 1920,
                            "targetRect": [0.0, 0.0, 1.0, 1.0],
                            "bitrate": 23068,
                            "frameRate": 60,
                            "durationInMs": 14034,
                            "videoSource": 1,
                            "isDynamicCropping": False,
                            "speedTimes": "1.9"
                        }]
                    }],
                    "sceneType": 2,
                    "musicTrackList": [],
                    "textTrackList": [],
                    "stickerList": [],
                    "durationInMs": 7386
                },
                "pollAttach": {
                    "attachId": None,
                    "polloptList": [{
                        "createdTime": None,
                        "globalVotedValue": 0,
                        "globalVotesCount": 0,
                        "mediaList": None,
                        "parentId": None,
                        "parentType": 0,
                        "polloptId": None,
                        "refObject": None,
                        "refObjectId": None,
                        "refObjectType": 0,
                        "status": 0,
                        "title": "Op1",
                        "type": 0,
                        "uid": None,
                        "votedValue": 0,
                        "votesCount": 0,
                        "votesSum": 0
                    }, {
                        "createdTime": None,
                        "globalVotedValue": 0,
                        "globalVotesCount": 0,
                        "mediaList": None,
                        "parentId": None,
                        "parentType": 0,
                        "polloptId": None,
                        "refObject": None,
                        "refObjectId": None,
                        "refObjectType": 0,
                        "status": 0,
                        "title": "Op2",
                        "type": 0,
                        "uid": None,
                        "votedValue": 0,
                        "votesCount": 0,
                        "votesSum": 0
                    }],
                    "title": "PollPlay"
                },
                "question": {
                    "extensions": {
                        "quizQuestionOptList": [{
                            "isCorrect": True,
                            "mediaList": None,
                            "optId": None,
                            "qhash": None,
                            "title": "Aaaaaaaaaaa"
                        }, {
                            "isCorrect": False,
                            "mediaList": None,
                            "optId": None,
                            "qhash": None,
                            "title": "Bbbbbbbbbbbbbbbbbbbbbbb"
                        }, {
                            "isCorrect": False,
                            "mediaList": None,
                            "optId": None,
                            "qhash": None,
                            "title": "Ccc"
                        }, {
                            "isCorrect": False,
                            "mediaList": None,
                            "optId": None,
                            "qhash": None,
                            "title": "Ddddddddddd"
                        }]
                    },
                    "mediaList": None,
                    "parentId": None,
                    "parentType": 0,
                    "quizQuestionId": None,
                    "title": "Quizaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            }],

            "title": "Post Story2",
            "type": 9,
            "metadata": {
                "coverImageSource": 1
            },
            "contentLanguage": "en",
            "eventSource": "ComposeMenu",
            "timestamp": int(time.time())
        }
        data['sceneList'][0]['media'][1] = videoUrl
        data['sceneList'][0]['media'][5]['coverImage'] = coverimageUrl
        data['metadata']['coverImage'] = coverimageUrl
        data['extensions']['style']['coverMediaList'][0][1] = coverimageUrl
        r=requests.post(url,headers=header,json=data)
        if r.ok:
            print('Uploaded!',r.text)
        else:
            print('fail to upload the story',r.text)



Post.create_story()

#imge='/Users/zhoujessie/Desktop/e.jpg'
#Post.uploadImage_getImageUrl(imge)
#Post.createimageBlog('test','title')


