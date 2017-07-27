import urllib.request
import urllib.error


def download_html(url):
	#下载网页源码
	print('downloading:'+url)
	headers = create_header()
	try:
		request = urllib.request.Request(url,headers = headers)
		response = urllib.request.urlopen(url)
	except urllib.error.HTTPError as e:
		print('download failed:',e.reason)
		html = None
	else:
		print("download finished!")
		html = response.read()
	print(request.get_header('User-agent'))
	return str(html)

def create_header():
	#创建网络报头
	
	#创建User_Agent
	user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063"
	
	#创建cookies（等待后续添加）
	
	#创建Headers
	headers = {"User-Agent":user_agent}
	return headers