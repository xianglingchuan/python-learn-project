# -*- coding: utf-8 -*-
# !/usr/bin/python

import re;
string = "文本最重要的来源无疑是网络。我们要把网络中的文本获取行成一个文本数据库。利用一个爬虫抓取到网络中的信息。" \
         "爬取的策略有广度爬取和深度爬取。根据用户的需求，爬虫可以有主要爬虫和通用爬虫之分。";
regex = "爬虫";
pString = string.split("。");
for line in pString:
    if re.search(regex, line) is not None:
        print(line);

print("\n\r");
print("====================================");
print("匹配任意一个字符(.匹配任意一个字符) ");
print("====================================");
regex = "爬.";
pString = string.split("。");
for line in pString:
    if re.search(regex, line) is not None:
        print(line);

regex = ".用户";
pString = string.split("。");
for line in pString:
    if re.search(regex, line) is not None:
        print(line);



print("\n\r");
print("====================================");
print("匹配起始和结尾字符串(^匹配开始的字符串$匹配结尾的字符串)");
print("====================================");
regex = "^文本";
regex = "^爬";
pString = string.split("。");
for line in pString:
    if re.search(regex, line) is not None:
        print(line);

regex = "数据库$";
pString = string.split("。");
for line in pString:
    if re.search(regex, line) is not None:
        print(line);

print("\n\r");
print("====================================");
print("匹配多个字符串([]匹配多个字符串)");
print("====================================");
string = ['[重要的]今年第七号台风23号登陆广东东部沿海地区','上海发布车库销售监管通知：违规者暂停网签资格',
          '[紧要的]中国对印度连发强硬信息，印度急切需要结束对峙'];

regex = "^\[[重紧]..\]"
regex = "^\[.[要].\]";
regex = "^\[..[的]\]"; #一个.表示一个匹配字符
for line in string:
    if re.search(regex, line) is not None:
        print(line);
    else:
        print("not match.");


