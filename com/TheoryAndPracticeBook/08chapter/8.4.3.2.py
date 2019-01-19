# -*- coding: utf-8 -*-
# !/usr/bin/python
from __future__ import division;
import nltk,re,pprint;
from urllib.request import urlopen;

print ("********* 布朗语料库 *********");

print ("=== 查看语料信息 ===");
from nltk.corpus import brown;
print (brown.categories());

print ("=== 比较文本中情态动语的用法 ===");
new_texts = brown.words(categories='news');
fdist = nltk.FreqDist([w.lower() for w in new_texts]);
modals = ['can', 'could', 'may', 'might', 'must', 'will'];
for m in modals:
    print (m + ":", fdist[m]);

print ("=== NLTK 条件概率分布函数 ===");
cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre));
genres = ["news", "religion", "hobbies", "science_fiction", "romance", "humor"];
modals = ['can', 'could', 'may', 'might', 'must', 'will'];
cfd.tabulate(condition=genres, samples=modals);

