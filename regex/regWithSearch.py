#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# 将正则表达式编译成pattern
pattern = re.compile(r'\d+')

# 使用match匹配字符串, 无匹配则返回none
result1 = re.search(pattern,  'eqewq1w928abc')
result2 = re.findall(pattern,  'eqewq1w928abc')

print result2

if result1:
    print result1.group()
else:
    print '匹配失败1'
