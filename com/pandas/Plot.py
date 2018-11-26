# coding=utf-8


import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;


print("==========================================================")
print("Pandas可视化");
print("==========================================================")

print("==== 基本绘图 ====");
df = pd.DataFrame(np.random.randn(10, 4), index=pd.date_range('2019/12/01', periods=10),
                  columns=list('ABCD'));
df.plot()



print("==== 条形图 ====");
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd']);
df.plot.bar();

df.plot.bar(stacked=True);

#获取水平条形图
df.plot.barh(stacked=True);


#直方图
print("==== 直方图 ====");
df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
df.plot.hist(bins=20);



df=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
df.hist(bins=20)


print("==== 箱形图 ====");
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box();


print("==== 区域块图形 ====");
df.plot.area();


print("==== 散点图形 ====");
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b');


print("==== 饼状图 ====");
df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)



plt.show();



# df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
# df.plot.bar().show();









