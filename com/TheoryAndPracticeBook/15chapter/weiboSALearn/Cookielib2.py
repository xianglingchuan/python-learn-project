# -*- coding: utf-8 -*-
# !/usr/bin/python

from urllib import request;
from http.cookiejar import CookieJar;

# cookie = CookieJar();
# cookie_support = request.HTTPCookieProcessor(cookie);
# opener = request.build_opener(cookie_support);
# opener.open("http://www.baidu.com");
# for item in cookie:
#     print(item.name, ":", item.value);

#无法正常运行
# cookie = getCookie();
# with open('proxy.txt', 'w') as f:
#     for page in range(1, 101):
#         if page%50==0: #每50页更新cookie
#             cookie = getCookie();
#         url = "http://www.test.com/nn/%s" %page;
#         cookie_support = request.HTTPCookieProcessor(cookie);
#         opener = request.build_opener(cookie_support);
#         request.install_opener(opener);
#
#         req = request.Request(url, headers=dict(headers));
#         content = request.urlopen(req);
#         soup = BeautifulSoup(content, "lxml");
#         trs = soup.find("table", id="ip_list").findAll(tr);
#
#         for tr in trs[1:]:
#             tds = tr.findAll('td');
#             ip = tds[1].text.strip();
#             prot = tds[2].text.strip();
#             protocol = tds[5].text.strip();
#             f.write("%s://%s:%s\n" % (protocol, ip, prot));
