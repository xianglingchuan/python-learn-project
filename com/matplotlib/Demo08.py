# coding=utf-8

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

print("==========================================================")
print("条形图");
print("==========================================================")



n = 12;

X = np.arange(n);

Y1 = (1- X/float(n)) * np.random.uniform(0.5, 1.0, n);
Y2 = (1- X/float(n)) * np.random.uniform(0.5, 1.0, n);

plt.figure(figsize=(12, 8));
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X,Y1):
    # ha: horizontal alignment水平方向
    # va: vertical alignment垂直方向
    plt.text(x, y+0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X,-Y2):
    # ha: horizontal alignment水平方向
    # va: vertical alignment垂直方向
    plt.text(x, y-0.05, '%.2f' % y, ha='center', va='top')

#定义范围和标签
plt.xlim(-.5, n);
plt.xticks(());

plt.ylim(-1.25, 1.25);
plt.yticks(());



plt.show();







