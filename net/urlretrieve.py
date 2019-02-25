#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
from lxml import etree
import requests
# 解决中文乱码关键代码
import sys
reload(sys)
sys.setdefaultencoding("gb18030")

def schedule(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        return per
    print '当前下载进度 %d ' % per


if __name__ == '__main__':
    r = requests.get("https://www.19lou.com/r/1/19lnsxq.html")
    r.encoding = 'gb18030'
    html = etree.HTML(r.text, parser=etree.HTMLParser(encoding='gb18030'))
    # div_pics = html.xpath('.//*[@class="pics"]')
    div_elements = html.xpath('.//*[@class="J_item J_toUrl item item-a"]')
    i = 0
    for div_element in div_elements:
        title = div_element.xpath('./div[@class="item-hd"]/h3/text()')
        detail_url = div_element.xpath('./@data-url')
        pick_up_time = div_element.xpath('./div[@class="item-hd"]/p/text()')
        view_count = div_element.xpath('./div[class="item-ft"]/p/span/em/text()')
        print view_count
        print pick_up_time[0].encode('utf-8').split(" ")[0]
        print detail_url
        print title[0].encode('utf-8')

        download_url = div_element.xpath('./div[@class="item-bd"]/div[@class="pics"]/img/@data-src')[0]  # 先找到所有的img
        print download_url
        urllib.urlretrieve(download_url, '/Users/mark1xie/img/test/img' + str(i) + '.jpg', schedule)
        i += 1
