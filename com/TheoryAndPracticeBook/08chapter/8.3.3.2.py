# -*- coding: utf-8 -*-
# !/usr/bin/python

import nltk;
#加载NLTK book模块
from nltk.book import *;


print("== 细粒度查询 ==");
V = set(text1);
longwords = [w for w in V if len(w) > 15];
print (sorted(longwords));

print("== 查询文本中单词长度大于10并且出现次数超过10次的 ==");
fdist1 = FreqDist(text1);
print ([w for w in set(text1) if len(w)>10 and fdist1[w] > 10]);

print("== 词语搭配和双连词 ==");


