class Settings():
	'''
	初始化爬虫设置
	'''
	def __init__(self):
		#初始url设置
		self.url = "https://tieba.baidu.com/f?kw=%CE%B1%C4%EF&fr=ala0&tpl=5"
		
		#正则匹配式设置
		self.zzpp1 = r'href="/p/[0-9]+"'
		self.zzpp2 = r'https://imgsa.baidu.com/forum/w%3D580/sign=[a-z0-9]+/[a-z0-9]+.jpg'
		