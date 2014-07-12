#!/usr/bin/python
#-*-coding:utf-8-*-
import urllib2
import urllib
import cookielib
import re
import thread
import time

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
COUNT = 0

def GetPage(StudID):
    url = 'http://172.16.47.252:80/mis_o/login.php'
    mainurl = 'http://172.16.47.252:80/mis_o/query.php'
    term = 2013.2
    print 'loding...'
    logindata = urllib.urlencode({
        'user':'jwc',
        'pass':'jwc'
    })
    querydata = urllib.urlencode({
        'StuID':StudID,
        'Term':term
        })
    urlGet(url,logindata)
    try:
    	result = urlGet(mainurl,querydata)
    except:
    	print 'fail to connect the server'
    content = result.decode('gbk').encode('utf-8')
    return content
 
def show(content):
	parttern = '<td>(.*?)</td>'
	match = re.findall(parttern, content, re.S)
	del match[0]
	for i in range(0,len(match),9):
		partternNext = '<font color=red>(.*?)</font>'
		matchs = re.findall(partternNext, match[i+6], re.S)
		#print len 	 (matchs)
		if len(matchs) != 0:
			match[i+6] = matchs[0]
		if match[i+6] < '60' or match[i+6] == '不及格' or match[i+6] == '不合格':
			print '姓名：' + match[i+2] 
			print '课程:'+match[i+3].decode('utf-8').encode('utf-8')
			print '性质:'+match[i+4]
			print '学分:'+match[i+5]
			print '成绩:'+match[i+6]
			global COUNT
			COUNT =COUNT + 1
			if match[i+7] != ' ':
				print '补考1：'+match[i+7]
				if match[i+8] != ' ':
					print '补考2：'+match[i+8]
			print '===================='
def urlGet(url,data):
	user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'
	headers = { 
        'User-Agent' : user_agent,
        'Referer' : 'http://jwc.ecjtu.jx.cn/mis_o/main.php' 
    	}
	req = urllib2.Request(url, headers = headers, data = data)
	result = opener.open(req)
	upage = result.read()
	return upage

def start():
	global COUNT
	studID = ['20122110090224','20130310010221','20132110010616','20120210030110','20132110130227','20132110010311','20132110010417','20130610040122 ','20132110011008','20132110090310','20132110010408']
	for i in range(0, len(studID)):
		print '爬虫%d正在判断成绩' % i
		show(GetPage(studID[i]))
		print '判断完成～！'
	print 'Done!' 
	print '挂科总数：%d' % COUNT
	
start()
