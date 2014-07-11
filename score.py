#!/usr/bin/python
#-*-coding:utf-8-*-
import urllib2
import urllib
import re
import thread
import time

def GetPage(page):
	#url = raw_input('please input you url')
	StudID = raw_input('please input your studentID:')
		
	url = 'http://jwc.ecjtu.jx.cn/mis_o/query.php'
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5 ; Windows NT)'
	headers = { 
		'User-Agent' : user_agent
		'Referer':url 
	}
	req = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(req).reade()
	upage = response.decode("utf-8")
	parttern = '<p>'
