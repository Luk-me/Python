import requests as re
from lxml import etree
import os,pprint,time
down_dir = os.path.join(os.getcwd(), 'beautifulgirls/')
#all_down_url={}# 格式：{性感撩人美女私房大胆诱惑图片：[下载地址1，下载地址2]}
jpg_title=[]
jpg_url=[]
def get_url_one(url):
    all_url_one=[]
    req=re.get(url)
      
    for i in range(1,2):#共24页
        
        xp='/html/body/div[4]/div/div[3]/div[1]/div[1]/div[2]/div/div/ul/li['+str(i)+']/a'
        ele=etree.HTML(req.text).xpath(xp)
        #print(ele[0].attrib['href'])
        all_url_one.append(ele[0].attrib['href'])
    return all_url_one#列表
   
def get_url_two_page(ls):#传入一个列表
    for i in range(len(ls)):
    
        #/html/body/div[4]/div/div[2]/div/div[1]/div[1]/h1  #标题
    
        req=re.get(ls[i])
        xp_titie='/html/body/div[4]/div/div[2]/div/div[1]/div[1]/h1'
        ele_title=etree.HTML(req.text).xpath(xp_titie)
        title=str(ele_title[0].text)
        global jpg_title
        jpg_title.append(title)       
        
        xp_page='/html/body/div[4]/div/div[2]/div/div[1]/div[1]/em'  #/html/body/div[4]/div/div[2]/div/div[1]/div[1]/em
        ele_page=etree.HTML(req.text).xpath(xp_page)#9
        #print(str(ele_page[0].text))     
        temp=[]
        for x in range(1,int(ele_page[0].text)+1):#1-9
            temp.append(ls[i][:(len(ls[i])-5)]+'_'+str(x)+'.html')
        ls[i]=temp    
    return ls
    #print(ls)
    
def get_url_two(url):#获取图片地址***.jpg
    
    req=re.get(url)
    xp='//*[@id="pic-meinv"]/a/img'
    ele=etree.HTML(req.text).xpath(xp)
    
    return ele[0].attrib['url']



def main():
    for i in range(1,6):
        website='http://www.win4000.com/meinvtag4_%s.html'% str(i)    
    
        url=get_url_one(website)
        #print(url)
        allurl=get_url_two_page(url)
        
        #pprint.pprint(allurl)
        for u1 in allurl:
            temp=[]
            for u2 in u1:
                print(u2)
                temp.append(get_url_two(u2))
                time.sleep(1)
        
        #print(temp)
            jpg_url.append(temp)
        #all_down_url=dict(zip(jpg_title,jpg_url))
        #pprint.pprint(all_down_url)
   
    down_and_save()
    



def down_and_save():#命名规则 字典key+编号.jpg
    for i in range(len(jpg_url)):
        for num in range(1,len(jpg_url[i])+1):
            file_name=jpg_title[i]+str(num)+'.jpg'
            jpg=jpg_url[i][num-1]
            print(file_name,jpg)
            res=re.get(jpg)
            with open(down_dir+file_name,'wb') as f:
                for chunk in res.iter_content(100000):
                    f.write(chunk)
                


if __name__=='__main__':
    if not os.path.exists(down_dir):
        os.mkdir(down_dir)
    print('图片保存在:'+down_dir)
    
    main()