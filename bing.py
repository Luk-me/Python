import os,time,requests
from bs4 import BeautifulSoup

# url = 'https://bing.ioliu.cn/ranking'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

# r = requests.get(url, headers)
# soup = BeautifulSoup(r.text, 'lxml')

# img = soup.findAll('div', attrs={'class': 'item'})
down_dir = os.path.join(os.getcwd(), '1234/')
if not os.path.exists(down_dir):
    os.mkdir(down_dir)
i = 1
# for item in img:
#     imgName = item.find('h3').text
#     print(imgName)
#     filename = str(i)+'.jpg'
#     url_child = item.find('img').get('src')
#     print(url_child)
#     f = requests.get(url_child)
#     i = i+1
#     print(down_dir+filename)
#     with open(down_dir+filename, 'wb')as g:
#         for chunk in f.iter_content(100000):
#             g.write(chunk)

num=1
for i in range(1,117):
    if i==1:
        url='https://bing.ioliu.cn/ranking'
    else:
        url='https://bing.ioliu.cn/ranking?p='+str(i)
    r=requests.get(url,headers)
    soup=BeautifulSoup(r.text,'lxml')
    img=soup.findAll('div',attrs={'class':'item'})
    for item in img:
        filename=str(num)+'.jpg'
        url_child=item.find('img').get('src')
        print(url_child)
        f=requests.get(url_child)
        num=num+1
        with open(down_dir+filename,'wb') as g:
            for q in f.iter_content(100000):
                g.write(q)
                time.sleep(0.5)
