#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import json

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
headers = {'User-Agent': user_agent}
r = requests.get('http://www.seputu.com', headers=headers)
soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
content = []
for mulu in soup.find_all(class_='mulu'):
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string
        # print h2_title
        list = []
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            print href
            print box_title
            list.append({'href': href, 'box_title': box_title})
        content.append({'title': h2_title, 'content': content})
with open('qiye.json', 'wb') as fp:
    json.dump(content, fp, indent=4)
