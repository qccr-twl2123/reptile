#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# 将正则表达式编译成pattern
pattern = re.compile(r'\d+')

result = re.finditer(pattern, '<span>阅读：<em>3816</em></span><span>回复：<em>9</em></span>')
print type(result)

for str1 in result:
    print str1.group()
