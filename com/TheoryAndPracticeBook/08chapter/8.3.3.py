# -*- coding: utf-8 -*-
# !/usr/bin/python

import nltk;
#加载NLTK book模块
from nltk.book import *;
#text1;

print("============= 使用函数concordance搜索指定内容 ===============");
text1.concordance("American");

print("============= 使用函数similar查找相似上下文 ===============");
text1.similar("very");

print("============= 使用函数common_contexts共用多个词汇的上下文 ===============");
text1.common_contexts(['a', 'very']);

print("============= 使用函数dispersion_plot离散图表示词汇分布情况 ===============");
text1.dispersion_plot(["The", "Moby", "Dick", "Maerica"]);

print("============= 函数len()计数词汇 =============");
len(text1);
