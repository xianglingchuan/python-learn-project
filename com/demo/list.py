# -- coding: utf-8 --

#1、Python创建list
print ['aa','bb','cc'];

list = ['aa','bb','cc'];
print list;

emptyList = [];
print emptyList;

students = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59];
print students;
print '===============================';
print '===============================';


#2、Python按照索引访问list
L = ['Adam', 'Lisa', 'Bart']
print L[0];
print L[1];
#print L[3]; 超出下标
print '===============================';
print '===============================';


#3、Python之倒序访问list
print L[-1];
print L[-2];
print L[-3];
print '===============================';
print '===============================';


#4、Python之添加新元素
L = ['Adam', 'Lisa', 'Bart']
L.append("lili");
print "L=========",L;

L.insert(0,"admin");
print "L=========",L;
L[0] = "ADAM";
print "L=========",L;

L = ['Adam', 'Lisa', 'Bart'];
L.insert(2,"Paul");
print L;
print '===============================';
print '===============================';



#5、Python从list删除元素
L = ['Adam', 'Lisa', 'Bart', 'Paul'];
popItem = L.pop();
print "被删除的值是:",popItem;

iItem = L.pop(1);
print "将第二个元素删除",iItem

L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(2)
L.pop(2)
print L;

print '===============循环List================';
#循环List
for name in L:
    print name;
print '===============================';
print '===============================';



#6、Python中替换元素
L = ['Adam', 'Lisa', 'Bart'];
print L;
L[1] = "LISA";
L[-1] = "BART";
print L;

L = ['Adam', 'Lisa', 'Bart'];
L[-1] = L[0];
L[0] = "Bart";
print L;
print '===============================';
print '===============================';


#7、Python之创建tuple
t = ('Adam', 'Lisa', 'Bart')
print t;
print '===============================';
print '===============================';



#8、Python之创建单元素tuple
t = ();
print t;

t = (1);
print t;

t = (1,);
print t;

t = (1,2,4);
print t;
print '===============================';
print '===============================';

#9、Python之“可变”的tuple
t = ('a','b',['A','B']);
print t;
L = t[2];
L[0]='admin';
L[1]='User';
print t;

print '===============================';
print '===============================';












