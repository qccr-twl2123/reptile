#!/usr/bin/python
import urllib
import urllib2

url = 'http://dev.api.kkd.51kirin.com/api/bg/sys/user/login'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
refere = 'http://dev.bg.kkd.51kirin.com/'
post_data = {'username': 'admin', 'password': '123456'}
headers = {'User-Agent': user_agent, 'Refere': refere}
data = urllib.urlencode(post_data)
print data
req = urllib2.Request(url, data, headers)
res = urllib2.urlopen(req)
html = res.read()
print html