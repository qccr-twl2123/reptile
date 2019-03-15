#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# 将正则表达式编译成pattern
pattern = re.compile(r'\d+')

# 使用match匹配字符串, 无匹配则返回none
result1 = re.findall(pattern, '<span>阅读：<em>3816</em></span><span>回复：<em>9</em></span>')
result2 = re.findall(pattern, 'eqewq1w928abc')

print result1
#
# if result1:
#     print result1.group()
# else:
#     print '匹配失败1'

urls = []
for i in range(10, 200):
    # print i
    urls.append("https://www.19lou.com/r/1/19lnsxq-" + str(i) + ".html")
    print "https://www.19lou.com/r/1/19lnsxq-" + str(i) + ".html"
    with open("urls", "w") as fp:
        fp.write(str(urls))
