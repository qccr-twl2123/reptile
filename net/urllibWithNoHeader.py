#!/usr/bin/python
import urllib
import urllib2

url = 'http://dev.api.kkd.51kirin.com/api/bg/sys/user/login'
post_data = {'username': 'admin', 'password': '123456'}
data = urllib.urlencode(post_data)
req = urllib2.Request(url, data)
res = urllib2.urlopen(req)
print res.read()

