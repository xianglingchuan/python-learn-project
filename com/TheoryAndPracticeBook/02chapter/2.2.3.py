# -*- coding: utf-8 -*-
# !/usr/bin/python

print("============= 函数 ===============");
print("\n==== 定义函数 ====");
def fib(n):
    a, b = 0, 1;
    while a < n:
        print (a, end=" ");
        a, b = b, a+b;
    print();
fib(100);


print("\n==== 函数参数默认值 ====");
def sayHello(name="Tom"):
    print ("Hello %s" % (name));
sayHello();


print("\n==== 关键字参数 ====");
def person(name, age, **kw):
    print ("name: %s, age: %s, other:%s" % (name, age, kw));
person("xlc", 33);
person(name="ll", age=44, city="北京", sex="女");


print("\n==== 可变参数 ====");
def concat(*args, sep="/"):
    print (sep.join(args));
concat("我","是","可","变参数");


print("\n==== Lambda 形式====");
def Lambda(nums):
    nums.sort(key=lambda num: num[0])
    print(nums);

Lambda(nums=[(1, "one"), (2, 'two'), (3, 'three'), (4, "four")]);


