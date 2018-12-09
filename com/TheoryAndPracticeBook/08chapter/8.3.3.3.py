# -*- coding: utf-8 -*-
# !/usr/bin/python

import nltk;
#加载NLTK book模块
from nltk.book import *;
from nltk import bigrams;
from collections import Counter;

print("== 词语搭配和双连词 ==");
b = bigrams("This is a test");
print (Counter(b))








