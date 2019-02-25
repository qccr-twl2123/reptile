#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.19lou.com/r/1/19lnsxq.html")
res.encoding = 'gb18030'
soup = BeautifulSoup(res.text,'lxml')
print(soup.head.title.text)

item_list = soup.find_all(class_="J_item J_toUrl item item-a")
# print item_list[0]
print item_list[0].find('h3').text