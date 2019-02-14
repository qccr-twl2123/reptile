#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

str1 = [{'user_name': 'mark', 'age': 12}, (2, 4), 1]
json_str = json.dumps(str1, ensure_ascii=False)
print json_str

with open('test.text', 'w') as fp:
    json.dump(str1, fp=fp, ensure_ascii=False)
