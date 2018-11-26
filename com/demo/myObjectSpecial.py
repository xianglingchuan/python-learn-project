# -- coding: utf-8 --

print "1、python中什么特殊方法";
'''
Python如何把做任意变量变成str?
   因为任何数据类型的实例都有一个特殊方法
   __str__();
   
Python如何把任意变量变成str?
   如果给Person类加上__str__()这个特殊方法
   就能按我们的定义的格式打印类的内容
   
Python的特殊方法
   用于print的__str__
   用于len的__len__
   用于cmp的__cmp__

Python的特殊方法
   特殊方法定义在class中
   不需要直接调用
   Python的某些函数或操作符会调用对应的特殊方法
  
正确实现特殊方法
   只需要编写用到的特殊方法
   有关联性的特殊方法都必须实现
      例如:__getattr__
          __setattr__
          __delattr__
'''
print ('===============================\n');


print ("2、python中 __str__和__repr__ ");
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
    __repr__ = __str__
p = Person("Bob","male");
print p;
p;


print ("练习");
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return ("<%s: %s,%s,%s>" % (self.__class__.__name__, self.name,self.gender,self.score));

s = Student('Bob', 'male', 88)
print s;
print ('===============================\n');


print ("3、python中 __cmp__")
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__

    def __cmp__(self, s):
        if self.name < s.name:
            return -1
        elif self.name > s.name:
            return 1
        else:
            return 0;

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]
print sorted(L);

def isStudent(x):
    if isinstance(x,Student):
        return True;
    else:
        return False;
#L = [Student('Tim', 99), Student('Bob', 88), 100, 'Hello']
#print sorted(isStudent(L));

print "练习";
class StudentNew(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__

    def __cmp__(self, s):
        if(self.score > s.score):
            return -1;
        elif(self.score < s.score):
            return 1;
        else:
            if(self.name > s.name):
                return 1;
            elif(self.name < s.name):
                return -1;
            else:
                return 0;
LNew = [StudentNew('Tim', 99), StudentNew('Bob', 88), StudentNew('Alice', 99)]
print sorted(LNew)
print ('===============================\n');



print ("4、python中 __len__");
class Students(object):
    def __init__(self, *args):
        self.names = args
    def __len__(self):
        return len(self.names)
ss = Students('Bob', 'Alice', 'Tim');
print len(ss);
'''
斐波那契数列是由 0, 1, 1, 2, 3, 5, 8...构成。
请编写一个Fib类，Fib(10)表示数列的前10个元素，
print Fib(10) 可以打印出数列的前 10 个元素，
len(Fib(10))可以正确返回数列的个数10。
'''
class Fib(object):

    def __init__(self, num):
        L = [0,1];
        for i in range(num-2):
            L.append(L[-1]+L[-2]);
        self.names = L;

    def __str__(self):
        return str(self.names)

    def __len__(self):
        return len(self.names);
f = Fib(10)
print f
print len(f)
print ('===============================\n');


print ("5、python中数学运算");
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __str__(self):
        return '%s/%s' % (self.p, self.q)
    __repr__ = __str__

r1 = Rational(1, 3)
r2 = Rational(1,2);
print r1 + r2;

print ("练习");
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational((self.p * r.p), self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        if self.p < self.q:
            k = self.p;
        else:
            k = self.q;
        for x in range(k, 0, -1):
            if self.p%x==0 and self.q%x==0:
                self.p=self.p/x;
                self.q=self.q/x;
                break;
        return '%s/%s' % (self.p, self.q)
    __repr__ = __str__

'''
3/4
1/4
1/8
2/1
'''
r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2
print ('===============================\n');


print ("6、python中类型转换");
print int(12.34);
print float(12);
#r = Rational(12,5);
#print int(r);

print "*******";
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        print "(p===%s, q====%s)" % (self.p, self.q);

    def __int__(self):
        return self.p;

print int(Rational(7, 2))
print int(Rational(1, 3))


print "<练习>";
class Rational(object):

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p

    def __float__(self):
        return (self.p * 1.0) / self.q;

print float(Rational(7, 2));
print float(Rational(1, 3));
print ('===============================\n');


print ("7、python中 @property");

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

s = Student("Bob", 59);
s.score = 60;
print "score====>",s.score;

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

#s = Student("Bob", 59);
#s.set_score(1000)
#print "score====>",s.score;
#print "======";


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
s = Student("Bob", 59);
s.score = 60;
print "score---->",s.score;
#s.score = 1000; #ValueError: invalid score


print "《练习》"
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.__score >= 80:
            return "A";
        elif self.__score<80 and self.__score>=60:
            return "B";
        else:
            return "C";

s = Student('Bob', 59)
print s.grade

s.score = 60
print s.grade

s.score = 99
print s.grade
print ('===============================\n');


print ("8、python中 __slots__");
class Student(object):
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score

s = Student('Bob', 'male', 59);
s.name = "Tim";
print s.name;
s.score = 99;
print s.score;
s.gender = 'A';
print s.gender;
s.score = "88";
print s.score;
#s.grade = 'AA'; #赋值失败


print "《练习》";
class Person(object):
    __slots__ = ('name', 'gender')
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    __slots__ = ('score');
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender);
        self.score = score;

s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score
#s.age = 33;
print ('===============================\n');

print ("9、python中 __call__");
'''
一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()。
'''
f = abs;
print f.__name__;

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print 'My name is %s...' % self.name
        print 'My friend is %s...' % friend

p = Person("Bob","male");
p("Tim");
p("Jack");



class Fib(object):
    def __init__(self):
        pass;
    def __call__(self, number):
        numbers = [0,1];
        for i in range(number-2):
            numbers.append(numbers[-1]+numbers[-2]);
        return numbers;


f = Fib()
print f(10);


