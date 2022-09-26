#爬取音频文件
import requests
import json
import jsonpath
index = 1
for i in range(1,26):
	jsonUrl = '' #目标网址
	header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}#设置请求头
	response = requests.get(jsonUrl,headers = header)
	response.encoding = 'utf-8'
	html = response.text
	html = json.loads(html)
	m4a = jsonpath.jsonpath(html,'$..src')
	count = (index-1)*30+1
	index = index+1
	for i in m4a:
		root = ''
		path = i.split('/')[-1]
		with open(root+path,'wb') as f:
			r = requests.get(i)
			f.write(r.content)
			count = count + 1