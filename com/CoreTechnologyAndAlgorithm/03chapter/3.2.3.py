# -*- coding: utf-8 -*-
# !/usr/bin/python

print("\n\r");
print("====================================");
print("规则分词 - 双向最大匹配法");
print("====================================");


# 逆向最大匹配法
class MMReverse(object):
    def __init__(self):
        self.window_size = 3;

    def cut(self, text):
        result = [];
        index = len(text);
        dic = ['研究', '研究生', '生命', '命', '的', '起源']
        while index > 0:
            for size in range(index - self.window_size, index):
                piece = text[size:index]
                if piece in dic:
                    index = size + 1
                    break;
            index = index - 1;
            result.append(piece);
        print(result);
        return result;

#正向最大匹配法
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
            result.append(piece);
        print(result);
        return result;


#双向最大匹配法处理逻辑
#result<正向最大返回结果>
#resultReverse<逆向最大返回结果>
def BiDirectction(result, resultReverse):
    #取分词数少的,词数长度相同,最单词数少的，如果单词数一样，即返回任意一个即可。
    resultLen = len(result);
    resultReverseLen = len(resultReverse);
    if resultLen == resultReverseLen:
        #循环获取每个列表单字个数
        resultD = 0;
        for word in result:
            if len(word) == 1:
                resultD += 1;
        print("resultD====", resultD);

        resultReverseD = 0;
        for word in resultReverse:
            if len(word) == 1:
                resultReverseD += 1;
        print("resultReverseD====", resultReverseD);
        if resultD == resultReverseD:
            print(result);
        elif resultD < resultReverseD:
            print(result);
        elif resultReverseD < resultD:
            print(resultReverse);
    else:
        if resultLen > resultReverseLen:
            print(result);
        if resultReverseLen > resultLen:
            print(resultReverse);





if __name__ == '__main__':

    text = "研究生命的起源";
    #正向最大法
    tokenizer = MM();
    result = tokenizer.cut(text);
    #逆向最大法
    tokenizer2 = MMReverse();
    resultReverse = tokenizer2.cut(text);

    BiDirectction(result, resultReverse);