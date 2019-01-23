#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests


# get
# r = requests.get('http://www.baidu.com')
# print r.content
#
# # get with param
# payload = {'Keywords': 'java', 'pageindex': '1'}
# r = requests.get('http://zzk.cnblogs.com/s/blogpost', payload)
# print r.url
# print r.content

# get with headers
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
refere = 'http://dev.bg.kkd.51kirin.com/'
headers = {'User-Agent': user_agent, 'Refere': refere}
url = 'http://dev.api.kkd.51kirin.com/api/bg/sys/user/login'
post_data = {'username': 'admin', 'password': '123456'}
r = requests.post(url, post_data,  headers)
print r.content
for cookie in r.cookies.keys():
    print cookie + ':' + r.cookies.get(cookie)