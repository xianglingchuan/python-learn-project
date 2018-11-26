# -- coding: utf-8 --

#3、python把函数作为参数
def add(x, y, f):
    return f(x) + f(y)

print add(-5,9,abs);
import math;
def add(x, y,f):
    return f(x) + f(y);

print add(25,9,math.sqrt);
print ('===============================');


#4、python中map()函数
'''
map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
'''
def f(x):
    return x*x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]);

def handWord(word):
    return str(word[0].upper())+str(word[1:].lower());
print map(handWord,['adam', 'LISA', 'barT']);
print ('===============================');


#5、python中reduce()函数
def f(x, y):
    return x + y;
print reduce(f, [1, 3, 5, 7, 9]);
print reduce(f, [1, 3, 5, 7, 9], 100);

def myData(x, y):
    return x * y;
print reduce(myData, [2, 4, 5, 7, 12]);
print ('===============================');




#6、python中filter()函数
'''
filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，
filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
'''
def is_odd(x):
    return x % 2 == 1;
print filter(is_odd, [1, 4, 6, 7, 9, 12, 17])

def is_not_empty(s):
    return s and len(s.strip()) > 0
#注意: s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。
#当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')，如下：
print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

a = '   123';
print a;
print a.strip();
'''
请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
def is_sqr(x):
    return math.sqrt(x) % 1 == 0;
print filter(is_sqr, range(1, 101))
print ('===============================');

#7、python中自定义排序函数
print sorted([36, 5, 12, 9, 21])
'''
但 sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，比较函数的定义是，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
'''
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], reversed_cmp)
print sorted(['bob', 'about', 'Zoo', 'Credit']);

def myreverse_cmp(x, y):
    return cmp(x.lower(), y.lower());
print sorted(['bob', 'about', 'Zoo', 'Credit'], myreverse_cmp);
print ('===============================');

#8、python中返回函数
def calc_sum(lst):
    return sum(lst);
print calc_sum([1,2,3,4]);

#返回函数
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum;
f = calc_sum([1,2,3,4]);
print f;
print f();

'''
请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
'''

def calc_prod(list):
    def a():
        return reduce(lambda x, y: x * y, (list));
    return a;

f = calc_prod([1, 2, 3, 4]);
print f;
print f();
print ('===============================');



#9、python中闭包
def count():
    fs = []
    for i in range(1, 4):
        def f(m = i):
             return m*m;
        fs.append(f)
    return fs

f1, f2, f3 = count();
print f1();
print f2();
print f3();
print ('===============================');



#10、python中匿名函数
'''
高阶函数可以接收函数做参数，有些时候，我们不需要显式地定义函数，直接传入匿名函数更方便。
'''
#关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print sorted([1, 3, 9, 5, 0], lambda x,y: -cmp(x,y))
#print sorted([6,2,3,4,5],lambda x, y : x+y);


def is_not_empty(s):
    return s and len(s.strip()) > 0
print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END']);
print filter(lambda s : s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END']);


def is_not_empty(s):
    return s and len(s.strip()) > 0

print filter(lambda s : s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])
print ('===============================');




#11、python中decorator装饰器
def f1(x):
    return x*2;

def new_fn(f):
    def fn(x):
        print 'call------>'+f.__name__+"()";
        return f(x);
    return fn;

#第一种调用方法
g1 = new_fn(f1);
print ("g1====",g1(5));

#第二种调用方法
f1 = new_fn(f1);
print ("f1=====>",f1(5));

#使用装饰器
@new_fn
def myFunction(x):
    return x+5;
myFunction(100);
print ('===============================');




#12、python中编写无参数decorator
def log(f):
    def fn(x):
        print 'call------> ' + f.__name__ + '()...'
        return f(x)
    return fn;

@log
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1));
print factorial(10);


#@log 问题报错
'''
因为 add() 函数需要传入两个参数，但是 @log 写死了只含一个参数的返回函数。
要让 @log 自适应任何参数定义的函数，可以利用Python的 *args 和 **kw，保证任意个数的参数总是能正常调用：
'''
def logs(f):
    def fn(*args, **kwargs):
        print 'call------> ' + f.__name__ + '()...'
        return f(*args, **kwargs)
    return fn;

def add(x,y):
    return x+y;
print add(1, 2);


import time

def performance(f):
    def myfn(*args, **kwargs):
        print "performance----->"+f.__name__+"()....";
        print "运行时间为:",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
        return f(*args, **kwargs);
    return myfn;

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10);
print ('===============================');





#13、python中编写带参数decorator
def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test();




import time

def performance(unit):
    def per_decorator(f):
        def wrapper(*args, **kwargs):
            print "call functionName:",f.__name__+"()......";
            print "unit---->",unit;
            return f(*args, **kwargs);
        return wrapper;
    return per_decorator;

@performance('s')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10);
print ('===============================');




#14、python中完善decorator
def f1(x):
    pass
print f1.__name__;


'''
这样写decorator很不方便，
因为我们也很难把原函数的所有必要属性都一个一个复制到新函数上，
所以Python内置的functools可以用来自动化完成这个“复制”的任务：
'''
import functools;

def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)

    #wrapper.__name__ = f.__name__
    #wrapper.__doc__ = f.__doc__
    return wrapper
@log
def f2(x):
    pass
print f2.__name__
'''
最后需要指出，由于我们把原函数签名改成了(*args, **kw)，
因此，无法获得原函数的原始参数信息。即便我们采用固定参数来装饰只有一个参数的函数：
'''

import time, functools

def myperformance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args,**kwargs):
            print("unit------>",unit)
            return f(*args,**kwargs);
            #这里面等于又重新调了一下传入的f函数
        return wrapper;
    return perf_decorator;


@myperformance('www')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial.__name__
print ('===============================');



#15、python中偏函数
print int('12345');

print int('12345', base=8);

print int('12345', 16);

def int2(x, base=2):
    return int(x, base);

print int2('1000000');
print int2('1010101');

import functools

int2 = functools.partial(int, base=2);
print int2('1000000');
print int2('1010101');

import functools
sorted_ignore_case = functools.partial(sorted, key=str.lower)
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']);
print ('===============================');


