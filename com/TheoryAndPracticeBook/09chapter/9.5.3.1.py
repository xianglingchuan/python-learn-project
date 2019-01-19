# -*- coding: utf-8 -*-
# !/usr/bin/pythonrrrr

from __future__ import print_function, unicode_literals;
import sys;
sys.path.append("../");
import  jieba;
import jieba.posseg as pseg;

print ("=== 自定义分词器 ===");

jieba.load_userdict("../../../resource/jieba/userdict.txt");

print ("======= 词性标注 =======");
jieba.add_word("凯特琳", tag="nr");
jieba.add_word("李铁军", tag="nr");
test_send = (
    "李小福和李铁军是创新办主任也是云计算方面的专家;什么是八一双鹿\n"
    "例如我输入一个带'韩玉赏鉴'的标题，在自定义词类中也增加了此词为N类\n"
    "[台中]正确应该不会被切开。mac中可分出[石墨烯]；此时又可以分出来凯特琳了。"
);
words = jieba.cut(test_send);
print("/".join(words));
print ("="*40);

result = pseg.cut(test_send);
for w in result:
    print(w.word, "/", w.flag, ", ", end ='');
print ("="*40);

terms = jieba.cut("easy_install as great");
print("/".join(terms));

terms = jieba.cut("Python 的正则表达式是好用的");
print("/".join(terms));
print ("="*40);








print ("====== 自定义调整词典 ======");
testlist = [
    ('今天天气不错',('今天', '天气')),
    ('如果放到post中将出现.',('中', '将')),
    ('我们中出了一个叛徒.',('一', '个')),
]
for send, seg in testlist:
    #print ("send:"+send);
    print('%s %s' % (send, seg))
    #print("seg:" + seg);
    print("/".join(jieba.cut(send, HMM=False)));
    word = ''.join(seg);
    print('%s Before: %s, After:%s' % (word, jieba.get_FREQ(word),jieba.suggest_freq(seg, True)));
    print("/".join(jieba.cut(send, HMM=False)));
    print("-" * 40);



print ("====== 自定义调节词典解决歧义分词问题 ======");
print("/".join(jieba.cut("如果放到post中将出现。", HMM=False)));
jieba.suggest_freq(("中", "将"), True);
print("/".join(jieba.cut("如果放到post中将出现。", HMM=False)));


print("/".join(jieba.cut("[台中]正确应该不会被切开。", HMM=False)));
jieba.suggest_freq(("台中"), True);
print("/".join(jieba.cut("[台中]正确应该不会被切开。", HMM=False)));


print ("====== 词性标注 ======");
words = pseg.cut("我爱北京天安门")
for word, flag in words:
    print ('%s %s' % (word, flag));
