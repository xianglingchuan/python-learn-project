# -*- coding: utf-8 -*-
# !/usr/bin/python

print("============= 类 ===============");
class BaseAnimal:
    def __init__(self, name, age=1):
        self.name = name;
        self.age = age;
    def speak(self):
        print ("我的名字是[%s],今年[%d]岁" % (self.name, self.age));

class SubDog(BaseAnimal):
    def __init__(self, name, age, say):
        BaseAnimal.__init__(self, name, age);
        self.say = say;
        print ("这是子类[%s]" % (self.name));
        print ("*"*20+"调用子函数方法"+"*"*20);
    def talk(self):
        BaseAnimal.speak(self);
        print("我的名字是[%s],今年[%d]岁, 我想说:%s" % (self.name, self.age, self.say));
ani = SubDog("dog", 2, "汪汪.....");
ani.talk();