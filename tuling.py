#coding=utf8
import itchat
import requests, json

apiUrl = 'http://www.tuling123.com/openapi/api'

# 根据输入的 content 信息，获取自动回复信息
def GetReply(content):
    data = {
        'key'    : 'bfb6d0d943784a9ba77467aa64c5b7d5', # Tuling Key 注册后可以免费获得一个
        'info'   : u'%s'%content,                   # 这是我们发出去的消息
        'userid' : 'www.xrkzn.cn',                  
    }
    r = requests.post(apiUrl, data=data)
    js = json.loads(r.content)
    return js['text']

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # print GetReply(msg.text)
    return GetReply(msg.text)

if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    itchat.run()



