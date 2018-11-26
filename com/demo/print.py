# -- coding: utf-8 --

#1、数据类型
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
print '===============================';
print '===============================';



#1、print使用方法
#打印单行信息
print 'hello,word';
#print语句可以跟上多个字符串，用逗号分隔开
print 'The quick','用逗号分隔开即可' \
                  ',TM今天天所好冷';
print 300;
print 100 + 200;
print '100 + 200=',100 + 200

print 'hello,python.';
print 'hello,','python.';
print '===============================';
print '===============================';


#3、Python的注释
print 'hello'; #这是一个注释


#4、Python中什么是变量
a = 1;
a = 123;
print a;
a = 'china';
print a;

a = 123;
a = 'aaaa';
print a;

x = 10;
x = x + 2 * 10;
print x;

a = 'abc';
b = a;
a = 23;
print a; #23
print b; #abc

'''
等差数列可以定义为每一项与它的前一项的差等于一个常数，可以用变量 x1 表示等差数列的第一项，用 d 表示公差，请计算数列

1 4 7 10 13 16 19 ...

前 100 项的和。
'''
x1 = 1;
d = 3;
n = 100;
x100 = x1+(n-1)*d;
s = (x1+x100)*n/2;
print "s:",s;
print '===============================';
print '===============================';


#5、Python中定义字符串
print 'Python was started in 1989\' by "Guido".';
print 'Python is free and easy to learn.';
print '===============================';
print '===============================';



#6、Python中raw字符串与多行字符串
print r'\(~_~)/ \(~_~)/'
print '''Line 1
Line 2
Line 3
'''
print 'Line1 1\n Line1 2\n Line1 3\n';

print r'''Python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!'''

print r'''\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.\''''
print '===============================';
print '===============================';



#7、Python中Unicode字符串
print u'中文';
print u'中文\n日文\n韩文'
print u'''
中文
日文
'''

print ur'''Python的Unicode字符串支持"中文",
"日文",
"韩文"等多种语言'''

str = '中国';
print str;

print u'''
静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
'''
print '===============================';
print '===============================';


#8、Python中整数和浮点数
print "1 + 2 + 3:", 1 + 2 + 3;
print "4 * 5 - 6:",4 * 5 - 6;
print "7.5 / 8 + 2.1:",7.5 / 8 + 2.1;

print 1+2;
print 1.0 + 2.0;

print 1+ 2.0;

print "11 / 4:",11 / 4; #取商值
print "11 % 4:",11 % 4; #取余数

print "11.0 / 4 :",11.0 / 4;

print "2.5 + 10 / 4:",2.5 + 10 / 4;  #4.5,先除后加
print "2.5 + 10.0 / 4:",2.5 + 10.0 / 4;
print '===============================';
print '===============================';


#9、Python中布尔类型
print "True and True:",True and True;
print "True and False:",True and False;
print "False and True:",False and True;
print "False and False:",False and False;

print "True or True:",True or True;
print "True or False:",True or False;
print "False or True:",False or True;
print "False or False:",False or False;

print not True;
print not False;

a = True;
print a and 'a=T' or 'a=F';
#计算结果不是布尔类型，而是字符串 'a=T'，这是为什么呢？
#因为Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True


a = 'python';
print 'hello,', a or 'world'; #hello,python;
b = '';
print 'hello,',b or 'world'; #hello,world;





