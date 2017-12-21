# -- coding: utf-8 --

#1、Python之什么是dict
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}

print d;
print len(d);

l=['a','b','c'];
print len(l);

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul':75
}
print d;

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
d['Paul'] = 75;
print d;

print '===============================';


#2、Python之访问dict
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
};

print d['Adam'];
print d.get('Adam');
print d.get('aa'); #不存在的key,返回None

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print "Adam:"+str(d.get("Adam"));
print "Lisa:"+str(d.get("Lisa"));
print "Bart:"+str(d.get("Bart"));

print d;
for(key, value) in d.items():
    print("%s:%s "%(key,value));
print '===============================';




#3、Python中dict的特点
    #dict的第一个特点是查找速度快
    #key不能重复
    #dict的第三个特点是作为 key 的元素必须不可变

dd = {
    '123': [1, 2, 3],  # key 是 str，value是list
    123: '123',  # key 是 int，value 是 str
    ('a', 'b'): True  # key 是 tuple，并且tuple的每个元素都是不可变对象，value是 boolean
   }
print dd;

dd2 = {
    '123' : [1,2,4],
    123 : "456",
    True: ('a','b')
};
print dd2;


score = {
    'Adam' : 95,
    'Lisa' : 85,
    'Bart' : 59,
};
print score;
print '===============================';




#4、Python更新dict
d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
print d;
d[72] = 'Paul';
d[59] = 'BART';
print d;
print '===============================';


#5、Python之 遍历dict
d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
for key in d:
    print "key:",key;
    print "value:",d.get(key);

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print str(key),":",d.get(key);
print '===============================';



#6、Python中什么是set
s = set(['A', 'B', 'C']);
print s;
s = set(['A', 'B', 'C', 'C'])
print s;

student = set(['Adam','Lisa','Bart','Paul']);
print student;
print '===============================';



#7、Python之 访问set
student = set(['Adam','Lisa','Bart','Paul']);

print  "判断Bart是否在set集合中:",'Bart' in student;
print  "判断Bill是否在set集合中:",'Bill' in student;
print  "判断Lisa是否在set集合中:",'Lisa' in student;
print  "判断lisa是否在set集合中:",'lisa' in student;


#8、Python之 set的特点
'''
set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。
set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。
最后，set存储的元素也是没有顺序的。
'''
#判断用户输入的星期是否合法
weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
userInput = "mon";
if userInput in weekdays:
    print "input ok"
else:
    print "input error"
months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug','Sep','Oct','Nov','Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print 'x1: ok'
else:
    print 'x1: error'

if x2 in months:
    print 'x2: ok'
else:
    print 'x2: error'
print '===============================';



#9、Python之 遍历set
s = set(['Adam', 'Lisa', 'Bart'])
for name in s:
    print name;

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for value in s:
    print value[0],":", value[1];

print '===============================';


#10、Python之 更新set
'''
由于set存储的是一组不重复的无序元素，因此，更新set主要做两件事：
一是把新的元素添加到set中，二是把已有元素从set中删除。
'''
s = set([1, 2, 3])
s.add(4);
print s;
s.add(4);
print s;
s.remove(4);
print s;
#s.remove(50);
#print s;

s = set(['Adam', 'Lisa', 'Paul']);
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for key in L:
    print key;
    if (key in s) == False:
        s.add(key);
    else:
        s.remove(key);
print L;
print (s);




print '===============================';






