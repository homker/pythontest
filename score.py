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

def GetPage():
    url = 'http://172.16.47.252:80/mis_o/login.php'
    mainurl = 'http://172.16.47.252:80/mis_o/query.php'
    while True :
        StudID = raw_input('please input your studentID:')
        if type(eval(StudID)) is int:
                break
        break
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
    
    user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'
    headers = { 
        'User-Agent' : user_agent,
        'Referer' : 'http://jwc.ecjtu.jx.cn/mis_o/main.php' 
    }
    req = urllib2.Request(url, headers = headers, data = logindata)
    response = opener.open(req).read()
    print 'main page lode success'
    for item in cookie:
        print 'cookie name:'+item.name
        print 'cookie value:'+item.value
        print 'loding...'
    req = urllib2.Request(mainurl, headers = headers, data = querydata)
    result = opener.open(req)
    upage = result.read().decode('gbk').encode('utf-8')
    parttern = '<td>(.*?)<\/td>'
    match = re.findall(parttern, upage, re.S)
    del match[0]
    for i in range(0,len(match),9):
        print '课程:'+match[i+3].decode('utf-8').encode('utf-8')
        print '性质:'+match[i+4]
        print '学分:'+match[i+5]
        print '成绩:'+match[i+6]
        if match[i+7] != ' ':
            print '补考1：'+match[i+7]
            if match[i+8] != ' ':
                print '补考2：'+match[i+8]
        print '======================='


    
GetPage()
