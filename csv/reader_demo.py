#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
from collections import namedtuple

with open('demo.csv', 'r') as fp:
    f_csv = csv.reader(fp)
    headers = next(f_csv)
    Row = namedtuple('ROW', headers)
    print headers
    for r in f_csv:
        row = Row(*r)
        print row.name
        print row.age

print '-------'
with open('demo.csv', 'r') as fp:
    f_csv = csv.DictReader(fp)
    for row in f_csv:
        print row.get('name')
