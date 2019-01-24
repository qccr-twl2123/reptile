#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# 将正则表达式编译成pattern
pattern = re.compile(r'\d+')

result1 = re.split(pattern, 'A1B2')
print result1