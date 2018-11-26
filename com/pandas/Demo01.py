# coding=utf-8


import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
print ("Hello, Pandas");

'''
Pandas处理以下三个数据结构
  1、系列(Series) 系列是具有均匀数据的一维数组结构。
  2、数据帧(DataFrame)  数据帧(DataFrame)是一个具有异构数据的二维数组。
  3、面板(Panel) 面板是具有异构数据的三维数据结构。在图形表示中很难表示面板。但是一个面板可以说明为DataFrame的容器。

'''

print("==========================================================")
print("对象创建");
print("==========================================================")

#对象系列创建
s = pd.Series([1, 3, 5, 7, np.nan, 9, 11]);
print(s);
print("--------------------------------");


#通过传递numpy数组，使用datetime索引和标记列来创建DataFrame：import pandas as pd
dates = pd.date_range('20181012',periods=7);
print(dates);
print("--------------------------------");


#np.random.rand:生成7行4列数据
df = pd.DataFrame(np.random.rand(7,4), index=dates, columns=list('ABCD'));
print("--"*16)
print (df);
print("--------------------------------");



#通过传递可以转换为类似系列的对象的字典来创建DataFrame
df2 = pd.DataFrame(
    {
        'A' : 1.,
        'B' : pd.Timestamp('20181012'),
        'C' : pd.Series(1,index=list(range(4)), dtype='float32'),
        'D' : np.array([3] * 4, dtype='int32'),
        'E' : pd.Categorical(['one','two', 'three', 'four']),
        'F' : 'foo'
    },
);
print(df2);
print("--------------------------------");
#打印数据帧的数据类型
print(df2.dtypes);
print("--------------------------------");


print("==========================================================")
print("查看数据");
print("==========================================================")

#查看框架的顶部和底部的数据行
dates = pd.date_range('20181012',periods=7);
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list("ABCD"));
#查看顶部数据
print (df.head());
print("--------------" * 10)
#查看底部数据3条
print (df.tail(3));

#显示索引，列和底层numpy数据
print ("索引值是==",df.index);
print ("列数据==",df.columns);
print ("底层数据==",df.values);
#描述显示数据的快速统计摘要
print ("描述显示数据==",df.describe());

#调换数据,X轴与Y轴的数据进行互换
print ("调换数据");
print (df.T);

#通过轴排序(axis=1轴排序/axis=0Y轴排序)
print (df.sort_index(axis=0,ascending=False));

#按值排序
print (df.sort_values(by='D'));



print("==========================================================")
print("选择区块");
print("==========================================================")

print("==========================================================")
print("获取");
print("==========================================================")
#选择一列，产生一个系列，相当于df.A
print(df['A']);
print("========= 选择通过[]操作符，选择切片行 ========")
print(df[0:2]);
print("========= 指定选择日期 ========")
print(df['20181012':'20181018'])


print("==========================================================")
print("按标签选择");
print("==========================================================")


print("======= 使用标签获取横截面 =======");
print(df.loc[dates[0]]);

print("======= 通过标签选择多轴 =======");
print(df.loc[:,['A','D']]);

print("======= 显示标签切片,包括两个端点 =======");
print(df.loc['2018-10-12':'2018-10-15',['A','B']]);

print("======= 减少返回对象的尺寸(大小) =======");
print(df.loc['2018-10-12',['A','B']]);

print("======= 获取标量值 =======");
print(df.loc[dates[0],'A']);

print("======= 快速方问标量(等同于先前的方法) ========")
print(df.at[dates[0], 'A']);


print("==========================================================")
print("通过位置选择");
print("==========================================================")

print("======= 通过传递的整数的位置选择 =======");
print(df.iloc[3]);

print("======= 通过整数切片,类似于numpy/python =======");
print(df.iloc[0:5,0:3]);

print("======= 通过整数位置的列表，类似于numpy/python样式 =======");
print(df.iloc[[1,2,4], [0,3]]);

print("======= 明确切片行 =======");
print(df.iloc[1:3,:]);

print("======= 明确切片列 =======");
print(df.iloc[:,1:3]);

print("======= 要明确获取值 =======");
print(df.iloc[1,1]);

print("======= 要快速访问标量(等同于先前的方法) =======");
print(df.iat[1,1]);


print("==========================================================")
print("布尔索引");
print("==========================================================")
print("======= 使用单列的值来选择数据 =======");
print(df[df.A > 0])

print("======= 从满足布尔条件的DataFrame中选择值 =======");
print(df);
print(df[df > 0]);


print("======= 使用isin()方法进行过滤 =======");
df2 = df.copy();
df2['E'] = ['one','two','three','four','five','six','seven'];
print(df2);
print("============= start to filter =============== ")
print(df2[df2['E'].isin(['two','four'])]);








