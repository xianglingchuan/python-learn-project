# -*- coding: utf-8 -*-
# !/usr/bin/python

print("\n\r");
print("====================================");
print("规则分词 - 逆向最大匹配法");
print("====================================");


class MM(object):
    def __init__(self):
        self.window_size = 3;

    def cut(self, text):
        result = [];
        index = len(text);
        dic = ['研究','研究生','生命','命','的','起源']
        while  index > 0:
            for size in range(index - self.window_size,index):
                piece = text[size:index]
                if piece in dic:
                    index = size + 1
                    break;
            index = index - 1;
            result.append(piece+"=====");
        print(result);

class MMTWO(object):
    def __init__(self):
        self.window_size = 4;

    def cut(self, text):
        result = [];
        index = len(text);
        #text_length = len(text);
        dic = ['南京市长','长江大桥','大桥','南京市']
        while index > 0:
            for size in range(index - self.window_size, index):
                piece = text[size:index]
                #print(piece);
                if piece in dic:
                    index = size + 1
                    break;
            index = index - 1;
            result.append(piece+"=====");
        print(result);



if __name__ == '__main__':
    text = "研究生命的起源";
    tokenizer = MM();
    print(tokenizer.cut(text));
    #['研究生=====', '命=====', '的=====', '起源=====']
    #['起源=====', '的=====', '生命=====', '研究=====']

    text = "南京市长江大桥";
    tokenizer = MMTWO();
    print(tokenizer.cut(text));







