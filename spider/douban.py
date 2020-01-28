import requests,time,os
from bs4 import BeautifulSoup

url='https://maoyan.com/board/4'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

r=requests.get(url)
print(r.status_code)

soup=BeautifulSoup(r.text,'lxml')

wrap=soup.find('div',attrs={'dl':'board-wrapper'})
print(wrap)
'''
for i in wrap:
    name=soup.i['title']
    print(name)
''' 