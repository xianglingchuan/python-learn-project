# -*- coding: utf-8 -*-
# !/usr/bin/python

import nltk;
#加载NLTK book模块
from nltk.book import *;

print("============= 函数len()计数词汇 =============");
print (len(text1));

print("============= 函数表排序 =============");
print (sorted(set(text1)));

print("============= 词汇表大小 =============");
print (len(set(text1)));

print("============= 每个词平均使用的次数 =============");
print (len(text1) / len(set(text1)));

print("============= 特定词在文本中出现的次数 =============");
print (text1.count("smote"));


print("============= 特定词在文本中所占的百分比 =============");
print(100 * text1.count("word") / len(text1));


print("============= NLTK搜索函数FreqDist() =============");
fdist1 = FreqDist(text1);
print (fdist1);
#指定查询某个词的使用频率
print (fdist1['whale']);
#指定常用词累积频率图
fdist1.plot(50, cumulative=True);




