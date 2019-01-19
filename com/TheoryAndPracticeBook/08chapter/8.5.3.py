# -*- coding: utf-8 -*-
# !/usr/bin/python
from __future__ import division;
import nltk,re,pprint;
from urllib.request import urlopen;
from nltk.book import *
from collections import Counter;

from nltk.corpus import PlaintextCorpusReader;
#nltk载入自己的中文语料库
# corpus_root = r"/Users/xianglingchuan/Documents/work/pythonWork/learnProject/resource/dict";
# file_pattern = r".*";
# wordlists = PlaintextCorpusReader(corpus_root, file_pattern);
# print (wordlists.fileids());
#print (len(wordlists.words("dqdg.txt")));

#大秦帝国语料操作
file = r"/Users/xianglingchuan/Documents/work/pythonWork/learnProject/resource/dict/dqdg.txt";
with open(file, "r+") as f:
    str = f.read();
    #print (str);
    print ("总的用词量:", (len(set(str))));
    #print (len(str));
    print ("词出现的频次: ", len(str)/(len(set(str)))  );

    print ("'秦'字出现的总次数: ", str.count("秦"));
    print("'大秦'字出现的总次数: ", str.count("大秦"));
    print("'国'字出现的总次数: ", str.count("国"));

    #整个词汇累积分布情况
    # fdist = FreqDist(str);
    # fdist.plot();

    #高频率的100个词
    print ("=== 高频率的100个词 ===");
    print (sorted(set(str[:100])));
    # fdist = FreqDist(str);
    # fdist.plot(20, cumulative=True);

    print("=== 查看所有词的使用频次数 ===");
    V = Counter(str);
    print (V);

    print("=== 查询词频在[0-100]的词有多少 ===");
    print(len([w for w in V.values() if w<100]));

    print("=== 查询词频在[100-1000]的词有多少 ===");
    print(len([w for w in V.values() if w>100 and w < 1000]));

    print("=== 查询词频在[5000]以上的词有多少 ===");
    print(len([w for w in V.values() if w > 5000]));











#查看第一部总共有多大的用字量，即不重复词和符合的尺寸


