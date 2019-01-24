#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# 将正则表达式编译成pattern
pattern = re.compile(r'\d+')

result = re.finditer(pattern, 'A1B7D9')

for str1 in result:
    print str1.group()
