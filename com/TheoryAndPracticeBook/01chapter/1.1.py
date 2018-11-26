# -*- coding: utf-8 -*-
# !/usr/bin/python

from Book import Book;
from Color import Color;
import keyword;
#导入整个模块
import sys;

def countNum(param):
    reslut = ""
    if(param[1]+param[2]) == 0:
        reslut ="除数不能为0"
    else:
        res = param[0]/(param[1]+param[2])
        reslut ="this count: "+str(res)
    print(reslut)




#logistic_regression
if __name__=="__main__":
    countNum([10,2,3])
    book = Book(22);
    print("年龄:",book.getAge());

    black = Color(1, 2, 3);
    print(black)

    print("===== 保留关键字 =====");
    print(keyword.kwlist);

    print("===== 多行语句 =====");
    item_one = item_two = item_three = 11;
    total = item_one + \
            item_three + \
            item_two;
    print (total);

    print("===== 引号 =====");
    word = 'word';
    word2 = "word2";
    word3 = """a line one
    a line two
    a line three
    """
    print (word3);

    print("===== 字符串 =====");
    print ("自然字符串,通过在字符串前加r或R实现");
    str = R"this is a line with \n\r";
    print (str);

    print ("python允许处理Unicode字符串,在前缀加u或U");
    str1 = U"this is an unicode string";
    print (str1);

    print("===== print(输出) =====");
    #不换行输出
    str2 = "aa";
    str3 = "bb";
    print(str2, end=" ");
    print(str3, end=" ");












