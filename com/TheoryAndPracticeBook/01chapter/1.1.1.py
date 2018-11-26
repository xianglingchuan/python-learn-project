# -*- coding: utf-8 -*-
# !/usr/bin/python

print("===== import与from...import =====");
print("import somemodule 将整个模块导入");

# import sys;
# print("命令行参数为:");
# for i in sys.argv:
#     print (i);
# print ("Python路径为:",sys.path);

from sys import argv,path
print("import somemodule somefunction 从某个模块中导入某个函数");

#print ("Python路径为:",sys.path)
#NameError: name 'sys' is not defined


print("===== 数据库 =====");

print("str 一个由字符组成的不可更改的有序列，在Python3.x里，字符串由Unicode字符组成");

print("bytes 一个由字节组成的不可更改的有序列");

print("list 可以包含多种类型的可改变的有序列");

print("tuple 可以包含多种类型的不可改变的有序列");

print("set/frozenset与数学中集合的概念类似,无序的，每个元素唯一");

print ("dict 或 map 一个可改变的由键值对组成的无序列");

print ("int 精度不限的整数");

print ("float 浮点数，精度与系统相关");

print ("complex 复数");

print ("bool 逻辑值,只有两个值：真、假");