# -- coding: utf-8 --

print ("老式类声明与新式类声明的不同");
class oldPerson():
    pass;

class newPerson(object):
    pass;
p1 = oldPerson();
p2 = newPerson();
print p1;
print p2;
print dir(p1);
print dir(p2);
print type(p1);
print type(p2);

print "\n==============================";
print ("属性的定义\n");
class Programer(object):
    score = 99;
    def __init__(self, name, age, weight):
        self.name = name;
        self._age = age;
        self.__weight = weight;

    def get_weight(self):
        return self.__weight;
programer = Programer("Jack",22,88);
print dir(programer);
print dir(programer.__dict__);
print programer.get_weight();
print programer._Programer__weight;
programer._Programer__weight = 99;
print programer.get_weight();
print programer._Programer__weight;


print "\n==============================";
print ("类的定义\n");
class Programer(object):
    score = 99;
    def __init__(self, name, age, weight):
        self.name = name;
        self._age = age;
        self.__weight = weight;

    @property
    def get_weight(self):
        return self.__weight;

    @classmethod
    def getScore(cls):
        return cls.score;

    def self_introduction(self):
        print "I am is %s, I am %s year old" % (self.name, self._age);
programer = Programer("Tom",22,88);
print dir(programer);
print Programer.getScore();
print programer.get_weight;
programer.self_introduction();



print "\n==============================";
print ("类的继承\n");
class Programer(object):
    score = 99;
    def __init__(self, name, age, weight):
        self.name = name;
        self._age = age;
        self.__weight = weight;

    @property
    def get_weight(self):
        return self.__weight;

    @classmethod
    def getScore(cls):
        return cls.score;

    def self_introduction(self):
        print "I am is %s, I am %s year old" % (self.name, self._age);

class BackendProgramer(Programer):
    def __init__(self,name, age, weight, language):
        super(BackendProgramer,self).__init__(name,age,weight);
        self.language = language;
programer = Programer("Tom",22,88);
backendProgramer = BackendProgramer("Jack",33,99,"python");
print dir(backendProgramer);
print backendProgramer;
print type(backendProgramer);
print isinstance(backendProgramer, BackendProgramer);
print issubclass(BackendProgramer,Programer);


print "\n==============================";
print ("类的多态\n");
class Programer(object):
    score = 99;
    def __init__(self, name, age, weight):
        self.name = name;
        self._age = age;
        self.__weight = weight;

    @property
    def get_weight(self):
        return self.__weight;

    @classmethod
    def getScore(cls):
        return cls.score;

    def self_introduction(self):
        print "I am is %s, I am %s year old" % (self.name, self._age);

class BackendProgramer(Programer):
    def __init__(self,name, age, weight, language):
        super(BackendProgramer,self).__init__(name,age,weight);
        self.language = language;

    def self_introduction(self):
        print "I am is %s, I am %s year old, language:%s" % (self.name, self._age,self.language);

class FrontendProgramer(Programer):
    def __init__(self,name, age, weight, frame):
        super(FrontendProgramer,self).__init__(name,age,weight);
        self.frame = frame;

    def self_introduction(self):
        print "I am is %s, I am %s year old, frame:%s" % (self.name, self._age,self.frame);


def introduction(programer):
    if isinstance(programer, Programer):
        programer.self_introduction();


programer = Programer('Alili', 22, 90);
#programer.self_introduction();
backendProgramer = BackendProgramer("Tim", 30, 70, "Python");
#backendProgramer.self_introduction();
frontendProgramer = FrontendProgramer("Jack", 30, 55, "Angue");
#frontendProgramer.self_introduction();
introduction(backendProgramer);
introduction(frontendProgramer);


print "\n==============================";
print ("对象的实例化\n");
class Programer(object):

    def __init__(self, name, age):
        self.name = name;
        self._age = age;

    def __new__(cls, *args, **kwargs):
        print "call __new__ method";
        print args;
        return super(Programer,cls).__new__(cls,*args,**kwargs);

programer = Programer("Tom",22);
print programer.__dict__;


print "\n==============================";
print ("类与运算符\n");
s = "test";
s == s;
print dir(s);
#['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

class Programer(object):

    def __init__(self, name, age):
        self.name = name;
        self._age = age;

    def __new__(cls, *args, **kwargs):
        print "call __new__ method";
        print args;
        return super(Programer,cls).__new__(cls,*args,**kwargs);

    def __eq__(self, other):
        if isinstance(other,Programer):
            if self._age == other._age:
                return True;
            else:
                return False;
        else:
            raise Exception("The type of object must be Programer");

    def __add__(self, other):
        if isinstance(other,Programer):
            return other._age + self._age;
        else:
            raise Exception("The type of object must be Programer");

p1 = Programer("mack", 22);
p2 = Programer("Jack", 33);
print p1 == p2;
print p1 + p2;

print "\n==============================";
print ("类的展示\n");
class Programer(object):

    def __init__(self, name, age):
        self.name = name;
        self._age = age;

    def __str__(self):
        return "%s is year %s old" % (self.name, self._age);

    def __dir__(self):
        return self.__dict__.keys();

p = Programer("lili", 22);
print p;
print dir(p);


print "\n==============================";
print ("类的属性控制\n");
class Programer(object):

    def __init__(self, name, age):
        self.name = name;
        self._age = age;

    def __getattribute__(self, item):
        print ("call __getattribute__");
        #return getattr(self,item); #也是在次调用__getattribute__方法
        #return self.__dict__[item];#也是在次调用__getattribute__方法
        return super(Programer,self).__getattribute__(item);

    def __setattr__(self, key, value):
        print ("call __setattr__");
        #setattr(self, key, value); #也是在次调用__setattr__
        self.__dict__[key] = value;

p = Programer("lili", 22);
print p.name;