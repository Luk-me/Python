import requests
import time
import threading
import os
import random
from bs4 import BeautifulSoup



def get_img_url(down_dir,url):
    r=requests.get(url)
    r.encoding="UTF-8"
    soup=BeautifulSoup(r.text,'lxml')
    div=soup.find('div',attrs={'class':'page-content text-center'})
    a=div.findAll('a',attrs={'class':'col-xs-6 col-sm-3'})
    for item in a:
        img_url=item.find('img',attrs={'referrerpolicy':'no-referrer'}).get('data-original')
        img_title=item.find('p').text
        print(img_url)
        print(img_title)
        filename=img_title
        f=requests.get(img_url)
        with open(down_dir+filename+".jpg",'wb')as g:
            for j in f.iter_content(10240):
                g.write(j)

def main():
    down_dir=os.path.join(os.getcwd(),'emjoys/')
    if not os.path.exists(down_dir):
        os.mkdir(down_dir)
        print("图片储存在"+down_dir+".")
    # get_img_url(down_dir)
    for page in range(2,3000):
        url="https://www.doutula.com/photo/list/?page="+str(page)
        t=threading.Thread(target=get_img_url,args=(down_dir,url))
        t.start()
        t.join()
        print("第 %s 页正在写入..\n" %page)
        time.sleep(3)
        # get_img_url(down_dir,url)
if __name__ == "__main__":
    main()