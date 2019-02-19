#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers)
        if r.status_code == 200:
            r.encoding = 'utf=8'
            return r.text
        return None
