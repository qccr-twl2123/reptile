#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2

# proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8888'})
# opener = urllib2.build_opener([proxy, ])
# urllib2.install_opener(opener)
# res = urllib2.urlopen('http://www.baidu.com')
# print res.read()

lists =[1,2,8]
assert len(lists) >=5,'列表元素个数小于5'
