# -- coding: utf-8 --

print "1、python之面向对象编程";
'''
什么是面向对象编程
   面向对象编程是一种程序设计范式
   把程序看做不同对象的相互调用
类和实例
   类用于定义抽象类型
   实例根据类的定义被创建出来
面向对象编程：数据封装
'''

class Person2:
    def __init__(self,name):
        self.name = name;
p1 = Person2("Jack");
p2 = Person2("Mark");
print p1;
print p2;
print ('===============================\n');






print "2、python之定义类并创建实例 ";

print "\n练习\n";
class Person:
    def __init__(self):
        pass;
xiaoming = Person();
xiaohong = Person();

print xiaoming;
print xiaohong
print xiaoming==xiaohong;
print ('===============================\n');



print "3、python中创建实例属性";
print ('===============================\n');

xiaoming.name = 'Xiao Ming'
xiaoming.gender = 'Male'
xiaoming.birth = '1990-1-1';
print xiaoming.name;
print xiaoming.gender;
print xiaoming.birth;

print "\n练习\n";
p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1,key=lambda  p:p.name);
print L2[0].name
print L2[1].name
print L2[2].name
print ('===============================\n');




print "4、python中初始化实例属性";
#要特别注意的是，初学者定义__init__()方法常常忘记了 self 参数：
class Person(object):
    def __init__(self, name, gender, birth):
        self.name = name
        self.gender = gender
        self.birth = birth
jack = Person("jack","Male","1991-01-11");
#print jack.name;
#print jack.gender;

print "\n练习\n";
class PersonNew(object):
    def __init__(self, name, gender, birth, **kwargs):
        self.name = name
        self.gender = gender
        self.birth = birth
        for key,value in kwargs.items():
            setattr(self,key,value);

mark = PersonNew("mark","Male","1991-01-11",job='Student',favoute="打球");
print "name====>",mark.name;
print "job=====>",mark.job;
print "favoute====>",mark.favoute;
#print mark.favoute;
print ('===============================\n');


print "5、python中访问限制";
'''
Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，
该属性就无法被外部访问。
'''
class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'
p = Person('Bob');
print p.name;
print p._title;
#print p.__job; 访问不了

class Person(object):
    def __init__(self, name, score):
        self.name = name;
        self.__score = score;

p = Person('Bob', 59)
print "name=====>",p.name
try:
    print p.__score;
except AttributeError:
    print "attributeError";
print ('===============================\n');


print "6、python中创建类属性";
#类是模板，而实例则是根据类创建的对象
class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name

p1 = Person("Bob");
p2 = Person("Alice");
print p1.address;
print p2.address;
#p1.address = "bejin";
Person.address= "Bejin";
print p1.address;
print p2.address;

class Person(object):
    count = 0;
    def __init__(self,name):
        self.name = name;
        Person.count+=1;


p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count
print ('===============================\n');


print "7、python中类属性和实例属性名字冲突怎么办";
#当实例属性和类属性重名时，实例属性优先级高
class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name
p1 = Person('Bob')
p2 = Person('Alice')

print 'Person.address = ' + Person.address
p1.address = 'China'
print 'p1.address = ' + p1.address
print 'Person.address = ' + Person.address
print 'p2.address = ' + p2.address

del  p1.address;
print 'p1.address = ' + p1.address



class Person(object):
    __count = 0;
    def __init__(self,name):
        self.name = name;
        Person.__count+=1;


p1 = Person('Bob')
p2 = Person('Alice')
try:
    print Person.count
except AttributeError:
    print "attributeerror";
print ('===============================\n');



print "8、python中定义实例方法";
class Person(object):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

p1 = Person("Bob");
print p1.getName();


class Person(object):
    __score = 0;
    def __init__(self, name, score):
        self.name = name;
        self.__score = score;

    def get_grade(self):
        if (self.__score >= 90) :
            return "A-优秀";
        elif (self.__score >= 60 and self.__score < 90):
            return "B-及格";
        else:
            return "C-不及格";



p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()
print ('===============================\n');



print "9、python中方法也是属性";
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        return 'A'
p1 = Person("Bob", 90);
print p1.get_grade;
print p1.get_grade();


import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'


class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
p1 = Person("Bob", 90);
p1.get_grade = types.MethodType(fn_get_grade, p1, Person);
print p1.get_grade;
print p1.get_grade();

class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: "A";

p1 = Person('Bob', 90)
print p1.get_grade
print p1.get_grade()
print ('===============================\n');


print "10、python中定义类方法";



print ('===============================\n');
'''通过标记一个 @classmethod，该方法将绑定到 Person 类上，而非类的实例。
类方法的第一个参数将传入类本身，通常将参数名命名为 cls，上面的 
cls.count 实际上相当于 Person.count。
'''
#和属性类似，方法也分实例方法和类方法。
class Person(object):
    count = 0
    #类拟的类的静态方法
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

print Person.how_many()
p1 = Person('Bob');
print Person.how_many();
print p1.how_many();

p2 = Person("Jack");
print p2.how_many();
print Person.how_many();



