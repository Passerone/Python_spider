from url_download import download_html
from urllib.request import urlretrieve
from setting import Settings
import re


settings = Settings()

content = download_html(settings.url)
tiezilist = re.findall(settings.zzpp1,content)
urllist = []
filename = 0

for tiezi in tiezilist:
        url = "http://tieba.baidu.com"+tiezi.split("\"")[1]
        urllist.append(url)

for url in urllist:
        contend = download_html(url)
        tupiandizhi = re.findall(settings.zzpp2,contend)
        for tupian in tupiandizhi:
                urlretrieve(tupian,'img/'+str(filename)+'.jpg')
                filename += 1
