# -- coding: utf-8 --
#1、什么是迭代
'''
注意: 集合是指包含一组元素的数据结构，我们已经介绍的包括：
1. 有序集合：list，tuple，str和unicode；
2. 无序集合：set
3. 无序集合并且具有 key-value 对：dict
'''
#data = range(1:101);

for i in range(1,101):
   if(i%7==0):
       print i;
   else:
       continue;
print ('===============================');


#2、索引迭代
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index,'-',name;

print zip([10, 20, 30], ['A', 'B', 'C']);

'''
在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如果我们想打印出名次 - 名字（名次从1开始)，
请考虑如何在迭代中打印出来。
提示：考虑使用zip()函数和range()函数
'''
L = ['Adam', 'Lisa', 'Bart', 'Paul']
socre = range(1,5);
data = zip(socre,L);
for index, name in enumerate(data):
    print name[0], '-', name[1];
print ('===============================');



#3、迭代dict的value
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 };
print d.values();
for v in d.values():
    print v;
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0;
for i in d.values():
    sum += i;
print sum / len(d);
print ('===============================');



#4、迭代dict的key和value
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.items();
for key, value in d.items():
    print key,":",value;

'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
打印出 name : score，最后再打印出平均分 average : score。
'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0;
for key, value in d.items():
    print key,":",value;
    sum += value;
print "average",':',sum/len(d);








