# coding=utf-8
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;


print("==========================================================")
print("创建DataFrame");
print("==========================================================")

print("==========================================================")
print("创建一个空的DataFrame");
print("==========================================================")
df = pd.DataFrame();
print (df);

print("==========================================================")
print("从列表创建DataFrame");
print("==========================================================")
data = [1,2,3,4,5];
df = pd.DataFrame(data);
print (df);

data = [['zs',10], ['ls', 12], ['wu', 13]];
#指定列标题
df = pd.DataFrame(data,columns=['Name','Age']);
print (df);

#指定数据类型
df = pd.DataFrame(data,columns=['Name','Age'], dtype=float);
print (df);

print("==========================================================")
print("从ndarrays/Lists的字典来创建DataFrame");
print("==========================================================")

data = {"Name":['Tom','Jack','Steve','Ricky'],'Age':[25,34,54,33]}
df = pd.DataFrame(data);
print (df);

#使用数组创建一个索引的数据帧(DataFrame)
df = pd.DataFrame(data, index=['001', '002', '003', '004']);
print (df);

print("==========================================================")
print("从列表创建数据帧DataFrame");
print("==========================================================")
data = [{'a':1, 'b':2}, {'a':5,'b':10, 'c':20}];
df = pd.DataFrame(data);
print (df);

#指定行索引值
df = pd.DataFrame(data,index=['first','second']);
print (df);

df1 = pd.DataFrame(data,index=['first','second'], columns=['a','B', 'C']);
print (df1);

df2 = pd.DataFrame(data, index=['first','second'],columns=['a','b','c']);
print (df2);


print("==========================================================")
print("从系列的字典来创建DataFrame");
print("==========================================================")
d = {'one' : pd.Series([1,2,3],index=['a','b','c']),
     'two' : pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])};
df = pd.DataFrame(d);
print(df);


print("==========================================================")
print("列选择");
print("==========================================================")
print(df['one']);

print("==========================================================")
print("列添加");
print("==========================================================")

df['three'] = pd.Series([10,20,30], index=['a', 'b', 'c']);
print(df);

df['four'] = df['one'] + df['three'];
print (df);

print("==========================================================")
print("删除列");
print("==========================================================")

print("==== del ====");
del df['one'];
print (df);

print("==== pop ====");
print(df.pop('two'));
print("==== 余下数据 ====");
print (df);

print("==========================================================")
print("行选择，添加和删除");
print("==========================================================")
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d);
print(df.loc['b']);

print("==== 按整数位置选择 ====");
print (df.iloc[2]);

print("==== 行切片 ====");
print (df[2:4]);

print("==== 附加行 ====");
df = pd.DataFrame([[1,2],[3,4]], columns=['a', 'b'], index=[0,1]);
df2 = pd.DataFrame([[5,6],[7,8]], columns=['a', 'b'], index=[2,3])
df = df.append(df2);
print (df);

print("==== 删除行 ====");
df = df .drop(0);
print (df);






