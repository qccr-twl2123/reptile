#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import json


class HtmlParser(object):
    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return None
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        # new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        return new_urls

    def _get_new_data(self, page_url, soup):
        data = list()
        item_list = soup.find_all(class_="J_item J_toUrl item item-a")
        for item in item_list:
            person = dict()
            item_hd = item.find(class_='item-hd')
            person['summary'] = item_hd.find('h3').text
            person['pick_time'] = item_hd.find('p').text
            data.append(person)

        print data
        with open('girl.json', 'wb') as fp:
            json.dump(data, fp, indent=4)
        return data
