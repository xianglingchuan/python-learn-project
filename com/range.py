# -- coding: utf-8 --


#1、生成列表
print range(1, 11);
L =[];
for x in range(1,11):
    L.append(x * x);
print L;

print [x * x for x in range(1, 11)];
'''
任务
请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
提示：range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...]
'''
print [x * (x+1) for x in range(1, 100, 2)]
print ('===============================');



#2、复杂表达式
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d;

tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

'''
任务
在生成的表格中，对于没有及格的同学，请把分数标记为红色。
提示：红色可以用 <td style="color:red"> 实现。
'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    style = "";
    if score< 60:
        style = "style='color:red'";
    return '<tr><td>%s</td><td %s>%s</td></tr>' % (name, style, score)

tds = [ generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
print ('===============================');



#3、条件过滤
print [x * x for x in range(1, 11)];
print [x * x for x in range(1, 11) if x % 2 == 0];
'''
任务
请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
提示：
1. isinstance(x, str) 可以判断变量 x 是否是字符串；
2. 字符串的 upper() 方法可以返回大写的字母。
'''
def toUppers(L):
    print [x.upper() for x in L if isinstance(x, str)];
toUppers(['Hello', 'world', 101])
print ('===============================');


#4、多层表达式
print [m + n for m in 'ABC' for n in '123'];
'''
利用 3 层for循环的列表生成式，找出对称的 3 位数。
例如，121 就是对称数，因为从右到左倒过来还是 121。
'''
print [int(str(m)+str(n)+str(i)) for m in range(1,10) for n in range(0,10) for i in range(0,10) if m==i]



