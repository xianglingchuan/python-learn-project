# -- coding: utf-8 --


#1、Python之if语句
age = 20;
if age>= 18:
    print ('当前年龄为成年人');
print ('===============================');


#2、Python之 if-else
age = 11;
if age>=18:
    print ('当前年龄为成年人');
else:
    print ('未成年');
print ('===============================');


#3、Python之 if-elif-else
age = 9;
if age >= 18:
    print ("当前年龄为成年人");
elif age>=10 and age < 18:
    print ("当前年龄应该在上中学了");
elif age >= 6 and age < 10:
    print ("应该在上小学");
else:
    print ('在家玩着呢');

age = 20
if age >= 6 and age< 18:
    print ('teenager')
elif age >= 18:
    print ('adult')
else:
    print ('kid')

score = 85
if score>=90:
    print ('excellent')
elif score >= 80:
    print ('good')
elif score >= 60:
    print ('passed')
else:
    print ('failed')
print ('===============================');




#4、Python之 for循环
L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print (name);

L = [75, 92, 59, 68];
sum = 0.0
for isum in L:
    sum += isum;
print (sum / 4);
print ('===============================');


#5、Python之 while循环
N = 10;
x = 0;
while x < N:
    print ("x====",x);
    x = x + 1;

sum = 0
x = 1;
while x < 100:
    sum += x;
    x += 2;
print (sum)
print ('===============================');


#6、Python之 break退出循环
sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 1
    if x > 100:
        break
print (sum)

print ('===============================');
sum = 0; #总数
n = 1;  #每次的值
i = 1;  #循环次数
while True:
    print ("n======",n);
    n = n*2;
    sum += n;
    #print "i========", i;
    if(i>=20):
        break;
    i += 1;

print ("sum=====",sum);


sum = 0; #总数
n = 1;  #每次的值
i = 1;  #循环次数
while True:
    n = n*2
    sum += n
    if(i>=20):
        break
    i += 1
print (sum)
print ('===============================');


#7、Python之 continue继续循环
L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:
    sum = sum + x
    n = n + 1
print (sum / n)


sum = 1
x = 1
while True:
    x = x + 1
    if x >= 100:
        break
    if(x%2==0):
        continue;
    sum += x;
print (sum)


sum = 0
x = 0
while True:
    x = x + 1;
    if x > 100:
        break
    if x%2==0:
        print ("x====>",x)
        continue
    sum += x
print (sum)
print ('===============================');


#8、Python之 多重循环
arr1 = ['A', 'B', 'C'];
arr2 = ['1', '2', '3'];
for x in arr1:
    for y in arr2:
        print ("x=",x,"y=",y);

for x in [1,2,3,4,5,6,7,8,9]:
    for y in [1,2,3,4,5,6,7,8,9]:
        if(x<y):
            print (str(x) + str(y));
print ('===============================');
