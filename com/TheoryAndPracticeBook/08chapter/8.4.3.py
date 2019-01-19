# -*- coding: utf-8 -*-
# !/usr/bin/python
from __future__ import division;
import nltk,re,pprint;
from urllib.request import urlopen;

print ("********* 古腾堡语料库 *********");

#1、直接获取语料库的所有文本, nltk.corpus.gutenberg.fileids()
print (nltk.corpus.gutenberg.fileids());

#2、导入包获取语料库的所有文本
print ("=== 导入包获取语料库的所有文本 ===");
from nltk.corpus import gutenberg;
print (gutenberg.fileids());

#3、查找某个文本
print ("=== 查找某个文本 ===");
persuasion = nltk.corpus.gutenberg.words("austen-persuasion.txt");
print (persuasion);
print (len(persuasion));
print (persuasion[:200]);





