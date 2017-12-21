# -- coding: utf-8 --


#1、Python之什么是函数
print ('1111');
s = set(['A', 'B', 'C']);
print (s);

ss = ['1','2','3'];
print (ss);

r1 = 12.34
r2 = 9.08
r3 = 73.1
s1 = 3.14 * r1 * r1
s2 = 3.14 * r2 * r2
s3 = 3.14 * r3 * r3
print (s1);
print (s2);
print (s3);
#print (area_of_circle(s1)); 调用不成功，应该要引入函数库
print ('===============================');



#2、Python之调用函数
print (abs(100));
print (abs(-20));
print (abs(12.34));
#abs(1,2); 传入参数错误
#abs('str'); 传入类型错误

print (cmp(1,2));
print (cmp(2,1));
print cmp(3,3);
print int("124");
print int(12.34);
print str(123);
print str(12.34);


L = range(1,101);
sumList = [];
for i in L:
    value = i * i;
    sumList.append(value);
    #print i;

print sumList;
print sum(sumList);
print ('===============================');


#3、Python之编写函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print my_abs(12);
print my_abs(-120);
def square_of_sum(L):
    value = 0;
    for num in L:
        value += num * num;
    print "value===",value;
    return value;

print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])
print ('===============================');




#4、Python函数之返回多值
import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6);
print "x==",x, "y==",y;

r = move(100, 100, 60, math.pi / 6);
print r;

def quadratic_equation(a, b, c):
    x = b * b - 4 * a * c;
    if(x<0):
        return None;
    elif x==0:
        return -b /(2*a);
    else:
        return ((math.sqrt(x)-b)/(2*a)),((-math.sqrt(x) - b ) / (2 * a))

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)
print ('===============================');



#5、Python之递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(1);
print fact(5);
print fact(50);

def move(n, a, b, c):
    if n==1:
        print a,'-->',c;
        return
    else:
        move(n-1,a,c,b);
        move(1,a,b,c);
        move(n-1,b,a,c);

move(4, 'A', 'B', 'C')
print ('===============================');




#6、Python之定义默认参数
print int('123', 16);
print int('A', 16);

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5,2);
#由于函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必需参数的后面：
def fn1(a, b=1, c=2):
    return a+b+c;

print fn1(0);

#请定义一个 greet() 函数，它包含一个默认参数，如果没有传入，
# 打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'
def greet(msg = "world"):
    print "Hello,",msg,".";

greet()
greet('Bart')
print ('===============================');



#7、Python之定义可变参数
def fn(*args):
    print args;

fn();
fn('a','b','c');


#def average(*args):
    #print sum(args);
    #print sum(args) / len(args);
#average(10,20,4,1);


def average(*args):
    if (len(args)>=1):
        return sum(args)*1.0 / len(args);
    else:
        return 0.0;
print average();
print average(1, 2)
print average(1, 2, 2, 3, 4)