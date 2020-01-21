import requests,lxml
from bs4 import BeautifulSoup

url="https://www.dygod.net/html/gndy/dyzz/20200104/112810.html"

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
proxies={'http':'199.116.170.164:8080'}

r=requests.get(url,headers)

r.encoding="gb2312"

soup=BeautifulSoup(r.text,'lxml')

# zoom=soup.find('div',attrs={'id','Zoom'})

div=soup.find('div',attrs={'id':'Zoom'})

print(div)
# print([text.strip() for text in div.find_all(text=True) if text.parent.name !='table' and text.strip()])