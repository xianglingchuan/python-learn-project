# -*- coding: utf-8 -*-
# !/usr/bin/python
import  jieba;
print ("=== 全模式 ===");
seg_list = jieba.cut("我来到北京清华大学", cut_all=True);
print ("Full Model:"+"/".join(seg_list));

print ("=== 精确模式 ===");
seg_list = jieba.cut("我来到北京清华大学", cut_all=False);
print ("Default Model:"+"/".join(seg_list));


print ("=== 默认模式(精确模式) ===");
seg_list = jieba.cut("他来到了网易杭研厦");
print ("Default Model:"+"/".join(seg_list));

print ("=== 搜索引擎模式 ===");
seg_list = jieba.cut_for_search("小明毕业于中国科学院计算机所，后在日本东京大学深造")
print ("Default Model:"+"/".join(seg_list));


print ("=== 添加自定义词典 ===");
str = "李小福是创新办主任也是云计算方面的专家";

seg_list = jieba.cut(str, cut_all=False);
print ("未添加自定义词典之前:"+"/".join(seg_list));

jieba.load_userdict("/Users/xianglingchuan/Documents/work/pythonWork/learnProject/resource/jieba/dict.txt");
seg_list = jieba.cut(str, cut_all=False);
print ("添加自定义词典之后:"+"/".join(seg_list));
