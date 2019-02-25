#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import json
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class HtmlParser(object):
    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return None
        soup = BeautifulSoup(html_cont, 'lxml')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        return new_urls

    def _get_new_data(self, page_url, soup):
        girl_list = list()
        for girl in soup.find_all(class_="J_item J_toUrl item item-a"):
            girl_dict = dict()
            girl_dict['summary'] = girl.find('h3').text
            girl_dict['join_time'] = girl.find('p').text
            girl_dict['img_url'] = girl.find('img').get('data-src')
            girl_dict['detail_url'] = girl.find('a').get('href')
            girl_list.append(girl_dict)

        print json.dumps(girl_list, ensure_ascii=False, encoding='UTF-8')
        with open('girl.json', 'wb') as fp:
            json.dump(girl_list, fp, indent=4, ensure_ascii=False, encoding='UTF-8')
        return girl_list

    def get_detail(self, girl_dict, url):
        res = requests.get(url)
        res.encoding = 'gb18030'
        soup = BeautifulSoup(res.text, 'lxml')
        cont = soup.find({'div':{'id':'view-bd'}})
        girl_dict['popular'] = soup