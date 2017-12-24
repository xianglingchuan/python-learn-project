# -- coding: utf-8 --
#第一行解决中文注释问题

#print 1 #输出1

#整型
iNumber=10;
print "整型:",iNumber;

#浮点型
iFloat=1.23;
print "浮点型:",iFloat;

#字符串型
iString="hello,word!";
print "字符串型:",iString;

#布尔型
iBoole=True;
print "布尔型:",iBoole;

#空值
iNull=None;
print "空值型:",iNull;




'''
试一试，在右边编辑器中，完成以下任务:
1. 计算十进制整数 45678 和十六进制整数 0x12fd2 之和。
2. 请用字符串表示出Learn Python in imooc。
3. 请计算以下表达式的布尔值（注意==表示判断是否相等）：
    100 < 99
    0xff == 255
注意：使用print命令
'''
#第一题
a = 45678;
b = 0x12fd2;
print a + b;

#第二题
str = "Learn Python in Chain";
print str;

#第三题
if 100 < 99:
    print "100小于99";
else:
    print "100大于99";

print "100<99结果是:",(100<99);
print "0xff == 255结果是:",(0xff == 255);







