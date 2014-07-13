#! /usr/bin/python
#-*- coding = utf-8 -*-
import redis
print redis.__file__
r = redis.Redis(host = '127.0.0.1', port=6379, db =1)

info = r.info()
for key in info:
	print "%s %s" %(key , info[key])
	
