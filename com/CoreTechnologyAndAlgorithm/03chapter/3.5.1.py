# -*- coding: utf-8 -*-
# !/usr/bin/python
import jieba;

sent = "中文分词是文本处理不可或缺的一步！";
sent = "向铃川元宵节你准备去那里玩？";

seg_list = jieba.cut(sent, cut_all=True);
print("全模式:", '/'.join(seg_list));

seg_list = jieba.cut(sent, cut_all=False);
print("精确模式:", '/'.join(seg_list));

seg_list = jieba.cut(sent);
print("默认模式:", '/'.join(seg_list));

seg_list = jieba.cut_for_search(sent);
print("搜索引擎模式:", '/'.join(seg_list));

