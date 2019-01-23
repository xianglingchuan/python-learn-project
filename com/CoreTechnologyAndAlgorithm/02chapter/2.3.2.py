# -*- coding: utf-8 -*-
# !/usr/bin/python

import numpy as np;

print("\n\r");
print("====================================");
print("arange(n)生成n-1维的数字");
print("====================================");
arr1 = np.arange(15);
print(arr1);
print(arr1.shape);



print("\n\r");
print("====================================");
print("reshape(row,column)生成多行多列表array对象");
print("====================================");
arr2 = np.arange(15).reshape(3, 5);
print(arr2);
print(arr2.shape);







genfromtxt

#getfromtxt()方法读取csv格式内容

#SciPy练习在项目中
