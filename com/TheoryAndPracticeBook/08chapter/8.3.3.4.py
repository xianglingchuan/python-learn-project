# -*- coding: utf-8 -*-
# !/usr/bin/python

import nltk;
#加载NLTK book模块
from nltk.book import *;
from nltk import bigrams;
from collections import Counter;

print("== NLTK频率分布类中定义的函数 ==");

#fdist1 = FreqDist(Samples); 创建包含给定样本的频率分布
fdist1 = FreqDist(text1);

#增加样本
print("== 增加样本 ==");
samples2 = "this is a test";
#fdist1.inc(samples2);
# #AttributeError: 'FreqDist' object has no attribute 'inc'

print("== 计算给定样本出现的次数 ==");
print (fdist1["the"]);

print("== 给定样本的频率 ==");
print (fdist1.freq("the"));

print("== 样本总数 ==");
print (fdist1.N());

print("== 以频率递减顺序排序样本链表 ==");
#print (fdist1.keys()); #无该方法

print("== 以频率递减顺序遍历样本 ==");
for samples2 in fdist1:
    print (samples2);

print("== 数值最大样本 ==");
print (fdist1.max());


print("== 绘制频率分布表 ==");
print (fdist1.tabulate());

print("== 绘制频率分布图 ==");
print (fdist1.plot());

print("== 绘制累积频率分布图 ==");
#print (fdist1.plot(cumulative=True));

#fdist1 < fdist2; 测试样本在fidst1中出现的频率是否小于fidst2












