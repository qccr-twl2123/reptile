#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

proxies = {
    'http': 'http://0.10.10.1:8888',
    'https': 'http://0.10.10.1:8888',
}

requests.get('http://example.org', proxies = proxies)