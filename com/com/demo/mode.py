# -- coding: utf-8 --
'''
Python的新版本会引入新的功能，但是，实际上这些功能在上一个老版本中就已经存在了。
要“试用”某一新的特性，就可以通过导入__future__模块的某些功能来实现。
'''
from __future__ import division;
from __future__ import unicode_literals;



#1、python中模块和包的概念
'''
模块和包的概念
   如何区分包和普通目录
   包下面有一个__init__.py文件
   注意每层目录必须都存在此目录
'''

#2、python之导入模块
import math;

print "math.pow()====>",math.pow(2,0.5);
print math.pi;

print "\n只导入用到的math模块的某几个函数，而不是所有函数";
from math import pow, sin, log;
print pow(2,10);
print sin(3.14);

print "\n处理不同包内有相同的函数名冲突问题";
import math, logging;
print math.log(10);
print logging.log(10,"something");


print "\n为导入的函数取别名，以访止冲突";
from math import log;
from logging import  log as logger;
print log(10);
print logger(10,"import from logging");


print "\n练习\n";
import os;

dirPath = "/Users/xianglingchuan/Documents/work/pythonWork/learnProject/static/";
#dirPath = "static";
print os.path.isdir(dirPath);
#创建目录
#dirPathNew = "/Users/xianglingchuan/Documents/work/pythonWork/learnProject/static/dirPath/";
#os.mkdir(dirPathNew);
#os.remove(dirPathNew);

fileName = "/Users/xianglingchuan/Documents/work/pythonWork/learnProject/static/file22.txt";
print os.path.isfile(fileName);
#os.mkfifo(fileName);
print ('===============================\n');



#3、python中动态导入模块
print ("try 的作用是捕获错误，并在捕获到指定错误时执行 except 语句。");
try:
    from cStringIO import StringIO;
except ImportError:
    from StringIO import StringIO;

try:
    import json;
except ImportError:
    import simplejson;
print json.dumps({'python':2.7})
print ('===============================\n');


#4、python之使用__future__
print 10/3; #3

print 10/3; #3.x版本是3.33333333333

print "中国人民";
s = "am I an unicode?";
print isinstance(s, unicode);
print "\n\n";
print ('===============================\n');



#5、python之安装第三方模块
'''
内置了许多有用的模块
可以安装第三方模块

Python提供的模块管理工具
   easy_install
   pip(推荐,已内置到Python2.7.9)

使用pip安装第三方模块
   pip install web.py
   然后在工程中导入web即可。


安装easy_install
   sudo easy_install pip   
   
   
如果要查找第三方模块的名字
   https://pypi.python.org
   
??????一直没有安装成功   
'''




















