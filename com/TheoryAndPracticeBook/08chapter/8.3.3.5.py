# -*- coding: utf-8 -*-
# !/usr/bin/python

import nltk;
#加载NLTK book模块
from nltk.book import *;
from nltk import bigrams;
from collections import Counter;

print("== 词汇比较运算(s代表字符串) ==");

s = "this is a test";

print("== 测试是否以t开头 ==");
print (s.startswith("t"));

print("== 测试是否以t结尾 ==");
print (s.endswith("t"));

print("== 测试s是否包含t ==");
print ("t" in s);

print("== 测试s所有字符串是否都小写字母 ==");
print (s.islower());

print("== 测试s所有字符串是否都大写字母 ==");
print (s.isupper());

print("== 测试s所有字符串是否都是字母 ==");
print(s.isalpha());

print("== 测试s所有字符串是否都是字母或数字 ==");
print(s.isalnum());

print("== 测试s所有字符串是否都是数字 ==");
print(s.isdigit());

print("== 测试s所有词首字母都是大写 ==");
print(s.istitle);


