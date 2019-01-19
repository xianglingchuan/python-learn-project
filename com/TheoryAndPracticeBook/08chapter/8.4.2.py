# -*- coding: utf-8 -*-
# !/usr/bin/python
from __future__ import division;
import nltk,re,pprint;
from urllib.request import urlopen;

url = 'http://www.gutenberg.org/files/24272/24272-0.txt';
raw = urlopen(url).read();
raw = raw.decode('utf-8');
print (len(raw));
#print (raw);
print (raw[2000:2500]);

print ("=== 在线获取处理HTML文本(红楼梦) ===");
url = "http://www.gutenberg.org/cache/epub/24264/pg24264-images.html";
html = urlopen(url).read();
html = html.decode('utf-8');
print (html[5000:5500]);

