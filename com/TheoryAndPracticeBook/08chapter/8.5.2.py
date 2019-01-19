# -*- coding: utf-8 -*-
# !/usr/bin/python
from __future__ import division;
import nltk,re,pprint;
from urllib.request import urlopen;

from nltk.corpus import PlaintextCorpusReader;
#nltk载入自己的中文语料库
corpus_root = r"/Users/xianglingchuan/Documents/work/pythonWork/learnProject/resource/dict";
file_pattern = r".*";
wordlists = PlaintextCorpusReader(corpus_root, file_pattern);
print (wordlists.fileids());

print (len(wordlists.words("dqdg.txt")));



