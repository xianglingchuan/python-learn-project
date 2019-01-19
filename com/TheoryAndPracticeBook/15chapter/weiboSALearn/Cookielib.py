# -*- coding: utf-8 -*-
# !/usr/bin/python

from urllib import request;
from http.cookiejar import CookieJar;

cookie = CookieJar();
cookie_support = request.HTTPCookieProcessor(cookie);
opener = request.build_opener(cookie_support);
opener.open("http://www.baidu.com");
for item in cookie:
    print(item.name, ":", item.value);


