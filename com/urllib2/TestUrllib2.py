# -*- coding: utf-8 -*-
import urllib2;
import cookielib;

print "\n\n下载网页方法一";
response = urllib2.urlopen('http://www.baidu.com');
print response.getcode();
cont = response.read();
print len(cont);


print "\n\n下载网页方法2";
#创建Request对象
url = "http://www.baidu.com";
request = urllib2.Request(url);
#添加数据
#request.add_data('a','1');
#添加http的header
request.add_header('User-Agent', "Mozilla/5.0")
#发送请求获取结果
response = urllib2.urlopen(request);
print response.getcode();
print len(response.read());


print "\n\n下载网页方法3";
#创建cookie容器
cj = cookielib.CookieJar();
#创建1个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#给urllib2安装opener
urllib2.install_opener(opener)
#使用带有cookie的urllib2访问网页
response = urllib2.urlopen("https://baike.baidu.com/item/Python/407313")
print response.getcode();
print response.read()












