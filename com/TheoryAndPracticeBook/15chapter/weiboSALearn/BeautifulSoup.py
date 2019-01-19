# -*- coding: utf-8 -*-
# !/usr/bin/python
import re;
from urllib import request;
from bs4 import BeautifulSoup;

html = request.urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html,"lxml");
#打印所有图片地址
for pic in bs.find_all('img', {'src':re.compile(".*\.jpg$")}):
    print(pic['src']);





