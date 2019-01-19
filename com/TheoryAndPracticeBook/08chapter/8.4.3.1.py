# -*- coding: utf-8 -*-
# !/usr/bin/python
from __future__ import division;
import nltk,re,pprint;
from urllib.request import urlopen;

print ("********* 网络和聊天文本 *********");
from nltk.corpus import webtext;

print ("=== 获取网络聊天文本 ===");
for filed in webtext.fileids():
    print (filed);

print ("=== 查看网络聊天文本信息 ===");
for filed in webtext.fileids():
    print (filed, len(webtext.words(filed)), len(webtext.raw(filed)),
           len(webtext.sents(filed)), webtext.encoding(filed));

print ("=== 即时消息聊天会话语料库 ===");
from nltk.corpus import nps_chat;
chatroom = nps_chat.posts("10-19-20s_706posts.xml");
print (chatroom);
print (len(chatroom));
print (chatroom[123]);

