#!/usr/bin/python
# -*- coding: UTF-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

print os.getcwd()  # 打印出当前工作路径

f = open('stop.text', 'r').read()
print f
wordCloud = WordCloud(background_color="white", width=1000, height=860, margin=2).generate(f)
plt.imshow(wordCloud)
plt.axis("off")
plt.show()

wordCloud.to_file('test.png')
