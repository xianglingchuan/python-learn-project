# coding=utf-8
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

print("==========================================================")
print("Pandas窗口函数");
print("==========================================================")

print("==== .rolling()函数 ====");

df = pd.DataFrame(np.random.randn(10, 4),
                  index = pd.date_range('1/1/2020', periods=10),
                  columns=['A', 'B', 'C', 'D']);
print (df.rolling(window=5).mean());

print("==== .expanding()函数 ====");
df = pd.DataFrame(np.random.randn(10, 4),
                  index = pd.date_range('1/1/2019', periods=10),
                  columns=['A', 'B', 'C', 'D']);
print (df.expanding(min_periods=3).mean());

print("==== .expanding()函数 ====");
df = pd.DataFrame(np.random.randn(10, 4),
                  index = pd.date_range('1/1/2018', periods=10),
                  columns=['A', 'B', 'C', 'D']);
print (df.ewm(com=0.5).mean());


print("==========================================================")
print("Pandas聚合");
print("==========================================================")

print("==== DataFrame应用聚合 ====");
df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2019', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print (df);
print ("=====================");
r = df.rolling(window=3,min_periods=1);
print (r);


print("==== 在整个数据框上应用聚合 ====");
df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print(df);

r = df.rolling(window=3, min_periods=1);
print (r.aggregate(np.sum));


print("==== 在整据框的单个列上应用聚合 ====");
print (r['A'].aggregate(np.sum));

print("==== 在DataFrame的多列上应用聚合 ====");
print(r[['A','B']].aggregate(np.sum));

print("==== 在DataFrame的单个列上应用多个函数 ====");
print (r['A'].aggregate([np.sum,np.mean]));

print("==== 在DataFrame的多列上应用多个函数 ====");
print(r[['A','B']].aggregate([np.sum,np.mean]));

print("==== 将不同的函数应用于DataFrame的不同列 ====");
print (r.aggregate({'A':np.sum, 'B':np.mean}));


print("==========================================================")
print("Pandas缺失数据");
print("==========================================================")
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'],
                  columns=['one', 'two', 'three']);
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']);
print (df);

print("==== 检查缺失值， isnull()/notnull() ====");
print (df['one'].isnull());
print (df['two'].notnull());


print("==== 缺少数据的计算 求和NA=0, 数据全部是NA结果将是NA ====");
print (df['two'].sum());

df = pd.DataFrame(index=[0,1,2,3,4,5],columns=['one','two'])
print (df['one'].sum());

print("==== 清理/填充缺少数据 fillna() ====");

print("==== 用标量值替换NaN ====");
df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'],columns=['one',
'two', 'three']);

df = df.reindex(['a', 'b', 'c']);
print (df);
print (df.fillna(0)); #填充值
print (df.fillna(1));

print("==== 填写NA前进和后退 pad/fill填充方法向前  bfill/backfill填充方法向后====");
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']);
print (df);
print ("======================");
print (df.fillna(method='pad'));

print ("======================");
print (df.fillna(method='backfill'));

print("==== 丢失缺少的值 dropna() ====");
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']);
print (df);
print ("==========================");
print (df.dropna());
print ("==========================");
print (df.dropna(axis=1));

print("==== 替换丢失(或)通用值 ====");
df = pd.DataFrame({'one':[10,20,30,40,50,2000],
'two':[1000,0,30,40,50,60]});
print (df);
print ("==========================");
print (df.replace({1000:9999, 2000:8888}));


print("==========================================================")
print("Pandas分组(GroupBy)");
print("==========================================================")
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data);
print (df);

print("==== 将数据拆分成组 obj.groupby('key)/obj.groupby(['key1', 'key2'])/obj.groupby('key1',axis=1) ====");
print (df.groupby('Team'));
print (df.groupby('Team').groups);

print ("===========按多例分组===============");
#按多例分组
print (df.groupby(['Team', 'Year']).groups);

print ("=========== 迭代遍历分组 ===============");
grouped = df.groupby("Year");
for name, group in grouped:
    print ("name=>", name);
    print (group);

print ("=========== 选择一个分组 ===============");
print (grouped.get_group(2014));

print ("=========== 聚合 ===============");
print (grouped['Points'].agg(np.mean));

print ("=========== 查看分组大小 ===============");
grouped = df.groupby("Team");
print (grouped.agg(np.size));


print ("=========== 一次应用多个聚合函数 ===============");
print (grouped['Points'].agg([np.sum, np.mean, np.std]));


print ("=========== 转换 ===============");
score = lambda x: (x - x.mean()) / x.std()*10;
print (grouped.transform(score));

print ("=========== 过滤 ===============");
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data);
#这里的len(x)是指记录条数
filter = df.groupby("Team").filter(lambda  x: len(x) >=2);
print (filter);
print ("==========================");


print("==========================================================")
print("Pandas合并/连接");
print("==========================================================")
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print (left)
print("========================================")
print (right)


print ("=========== 在一个键上合并两个数据帧 ===============");
rs = pd.merge(left, right, on="id");
print (rs);

print ("=========== 合并多个键上的两个数据框 ===============");
print (pd.merge(left,right,on=['id', 'subject_id']));

print ("=========== 合并使用how的参数 ===============");
print (left)
print("========================================")
print (right)
print("========================================")
rs = pd.merge(left, right, on='subject_id', how='left');
print (rs);

print("========================================")
rs = pd.merge(left, right, on='subject_id', how='right');
print (rs);

print ("=========== Outer Join示例 ===============");
print (pd.merge(left, right, how='outer', on='subject_id'));

print ("=========== Inner Join示例 ===============");
print (pd.merge(left, right, how='inner', on='subject_id'));

print("==========================================================")
print("Pandas级联");
print("==========================================================")

print ("=========== 连接对象 ===============");
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5]);
rs = pd.concat([one, two]);
print (rs);

print (pd.concat([one, two], keys=['x','y']));
print("========================================")
print (pd.concat([one, two], keys=['x','y'], ignore_index=True));

print (pd.concat([one,two], axis=1));

print ("=========== 使用附加连接 ===============");
print (one.append(two));

print (one.append([two,one,two]));

print ("=========== 时间序列 ===============");
print (pd.datetime.now());

print ("=========== 创建一个时间戳 ===============");
time = pd.Timestamp('2018-12-04');
print (time);

time = pd.Timestamp(1588686880,unit='s')
print(time);


print ("=========== 创建一个时间范围 ===============");
time = pd.date_range('12:00', '23:59', freq='30min').time;
print (time);


print ("=========== 改变时间的频率 ===============");
print (pd.date_range("12:00", '23:59', freq='H').time);

print ("=========== 转换为时间戳 ===============");
time = pd.to_datetime(pd.Series(['Jul 31, 2009','2019-10-10', None]));
print (time);
print (pd.to_datetime("2020-11-11"));
print (pd.Timestamp("2020-11-11").date());


print("==========================================================")
print("Pandas日期功能");
print("==========================================================")

print ("=========== 创建一个日期范围 ===============");
datelist = pd.date_range('2020/11/21', periods=5);
print (datelist);

print ("=========== 更改日期频率 ===============");
datelist = pd.date_range('2020/11/21', periods=5, freq='M');
print (datelist);

print ("=========== bdate_range()函数 ===============");
print (pd.bdate_range('2011/11/03', periods=5));

start = pd.datetime(2018, 11, 11);
end = pd.datetime(2018, 11, 15);
print (pd.date_range(start,end));


print("==========================================================")
print("Pandas时间差(Timedelta)");
print("==========================================================")

print ("=========== 字符串 ===============");
timediff = pd.Timedelta('2 days 2 hours 15 minutes 30 seconds')
print(timediff);

print ("=========== 整数 ===============");
print(pd.Timedelta(6, unit='h'));

print ("=========== 数据偏移 ===============");
print (pd.Timedelta(days=2));

print ("=========== 运算操作 ===============");
s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
print (s);
print (td);
df = pd.DataFrame(dict(A=s, B=td));
print (df);

print ("=========== 相加操作 ===============");
df['C'] = df['A'] + df['B'];
print (df);


print ("=========== 相减操作 ===============");
df['C'] = df['A'] + df['B'];
df['D'] = df['A'] - df['B'];
print (df);


print("==========================================================")
print("Pandas分类数据");
print("==========================================================")

print ("=========== 对象创建(类别/分类) ===============");
s = pd.Series(['a', 'b', 'c', 'a'], dtype="category")
print (s);

cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c']);
print (cat);

cat = cat = pd.Categorical(['a','b','c','a','b','c','d'], ['c','b','a']);
print (cat);

cat = cat = pd.Categorical(['a','b','c','a','b','c','d'], ['c','b','a'], ordered=True);
print (cat);

print ("=========== 描述 ===============");
cat = pd.Categorical(['a','c','c',np.nan], categories=['b','a','c']);
df = pd.DataFrame({"cat":cat,"s":["a","c","c",np.nan]});
print (df.describe());
print ("===================");
print (df["cat"].describe());


print ("=========== 获取类别的属性 ===============");
s = pd.Categorical(['a','c','c',np.nan], categories=['b','a','c']);
print (s.categories);

print (s.ordered);

print ("=========== 重命名类别 ===============");
s = pd.Series(['a','b','c','a'], dtype="category")
s.cat.categories = ["Group %s" % g for g in s.cat.categories]
print (s.cat.categories);

print ("=========== 附加新类别 add_categories ===============");
s = s.cat.add_categories([4]);
print (s.cat.categories);

print ("=========== 删除类别 remove_categories ===============");
print (s);
print ("After removal:");
print (s.cat.remove_categories("Group a"));


# print ("=========== 分类数据的比较 ===============");
# cat2 = pd.Series([1,2,3]).astype("category", categories=[1,2,3], ordered=True)
# cat1 =pd.Series([2,2,2]).astype("category", categories=[1,2,3], ordered=True)
# print (cat2>cat1);




