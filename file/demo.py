#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
from lxml import etree
import requests

def schedule(blocknum, blocksize, totlesize):
    '''
    :param blocknum: 已下载数据
    :param blocksize:
    :param totlesize:
    :return:
    '''
    per = 100 * blocknum * blocksize / totlesize
    if per > 100:
        per = 100

    print 'current down process %s' % per

r = requests.get('http://www.ivsky.com')
