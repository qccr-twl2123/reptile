#!/usr/bin/python
import urllib
import urllib2

try:
    res = urllib2.urlopen("http://www.baidu.com")
    print res.code
except urllib2.HTTPError as e:
    if hasattr(e, 'code'):
        print 'Error Code', e.code
