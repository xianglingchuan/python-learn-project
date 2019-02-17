# -*- coding: utf-8 -*-
# !/usr/bin/python
#加载训练模型
def load_mode(path):
    import os, CRFPP;
    # -v 3:access deep information like alpha, beta, prob
    # -nN: enable nbest output. N should be >= 2
    if os.path.exists(path):
        return CRFPP.Tagger('-m {0} -v 3 -n2'.format(path))
    return None;


#接收字符串，输出其识别出的地名
def locationNER(text):
    tagger = load_mode('./model')
    for c in text:
        tagger.add(c)
    result = [];
    #parse and change internal stated as 'parsed'
    tagger.parse();
    word = '';
    for i in range(0, tagger.size()):
        for j in range(0, tagger.xsize()):
            ch = tagger.x(i, j)
            tag = tagger.y2(i)
            if tag == 'B':
                word = ch;
            elif tag == 'M':
                word += ch;
            elif tag == 'E':
                word += ch
                result.append(word)
            elif tag == 'S':
                word = ch
                result.append(word)
    return result;


text = "我中午要去北京饭店，下午去中山公园，晚上回亚运村。";
print(text, locationNER(text), sep="===> ");

text = "我去回龙观，不去南锣鼓巷";
print(text, locationNER(text), sep="===> ");

text = "打地去北京南站";
print(text, locationNER(text), sep="===> ");
