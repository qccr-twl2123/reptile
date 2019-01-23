#!/usr/bin/python
import urllib
import urllib2

req = urllib2.Request('http://www.baidu.com')
res = urllib2.urlopen(req, timeout=2)
print res.read()