# -*- coding: utf-8 -*-
# !/usr/bin/python

import re;

print("\n\r");
print("====================================");
print("提取文本中的数字");
print("====================================");
strings = ['War of 1821', "There are 5280 feet to a mile",
           "Happy New Year 2016!"];
yearString = [];
for string in strings:
    if re.search('[1-2][0-9]{3}', string):
    #if re.search('[1-2]{1}[0-9]{3}', string):
        yearString.append(string);
    print(yearString);

print("\n\r");
print("====================================");
print("提取所有年份");
print("====================================");
yString = "2016 was a good year, but 2017 will be better!";
years = re.findall('[2]{1}[0-9]{3}', yString);
print(years);
#官方教程地址: docs.python.org/3/tutorial