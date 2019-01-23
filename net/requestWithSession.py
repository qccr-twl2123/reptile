#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

loginUrl = 'http://dev.api.kkd.51kirin.com/api/bg/sys/user/login'
s = requests.Session()
# 首先作为游客访问登陆页面, 服务器会先分配一个cookie
r = s.get(loginUrl, allow_redirects=True)
# 想登陆链接发送post请求， 游客权限转为会员权限
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
refere = 'http://dev.bg.kkd.51kirin.com/'
headers = {'User-Agent': user_agent, 'Refere': refere}
url = 'http://dev.api.kkd.51kirin.com/api/bg/sys/user/login'
post_data = {'username': 'admin', 'password': '123456'}

res = s.post(loginUrl, post_data, headers,allow_redirects=True)
print res.content


