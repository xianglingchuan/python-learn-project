# coding=utf-8
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

print("==========================================================")
print("与Pandas一起使用If/Ttuth语句");
print("==========================================================")

# if pd.Series([False, True, False]):
#     print ("I am True");
#error ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

if pd.Series([False, True, False]).any():
    print ("I am any");

print (pd.Series([True]).bool());

print("==== 按位布尔值 ====");
s = pd.Series(range(5));
print (s==4);

print("==== isin操作符 ====");
s = pd.Series(list('abc'));
s = s.isin(['a', 'c', 'e']);
print (s);

print ("==== 重构索引与ix陷阱 ====");
df = pd.DataFrame(np.random.randn(6, 4), columns = ['one', 'two', 'three', 'four'],
                  index=list("abcdef"));
print (df);
print ("====================");
print (df.ix[['b', 'c', 'e']]);

print ("====================");
print (df.reindex(['b', 'c', 'e']));

print ("====================");
print (df.ix[[1, 2, 4]]);

print ("====================");
print (df.reindex([1, 2, 4]));








