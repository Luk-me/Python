
import itchat,time
#在命令行顯示二維碼

itchat.auto_login(enableCmdQR=2,hotReload=True)

users=itchat.search_friends("初心")
userName= users[0]['UserName']
print(userName)
itchat.send('你好info南',toUserName=userName)