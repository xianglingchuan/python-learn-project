# -*- coding: utf-8 -*-
# !/usr/bin/python
from __future__ import division;
import nltk,re,pprint;
from urllib.request import urlopen;

print ("********* 路透社语料为 *********");

from nltk.corpus import reuters;
print (reuters.fileids()[:50]);

print ("=== 查看语料包括前100个类别");
#print(reuters.categories(){[0:100{]});
print(reuters.categories()[0:100]);

print ("=== 查看某个编号的语料下类别尺寸");
print (reuters.categories("training/9865"));

print ("=== 查看某几个联合编号下语料的类别尺寸");
print (reuters.categories(["training/9865", "training/9880"]));

print ("=== 查看哪些编号的文件属于指定的类别");
print (reuters.fileids('barley'));

