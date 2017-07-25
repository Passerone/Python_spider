from urllib.request import urlopen
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
for tiezi in tiezilist:
        url = "http://www.baidu.com"+tiezi.split("\"")[1]
        print(url)
