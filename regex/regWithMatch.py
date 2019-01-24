#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# 将正则表达式编译成pattern
pattern = re.compile(r'\d+')

# 使用match匹配字符串, 从字符串起始位置开始匹配字符串, 无匹配则返回none
result1 = re.match(pattern,  '1928abc')
if result1:
    print result1.group()
else:
    print '匹配失败1'

result2 = re.match(pattern, 'anndas9889')

if result2:
    print result2.group()
else:
    print '匹配失败2'
