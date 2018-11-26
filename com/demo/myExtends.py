# -- coding: utf-8 --
print "1、python中什么是继承";
'''
新类不必从头编写
新类从现有的类继承，就自动拥有了现有类的所有功能
新类只需要编写现有类缺少的新功能

继承的好处
  复用已有代码
  自动拥有了现有类的所有功能
  只需要编写缺少的新功能
继承的特点:
  了类的父类是is关系:
  class Student(Person):
      pass;
  p = Person();
  s = Student();
  p是一个Person-->正确
  p是一个Student-->错误
  s是一个Student-->正确
  s是一个Person-->正确
 
has关系应该使用组合而非继承
   Student类和Book类是has关系:
   class Student(Person):
       def __init__(self,booKname):
            self.book = Book(bookName); 
 
Python的继承
   总是从某个类继承
   class MyClass(Object):
       pass;
   不要忘记调用super().__init__
   def __init__(self,args):
       super(SubClass,self).__init__(args);
       pass;   
  
'''
print ('===============================\n');



print ("2、python中继承一个类 ");
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender;

'''
一定要用 super(Student, self).__init__(name, gender) 去初始化父类，否则，
继承自 Person 的 Student 将没有 name 和 gender。
函数super(Student, self)将返回当前类继承的父类，即 Person ，然后调用__init__()方法，
注意self参数已在super()中传入，在__init__()中将隐式传递，不需要写出（也不能写）。
'''
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student,self).__init__(name,gender);
        self.score = score;

s = Student("jack","Male",99);
print ("练习");

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name,gender);
        self.course = course;

t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course
print ('===============================\n');




print ("3、python中判断类型");
'''
函数isinstance()可以判断一个变量的类型，既可以用在Python内置的数据类型如str、list、dict，
也可以用在我们自定义的类，它们本质上都是数据类型。
'''
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')
print isinstance(p,Person); #ture
print isinstance(s,Student);#true
print isinstance(s,Teacher); #false

print ("练习");

class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')

print isinstance(t,Person); #true
print isinstance(t,Student); #false
print isinstance(t,Teacher); #true
print isinstance(t,object);  #true
print ('===============================\n');




print ("4、python中多态");
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name
def who_am_i(x):
    print x.whoAmI();
p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English');

class myWhoAm(object):
    def __init__(self,name):
        self.name = name;
    def whoAmI(self):
        return "I am a myWhoAm, my name is %s" % self.name;

my = myWhoAm("Tom");

who_am_i(p);
who_am_i(s);
who_am_i(t);
who_am_i(my);


print ("练习");
import json

class Students(object):
    def __init__(self,lists):
        self.lists = lists;
    def read(self):
        return self.lists;

s = Students('["Tim","Bob","Alice"]');
print json.load(s)
print ('===============================\n');



print ("4、python中多重继承");
#除了从一个父类继承外，Python允许从多个父类继承，
# 称为多重继承。
class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a

class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'
    def getName(self):
        return "class.name:",self.__name__;

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'
    #def getName(self):
        #return "class.name:",self.__name__;

class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'
d = D('d'); #调用多继承的同名方法直接报错


print "练习";
class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(Student,BasketballMixin):
    pass

class FTeacher(Teacher,FootballMixin):
    pass

s = BStudent()
print s.skill()

t = FTeacher()
print t.skill()
print ('===============================\n');


print "6、python中获取对象信息";
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

print type(123);
s = Student('Bob','Male',88);
print type(s);

#可以用 dir() 函数获取变量的所有属性
print dir(123);
print dir(s);

#获取类name的属性
print getattr(s,'name');
#设置类name新的值
print setattr(s,"name","Tom");
print getattr(s,'name');

#获取类的age属性，如果属性不存在，就返回默认值20
print getattr(s,"age",20);

print ("练习");

class Person(object):
    def __init__(self, name, gender, **kw):
        self.name = name;
        self.gender = gender;
        for key, value in kw.items():
            print "key=",key;
            print "value=",value;
            setattr(self,key,value);

p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course

print ('===============================\n');

