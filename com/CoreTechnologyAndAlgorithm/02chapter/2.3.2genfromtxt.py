# -*- coding: utf-8 -*-
# !/usr/bin/python

import numpy as np;
import codecs;

print("\n\r");
print("====================================");
print("简单实例");
print("====================================");






f = open("test.csv", 'w');
f.write("1, 1.2, 1.3\n2,2.2,2.3\n字符串,xlc,33");
f.close();
a = np.genfromtxt('test.csv', dtype=[('myint','i8'),('myfloat','f8'), ('mystring','U5')], delimiter=",", comments='#')
print(a);




print("\n\r");
print("====================================");
print("中文展示");
print("====================================");

#字段中有中文,成功！
def conv_str_chs(x):
    print("x======", x);
    #return x.decode('gb2312')
    return x;

#测试失败
f = open('test02.csv', 'w', encoding='utf-8')
f.write(u'1,1.2,今123天\n2,2.2,789天');
f.close()
a = np.genfromtxt('test02.csv', dtype=[('myint','i8'),('myfloat','f8'), ('mystring','U32')], delimiter=",", comments='#',
                  converters={2:conv_str_chs})
print (a);


print("\n\r");
print("====================================");
print("空缺部分字段, 使用默认填充");
print("====================================");
# 空缺部分字段, 使用默认填充。文档中描述：
# Expected type Default
# bool False
# int -1
# float np.nan
# complex np.nan+0j
# string '???'

f = open('test03.csv', 'w')
f.write(",,")
f.close()
a = np.genfromtxt('test03.csv', dtype=[('myint', 'i8'), ('myfloat', 'f8'), ('mystring', 'U5')], delimiter=",",
                  comments='#',
                  filling_values={0:9, 1:9.9, 2:'abc'})
print(a)



#SciPy练习在项目中
