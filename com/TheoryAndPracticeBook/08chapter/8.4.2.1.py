# -*- coding: utf-8 -*-
# !/usr/bin/python
from __future__ import division;
import nltk,re,pprint;
from urllib.request import urlopen;

print ("=== 处理RSS订阅 ===");
import feedparser;
url = "http://rss.sina.com.cn/news/marquee/ddt.xml";
llog = feedparser.parse(url);
print (llog);


'''
相关正则知识
1、\d 匹配一个数字
2、\w 匹配一个字母或者数字
   * 任意字符(包括0个)
   + 至少一个字符
   ？0个或1个字符
   {n} n个字符串
   {n,m} n~m个字符
   \s 匹配一个空格
   \s+ 至少有一个空格
   \d3,8 表示3~8个数字,例如:"1234567 "
   [0-9a-zA-Z_] 匹配一个数字、字母或者下划线
   [0-9a-zA-Z_]+, 匹配至少一个一个数字、字母或者下划线
   [0-9a-zA-Z_]* 匹配0个或1个数字、字母或者下划线
   [0-9a-zA-Z_]{0,19}更精确地限制了变量的长度1~20个字符
   A|B 可以匹配A或B
   ^ 表示行的开头,\d表示必须以数字开头
   - 表示行的结束,\d表示必须以数字结束




'''

