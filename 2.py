import os,time,requests
url =  "http://1.1.1.3/ac_portal/login.php"
data = {'opr':'pwdLogin','userName':'90','pwd':'Az123456!','rememberPwd':'0'}
headers = {"User-Agent":"GOD"}
while True:
    r = requests.get("https://www.baidu.com/")
    result = r.status_code
    if result == 200:
        print(str(result)+' succ')
        time.sleep(10)
    else:
        print(str(result)+' fail')
        requests.post(url,headers=headers,data=data)
        time.sleep(1)
