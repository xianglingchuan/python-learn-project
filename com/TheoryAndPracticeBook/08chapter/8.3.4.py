# -*- coding: utf-8 -*-
# !/usr/bin/python

import nltk;
#加载NLTK book模块
from nltk.book import *;
#text1;


from nltk.tokenize.stanford_segmenter import  StanfordSegmenter
'''
path_to_jar: 用来定位jar包,本程序分词依赖stanford-segmenter.jar(其它所有Stanford NLP接口都有path_to_jar参数)
path_to_slf4j: 用来定位slf4j-api.jar，作用于分词
path_to_sihan_corpora_dict: 设定为stanford-segmenter-2015-12-09.zip解压后目录中的data目录,data目录下有两个可用模型pkg.gz
和ctb.gz,需要注意的是，使用Stanford-Sementer进行中文分词后，其返回结果并不是list,而是一个字符中，各个汉语词江在其中被空格分隔开.

'''
segmenter = StanfordSegmenter(
    path_to_jar=r"目录/stanford-segmenter.jar",
    path_to_slf4j=r"slf4j-api.jar",
    path_to_sihan_corpora_dict=r"jar/data",
    path_to_model=r"data/pku.gz",
    path_to_dict=r"data/dict-chris6.ser.gz",
);
str = "我在博客园开了一个博客,我的博客名叫简单生活,写了一些关于服务端处理文章。";



'''
这个等相关的jar包下载完成后进行处理......
'''






