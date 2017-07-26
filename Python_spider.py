from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def download(url):
	#下载网页源码
	print('downloading:',url)
	try:
		html = urlopen(url).read()
	except HTTPError as e:
		print('download error:',e.reason)
		html = None
	else:
		print('download finished!')
	return html
	

url = "https://tieba.baidu.com/f?kw=%CE%B1%C4%EF&fr=ala0&tpl=5"
# 伪娘吧起始url
content = str(download(url))
tiezilist = re.findall(r'href="/p/[0-9]+"',content)
urllist = []
filename = 0

for tiezi in tiezilist:
        url = "http://tieba.baidu.com"+tiezi.split("\"")[1]
        urllist.append(url)

for url in urllist:
        contend = str(download(url))
        file = open('1.txt','w')
        file.write(contend)
        file.close()
        tupiandizhi = re.findall(r'https://imgsa.baidu.com/forum/w%3D580/sign=[a-z0-9]+/[a-z0-9]+.jpg',contend)
        for tupian in tupiandizhi:
                urlretrieve(tupian,'img/'+str(filename)+'.jpg')
                filename += 1
