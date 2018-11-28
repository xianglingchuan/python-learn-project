# -*- coding: utf-8 -*-
# !/usr/bin/python

###################
#Hellow world
###################
def callHello():
    print ("hello world python.");
callHello();


print("============= 语句和控制流 ===============");
def CallLevel(score):
    if score >= 90:
        print ("优秀");
    elif score >= 60:
        print ("及格");
    else:
        print ("不及格");
CallLevel(99);


print("\n==== for ====");
def GetLevel(score):
    for lev in score:
        print(lev, end=" "); #不换行
GetLevel(["优秀","及格","不及格"]);

print("\n==== while ====");
def GetLevel2(score):
    countLev = len(score);
    while countLev > 0:
        print (score[countLev-1], end=" ");
        countLev -= 1;
GetLevel2([99,99, 44, 88, 66]);


print("\n==== range 循环输出数组的下标 ====");
def GetValue(score):
    for lev in range(len(score)): #注意这里的写法
        print (lev, end=" ");
GetValue(["优秀","及格","不及格"]);


print("\n==== break====");
def GetHighLev(score):
    high = 0;
    for lev in score:
        if lev < 90:
            break;
        else:
            high+=1;
    print ("成绩优秀的学生人数是:",high,"位");
GetHighLev(score=[99, 95, 68, 75, 90])


print("\n==== continue  ====");
def GetHighLev2(score):
    high = 0;
    for lev in score:
        if lev < 90:
            continue;
        else:
            high += 1;
    print("成绩优秀的学生人数是:", high, "位");
GetHighLev2(score=[99, 95, 68, 75, 90])

print("\n==== pass 什么也不做,占位符  ====");
def CallPass():
    pass;
print(CallPass());