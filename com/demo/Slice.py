# -- coding: utf-8 --
#1、对list进行切片
L = ['Adam', 'Lisa', 'Bart', 'Paul']
#print L;

print L[0:3];#['Adam', 'Lisa', 'Bart']
print L[1:3];#['Lisa', 'Bart']
print L[:];#['Adam', 'Lisa', 'Bart', 'Paul']
print L[::2];#['Adam', 'Bart']

dataArray = range(1,101);
print dataArray[0:10];
print dataArray[2::3]; #从第三元素开始取，每隔2个取一个元素
print dataArray[4:50:5];
#‘开始元素’ : ‘最后元素’ : ‘取元素间隔’
print ('===============================');




#2、倒序切片
L = ['Adam', 'Lisa', 'Bart', 'Paul'];
print L[-2:]
print L[:-2]
print L[-3:-1];
#记住倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引。
print L[-4:];
print L[:];


'''
利用倒序切片对 1 - 100 的数列取出：
* 最后10个数；
* 最后10个5的倍数。
'''
L = range(1, 101);
print L;
print L[-10:]
print L[-46::5];
print L[4::5][-10:];
print ('===============================');

#3、对字符串切片
print 'ABCDEFG'[:3]
print 'ABCDEFG'[-3:]
print 'ABCDEFG'[::3];

print 'abc'.upper();
print 'ABC'.lower();

def myUpper(data):
    return str(data[0:1].upper())+str(data[1:]);
print myUpper('read');
print ('===============================');
