#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import json

r = requests.get('http://tech.qq.com/biznext/zlda.htm')
# print r.text

soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')

article_list = []
for article in soup.find(class_='fl listrow').find_all('a'):
    print article
    print article.get('href')
    print article.find('img').get('src')
    print article.find('p').text
    article_list.append(
        {'title': article.find('p').text.encode('utf-8'), 'link': article.get('href'), 'img': article.find('img').get('src')})

with open('demo.json', 'wb') as fp:
    json.dump(article_list, fp, indent=4, ensure_ascii=False)

with open('demo.json', 'r') as fp:
    print '-----------'
    print json.load(fp)
