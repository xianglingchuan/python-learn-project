# coding=utf-8
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

print("==========================================================")
print("创建面板");
print("==========================================================")

print("==== 从3D ndarray创建 ====");
data = np.random.rand(2,4,5);
p = pd.Panel(data);
print (p);

#提示以下内容，建议使用Panel.to_frame()方法
'''
sys:1: FutureWarning:
Panel is deprecated and will be removed in a future version.
The recommended way to represent these types of 3-dimensional data are with a MultiIndex on a DataFrame, via the Panel.to_frame() method
Alternatively, you can use the xarray package http://xarray.pydata.org/en/stable/.
'''

print("==== 从DataFrame对象的dict创建面板 ====");
data = {"Item1" : pd.DataFrame(np.random.randn(4, 3)),
        "Item2" : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data);
print (p);


print("==== 创建一个空面板 ====");
p = pd.Panel();
print (p);

print("==== 从面板中选择数据 ====");
data = {"Item1" : pd.DataFrame(np.random.randn(4, 3)),
        "Item2" : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data);
print ("Item1数据内容");
print (p['Item1']);

print ("Item2数据内容");
print (p['Item2']);
#上面示例有两个数据项，这里只检索item1。结果是具有4行和3列的数据帧(DataFrame)，
# 它们是Major_axis和Minor_axis维。

print("==== 使用major_axis ====");
#可以使用panel.major_axis(index)方法访问数据
#获取所有元素中第一行数据
print (p.major_xs(1));

print("==== 使用minor_axis ====");
print (p.minor_xs(1));


print("==========================================================")
print("Pandas基本功能");
print("==========================================================")

print("==== 系列基本功能 ====");
'''
axes    返回行轴标签列表。
dtype   返回对象的数据类型(dtype)。
empty   如果系列为空，则返回True。
ndim    返回底层数据的维数，默认定义：1。
size    返回基础数据中的元素数。
values  将系列作为ndarray返回。
head()  返回前n行。
tail()  返回最后n行。
'''
s = pd.Series(np.random.randn(4));
print (s);

print("==== axes示例(返回行轴标签列表) ====");
print (s.axes);

print("==== empty示例 ====");
print (s.empty);

print("==== ndim示例(返回底层数据的维数，默认定义：1) ====");
print (s.ndim);

print("==== size示例 ====");
print (s.size);

print("==== values示例 ====");
print (s.values);

print("==== head()和tail()方法示例 ====");
#要查看Series或DataFrame对象的小样本，请使用head()和tail()方法
print (s.head(2));
print (s.tail(2));


print("==== DataFrame基本功能 ====");
'''
DataFrame基本功能
  T 转置行和列。
  axes  返回一个列，行轴标签和列轴标签作为唯一的成员。
  dtypes  返回此对象中的数据类型(dtypes)。
  empty 如果NDFrame完全为空[无项目]，则返回为True; 如果任何轴的长度为0。
  ndim  轴/数组维度大小。
  shape 返回表示DataFrame的维度的元组。
  size  NDFrame中的元素数。
  values  NDFrame的Numpy表示。
  head()  返回开头前n行。
  tail()  返回最后n行。
'''
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df = pd.DataFrame(d);
print (df);


print("==== T(转置)示例 ====");
print (df.T);

print("==== axes示例(返回行轴标签和列轴标签) ====");
print(df.axes);

print("==== dtypes示例 ====");
print (df.dtypes);

print("==== empty示例 ====");
print (df.empty);

print("==== ndim示例 ====");
print (df.ndim);

print("==== shape示例(返回DataFrame的维度的元组) ====");
print(df.shape);

print("==== size示例(返回DataFrame中的元素数) ====");
print (df.size);

print("==== values示例(将DataFrame中的实际数据作为NDarray返回) ====");
print (df.values);

print("==== head示例 ====");
print (df.head(2));

print("==== tail示例 ====");
print (df.tail(3));


print("==========================================================")
print("Pandas描述性统计");
print("==========================================================")
#有很多方法用来集体计算DataFrame的描述性统计信息和其他相关操作。
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

df = pd.DataFrame(d);
print (df);

print("==== sum()方法(返回所请求轴的值的总和) ====");
print (df.sum());


print("==== axis=1示例 ====");
#计算从列1开始值
print (df.sum(1));

print("==== mean()示例(求平均值) ====");
print (df.mean());

print("==== std()示例(返回数字列的Bressel标准偏差) ====");
print (df.std());
'''
函数和说明
count() 非空观测数量
sum() 所有值之和
mean()  所有值的平均值
median()  所有值的中位数
mode()  值的模值
std() 值的标准偏差
min() 所有值中的最小值
max() 所有值中的最大值
abs() 绝对值
prod()  数组元素的乘积
cumsum()  累计总和
cumprod() 累计乘积
'''

print("==== 汇总数据 ====");
print (df.describe());


#include是用于传递关于什么列需要考虑用于总结的必要信息的参数。获取值列表; 默认情况下是”数字值”。
# object - 汇总字符串列
# number - 汇总数字列
# all - 将所有列汇总在一起(不应将其作为列表值传递)
print (df.describe(include=['object']));

#执行错误
#print (df.describe(include=['all']));
'''
Traceback (most recent call last):
  File "/Users/Documents/work/pythonWork/learnOctober/com/pandas/Panel.py", line 197, in <module>
    print (df.describe(include=['all']));
  File "/Users/Library/Python/3.6/lib/python/site-packages/pandas/core/generic.py", line 8574, in describe
    data = self.select_dtypes(include=include, exclude=exclude)
  File "/Users/Library/Python/3.6/lib/python/site-packages/pandas/core/frame.py", line 3057, in select_dtypes
    lambda x: frozenset(map(_get_dtype_from_object, x)), selection)
  File "/Users/Library/Python/3.6/lib/python/site-packages/pandas/core/frame.py", line 3057, in <lambda>
    lambda x: frozenset(map(_get_dtype_from_object, x)), selection)
  File "/Users/Library/Python/3.6/lib/python/site-packages/pandas/core/dtypes/common.py", line 1933, in _get_dtype_from_object
    return _get_dtype_from_object(np.dtype(dtype))
TypeError: data type "all" not understood
'''

print("==========================================================")
print("Pandas函数应用");
print("==========================================================")
'''
要将自己或其他库的函数应用于Pandas对象，应该了解三种重要的方法。
使用适当的方法取决于函数是否期望在整个DataFrame，行或列或元素上进行操作。
表明智函数应用：pipe()
行或列函数应用：apply()
元素函数应用：applymap()
'''
print("==== 表格函数应用 ====");

#加法器函数
def adder(ele1, ele2):
    return ele1 + ele2;
df = pd.DataFrame(np.random.randn(5,3), columns=['col1', 'col2', 'col3']);
print (df);

#执行adder函数，将值添加5
#print(df.pipe(adder, 5));
#print (df);

print("==== 行或列智能函数应用 ====");
#可以使用apply()方法沿DataFrame或Panel的轴应用任意函数，它与描述性统计方法一样，采用可选的轴参数。
print("np.mean===", np.mean);
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])

print("apply之前原始数据")
print (df);

print("apply(np.mean)之后数据");#数据值无变化
df.apply(np.mean)
print (df);

print("df.apply(np.mean,axis=1)之后数据"); #数据值无变化
df.apply(np.mean,axis=1);
print (df);

print("lambda之后数据"); #数据值无变化
df.apply(lambda x: x.max() - x.min());
print (df);


print("==== 元素智能函数应用 ====");
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print (df);
df['col1'].map(lambda x:x*1000000); #数据值无变化
print (df);

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.applymap(lambda x:x*100); #数据值无变化
print (df);


print("==========================================================")
print("Pandas重建索引");
print("==========================================================")
'''
重新索引会更改DataFrame的行标签和列标签。
  重新索引意味着符合数据以匹配特定轴上的一组给定的标签。
  可以通过索引来实现多个操作 -重新排序现有数据以匹配一组新的标签。
  在没有标签数据的标签位置插入缺失值(NA)标记。
'''
N=20
df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})
print (df);

df_reindexed = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B']);
print(df_reindexed);

print("==== 重建索引与其他对象对齐 ====");
df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
print ("df1=====", df1);
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
print ("df2=====", df2);

df1 = df1.reindex_like(df2)
print (df1);

print("==== 填充时重新加注 ====");
'''
reindex()采用可选参数方法，它是一个填充方法，其值如下：
   pad/ffill - 向前填充值
   bfill/backfill - 向后填充值
   nearest - 从最近的索引值填充
'''
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

print (df2.reindex_like(df1));
print (df2.reindex_like(df1, method='ffill'));


print("==== 重建索引时的填充限制 ====");
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

print (df2.reindex_like(df1));
print (df2.reindex_like(df1, method='ffill', limit=2));


print("==== 重命名(rename()) ====");
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print (df1);
print(df1.rename(columns={'col1' : 'C1', 'col2': 'C2', 'col3': 'C3'},
                 index={0:"apple", 1:'banana', 2 : 'durian'}));
#rename()方法提供了一个inplace命名参数，默认为False并复制底层数据。 指定传递inplace = True则表示将数据重命名。

print("==========================================================")
print("Pandas迭代器");
print("==========================================================")
'''
Pandas对象之间的基本迭代的行为取决于类型。
  当迭代一个系列时，它被视为数组式，基本迭代产生这些值。其他数据结构，如：DataFrame和Panel，遵循类似惯例迭代对象的键。
  基本迭代(对于i在对象中)产生 -Series - 值DataFrame - 列标签Pannel - 项目标签
'''
N=20
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })
for col in df:
    print (col);
'''
要遍历数据帧(DataFrame)中的行，可以使用以下函数
  iteritems() - 迭代(key，value)对
  iterrows() - 将行迭代为(索引，系列)对
  itertuples() - 以namedtuples的形式迭代行
'''

print("==== iteritems()示例 ====");
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
print ("原始数据集:", df);
# for key, value in df.iteritems():
#     print (key, value);

print("==== iterrows()示例 ====");
for row_index, row in df.iteritems():
    print (row_index, row);

print("==== itertuples()示例 ====");
for row in df.itertuples():
    print (row);

#注意 - 不要尝试在迭代时修改任何对象。迭代是用于读取，
# 迭代器返回原始对象(视图)的副本，因此更改将不会反映在原始对象上。
for index, row in df.iteritems():
    row['a'] = 10;
print(df.get(0));
print (df);


print("==========================================================")
print("Pandas排序");
print("==========================================================")
'''
Pandas有两种排序方式，
  它们分别是 -
        按标签
        按实际值
'''
unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],
                         columns=['col2','col1']);
print (unsorted_df);

print("==== 按标签排序 ====");#也就是第一行的行号排序
sorted_df = unsorted_df.sort_index();
print (sorted_df);

print("==== 排序顺序 ====");#降序
sorted_df = unsorted_df.sort_index(ascending=False);
print (sorted_df);

print("==== 按列排列 ====");
sorted_df = unsorted_df.sort_index(axis=1);
print(sorted_df);


print("==== 按值排序 ====");
unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
print ("原始数据===>", unsorted_df);
sorted_df = unsorted_df.sort_values(by='col1');
print(sorted_df);

sorted_df = unsorted_df.sort_values(by=['col1', 'col2']);
print(sorted_df);

print("==== 排序算法 ====");
#sort_values()提供了从mergeesort，heapsort和quicksort中选择算法的一个配置。Mergesort是唯一稳定的算法
sorted_df = unsorted_df.sort_values(by='col1', kind='mergesort');
print (sorted_df);

print("==========================================================")
print("Pandas排序");
print("==========================================================")
#Pandas提供了一组字符串函数，可以方便地对字符串数据进行操作
'''
lower() 将Series/Index中的字符串转换为小写。
upper() 将Series/Index中的字符串转换为大写。
len() 计算字符串长度。
strip() 帮助从两侧的系列/索引中的每个字符串中删除空格(包括换行符)。
split(' ')  用给定的模式拆分每个字符串。
cat(sep=' ')  使用给定的分隔符连接系列/索引元素。
get_dummies() 返回具有单热编码值的数据帧(DataFrame)。
contains(pattern) 如果元素中包含子字符串，则返回每个元素的布尔值True，否则为False。
replace(a,b)  将值a替换为值b。
repeat(value) 重复每个元素指定的次数。
count(pattern)  返回模式中每个元素的出现总数。
startswith(pattern) 如果系列/索引中的元素以模式开始，则返回true。
endswith(pattern) 如果系列/索引中的元素以模式结束，则返回true。
find(pattern) 返回模式第一次出现的位置。
findall(pattern)  返回模式的所有出现的列表。
swapcase  变换字母大小写。
islower() 检查系列/索引中每个字符串中的所有字符是否小写，返回布尔值
isupper() 检查系列/索引中每个字符串中的所有字符是否大写，返回布尔值
isnumeric() 检查系列/索引中每个字符串中的所有字符是否为数字，返回布尔值。
'''
s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])
print (s);

print("==== lower()函数示例 ====");
print (s.str.lower());

print("==== upper()函数示例 ====");
print(s.str.upper());

print("==== len()函数示例 ====");
print(s.str.len());


print("==== strip()函数示例 ====");
s = pd.Series(['Tom ', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])
print ("原始数据: ");
print (s);
print(s.str.strip());

print("==== split(pattern)函数示例 ====");
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s);
print (s.str.split(' '));

print("==== cat(sep=pattern)函数示例  ====");
print (s.str.cat(sep=' <=>'));

print("==== get_dummies()函数示例 ====");
print(s.str.get_dummies());


print("==== contains()函数示例 如果元素中包含子字符串，则返回每个元素的布尔值True，否则为False ====");
print (s.str.contains(' '));

print("==== replace(a, b)函数示例 ====");
print (s.str.replace('@', '$'));

print("==== repeat(value)函数示例 ====");
print (s.str.repeat(5));

print("==== count(pattern)函数示例 ====");
print(s.str.count('T'));

print("==== startswith(pattern) ====");
print (s.str.startswith('T'));

print("==== endswith(pattern) ====");
print (s.str.endswith('t'));


print("==== find(pattern) ====");
print(s.str.find('e'));

print("==== findall(pattern) ====");
print(s.str.findall('o'));

print("==== swapcase()函数 ====");
print(s.str.swapcase());

print("==== islower()函数 ====");
print(s.str.islower());

print("==== isupper() ====");
print(s.str.isupper());

print("==== isnumberic() ====");
print(s.str.isnumeric());


print("==========================================================")
print("Pandas选项和自定义");
print("==========================================================")
'''
API由五个相关函数组成。它们分别是
   get_option()
   set_option()
   reset_option()
   describe_option()
   option_context()
'''

print("==== get_option(param) ====");
'''
get_option(param)需要一个参数，并返回下面输出中给出的值
get_option需要一个参数，并返回下面输出中给出的值
display.max_rows显示默认值。解释器读取此值并显示此值作为显示上限的行。
'''

#解释器读取此值并显示此值作为显示上限的行
print("display.max_rows=", pd.get_option("display.max_rows"));

#解释器读取此值并显示此值作为显示上限的行
#这里展示的是0
print("display.max_columns = ", pd.get_option("display.max_columns"));
print ("display.max_columns = ", pd.get_option("display.max_columns"))


print("==== set_option(param, value) ====");

print("before display.max_rows=", pd.get_option("display.max_rows"));
pd.set_option("display.max_rows", 90);
print("after display.max_rows=", pd.get_option("display.max_rows"));

print ("before display.max_columns = ", pd.get_option("display.max_columns"))
pd.set_option("display.max_columns", 32);
print ("after  display.max_columns = ", pd.get_option("display.max_columns"))


print("==== reset_option(param) 将该值设置为默认值====");
pd.reset_option("display.max_columns");
print ("reset display.max_columns = ", pd.get_option("display.max_columns"))

pd.reset_option("display.max_rows");
print ("reset display.max_rows = ", pd.get_option("display.max_rows"))

print("==== describe_option(param) 打印参数的描述====");
pd.describe_option("display.max_rows");

print("==== option_context() 可以临时设置该值====");
aInt = 10;
if aInt == 10:
    #临时并没有改变值
    pd.option_context("display.max_rows", 10);
    print(pd.get_option("display.max_rows"))
else:
    print ("不等于10");

print ("globa display.max_rows = ", pd.get_option("display.max_rows"))
'''
display.max_rows	要显示的最大行数
display.max_columns	要显示的最大列数
display.expand_frame_repr	显示数据帧以拉伸页面
display.max_colwidth	显示最大列宽
display.precision	显示十进制数的精度
'''

print("==========================================================")
print("Pandas索引和选择数据");
print("==========================================================")
'''
Pandas现在支持三种类型的多轴索引; 这三种类型在下表中提到
   .loc()  基于标签
   .iloc() 基于整数
   .ix() 基于标签和整数
'''

print("==== .loc() ====");
'''
.loc()具有多种访问方式
   单个标量标签
   标签列表
   切片对象
   一个布尔数组
'''
df = pd.DataFrame(np.random.randn(8, 4),index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
print (df);
print (df.loc[:, 'A']);

#多个列进行展示
print (df.loc[:, ['A', 'B']]);

#行加列的选择
print (df.loc[['a','b','f','h'],['A','C','D']]);

print (df.loc[:, ['A','C']]);

#按行进行选择
print (df.loc['a':'h']);



print("==========================================================")
print("Pandas统计函数");
print("==========================================================")
print("==== pct_chnage()函数(此函数将每个元素与其前一个元素进行比较，并计算变化百分比。) ====");

s = pd.Series([1,2,3,4,5,4]);
print (s.pct_change());
#
# 0         NaN    1
# 1    1.000000    2
# 2    0.500000    3
# 3    0.333333    4
# 4    0.250000    5
# 5   -0.200000    4

df = pd.DataFrame(np.random.randn(5,2));
print (df.pct_change);
#默认情况下，pct_change()对列进行操作; 如果想应用到行上，那么可使用axis = 1参数

print("==== 协方差 Cov系列示例 ====");
s1 = pd.Series(np.random.randn(10));
s2 = pd.Series(np.random.randn(10));
print (s1.cov(s2));


frame = pd.DataFrame(np.random.randn(10,5), columns=['a', 'b', 'c', 'd', 'e']);
print (frame['a'].cov(frame['b']));
print (frame.cov());

print("==== 相关性 ====");
frame = pd.DataFrame(np.random.randn(10,5), columns=['a', 'b', 'c', 'd', 'e']);

print (frame['a'].corr(frame['b']));
print (frame.corr());

print("==== 数据排名 ====");
s = pd.Series(np.random.np.random.randn(5), index=list('abcde'))
s['d'] = s['b'];
print (s.rank());

print ("average");
print (s.rank(0,"average"));

print ("min");
print (s.rank(0,"min"));

print ("max");
print (s.rank(0,"max"));

print ("first");
print (s.rank(0,"first"));






















