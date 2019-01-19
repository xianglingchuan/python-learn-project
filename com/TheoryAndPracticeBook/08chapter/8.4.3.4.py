# -*- coding: utf-8 -*-
# !/usr/bin/python
from __future__ import division;
import nltk,re,pprint;
from urllib.request import urlopen;

print ("********* 就职演说语料库 *********");
from nltk.corpus import inaugural;
print (len(inaugural.fileids()));
print (inaugural.fileids());

print ("=== 查看演说语料的年份 ===");
print ([fileid[:4] for fileid in inaugural.fileids()]);

print ("=== 条件概率分布 ===");
cfd = nltk.ConditionalFreqDist(
    (target,fileid[:4]) for fileid in inaugural.fileids()
                        for w in inaugural.words(fileid)
                        for target in ['america', 'citizen'] if w.lower().startswith(target));
cfd.plot();
