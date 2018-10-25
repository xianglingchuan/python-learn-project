# coding=utf-8

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;


print("==========================================================")
print("Pandas IO工具");
print("==========================================================")

filename = "../../resource/test.csv";

df = pd.read_csv(filename);
print (df);

print("==== 自定义索引 ====");
df = pd.read_csv(filename, index_col=['S.No']);
print (df);


print("==== 转换器 ====");
df = pd.read_csv(filename, dtype={'Salary':np.float64});
print (df.dtypes);

print("==== header_names ====");
df = pd.read_csv(filename, names=['a', 'b', 'c', 'd', 'e']);
print (df);

df = pd.read_csv(filename, names=['a', 'b', 'c', 'd', 'e'], header=0);
print (df);


print("==== skiprows ====");
df = pd.read_csv(filename, skiprows=2);
print (df);


print("==========================================================")
print("Pandas 稀疏数据");
print("==========================================================")
ts = pd.Series(np.random.randn(10));
ts[2:-2] = np.nan;
sts = ts.to_sparse();
print (sts);

print("========");
df = pd.DataFrame(np.random.randn(10000, 4));
df.ix[:9998] = np.nan;
sdf = df.to_sparse();
print (sdf.density);

#to_dense可以将任何稀疏对象转换回标准密集形式
ts = pd.Series(np.random.randn(10));
ts[2:-2] = np.nan;
sts = ts.to_sparse();
print("========");
print (sts);
print("========");
print (sts.to_dense());

print("==== 稀疏Dtypes ====");
#稀疏数据应该具有与其密集表示相同的dtype。 目前，支持float64，int64和booldtypes。

s = pd.Series([1, np.nan, np.nan]);
print (s);
print ("===============");
s.to_sparse();
print (s);




