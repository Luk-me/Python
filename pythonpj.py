import requests,xlwt,lxml
from bs4 import BeautifulSoup
url="https://cn.bing.com"

r=requests.get(url,headers={})
r.encoding="utg-8"

def get_page(url):
	r=requests.get(url)
	r.encoding='utf-8'
	return r.text

def get_soup(url):
	html=get_page(url)
	soup=BeautifulSoup(html,'lxml')
	return soup

def down_image(start_url):
	soup=get_soup(start_url)
	list = soup.find('div',attrs={'class':'pinDaoPageImgBox'}).find_all('h3')
	for item in list:
		url_child = 'http://www.7dapei.com/tuku/'+item.find('a').get('href')
		print(url_child)
		dir_name=item.find('a').text
		print(dir_name)
	print(dir_name)


def down_data(url):
	pass

if __name__ == '__main__':
	start_url='http://www.7dapei.com/tuku/'
	down_image(start_url)