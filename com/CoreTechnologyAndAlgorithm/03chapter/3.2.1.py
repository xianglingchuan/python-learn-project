# -*- coding: utf-8 -*-
# !/usr/bin/python

print("\n\r");
print("====================================");
print("规则分词 - 正向最大匹配法");
print("====================================");


class MM(object):
    def __init__(self):
        self.window_size = 3;

    def cut(self, text):
        result = [];
        index = 0;
        text_length = len(text);
        dic = ['研究','研究生','生命','命','的','起源']
        while text_length > index:
            for size in range(self.window_size+index, index, -1): #4,0,-1
                piece = text[index:size]
                if piece in dic:
                    index = size -1
                    break;
            index = index + 1;
            result.append(piece+"=====");
        print(result);

class MMTWO(object):
    def __init__(self):
        self.window_size = 4;

    def cut(self, text):
        result = [];
        index = 0;
        text_length = len(text);
        dic = ['南京市长','长江大桥','大桥']
        while text_length > index:
            for size in range(self.window_size+index, index, -1): #4,0,-1
                piece = text[index:size]
                #print(piece);
                if piece in dic:
                    index = size -1
                    break;
            index = index + 1;
            result.append(piece+"=====");
        print(result);



if __name__ == '__main__':
    text = "研究生命的起源";
    tokenizer = MM();
    print(tokenizer.cut(text));
    #['研究生=====', '命=====', '的=====', '起源=====']

    text = "南京市长江大桥";
    tokenizer = MMTWO();
    print(tokenizer.cut(text));







