#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
from lxml import etree
import requests
import json
import csv
# 解决中文乱码关键代码
import sys

reload(sys)
sys.setdefaultencoding("gb18030")


def schedule(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        return per
    print '当前下载进度 %d ' % per


def crawl(url):
    r = requests.get(url)
    r.encoding = 'gb18030'
    html = etree.HTML(r.text, parser=etree.HTMLParser(encoding='gb18030'))
    div_elements = html.xpath('.//*[@class="J_item J_toUrl item item-a"]')
    i = 0
    girl_list = list()
    for div_element in div_elements:
        girl = dict()
        title = div_element.xpath('./div[@class="item-hd"]/h3/text()')
        detail_url = div_element.xpath('./@data-url')
        pick_up_time = div_element.xpath('./div[@class="item-hd"]/p/text()')
        girl['pick_up_time'] = pick_up_time[0].encode('utf-8').split(" ")[0]
        girl['detail_url'] = detail_url[0]
        girl['title'] = title[0].encode('utf-8')
        download_url = div_element.xpath('./div[@class="item-bd"]/div[@class="pics"]/img/@data-src')[0]  # 先找到所有的img
        girl['picture_download_url'] = download_url

        get_detail(girl, detail_url[0])
        girl_list.append(girl)
        urllib.urlretrieve(download_url, '/Users/mark1xie/img/test/img' + str(i) + '.jpg', schedule)
        i += 1
    with open('girl.json', 'w') as fp:
        json.dump(girl_list, fp, indent=4, ensure_ascii=False)


def get_detail(girl, url):
    r = requests.get(url)
    r.encoding = 'gb18030'
    html = etree.HTML(r.text, parser=etree.HTMLParser(encoding='gb18030'))

    div_profile_text = html.xpath('.//div[@class="thread-cont"]/text()')
    print div_profile_text
    girl['profile'] = div_profile_text



if __name__ == '__main__':
    # crawl('https://www.19lou.com/r/1/19lnsxq-3.html')

    headers = dict()
    # headers[''] =
    r = requests.get('https://www.19lou.com/forum-164-thread-9491548519005504-1-1.html')

    r.encoding = 'gb18030'
    html = etree.HTML(r.text, parser=etree.HTMLParser(encoding='gb18030'))

    div_profile_text = html.xpath('.//div[@class="love-blind-info fr"]/p[0]/text()')
    print div_profile_text
