#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

with open('test.text', 'r') as fp:
    print json.load(fp)