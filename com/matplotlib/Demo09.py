# coding=utf-8

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

print("==========================================================")
print("contour等高线图");
print("==========================================================")

def get_height(x, y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2);




n = 256;
x = np.linspace(-3, 3, n);
y = np.linspace(-3, 3, n);
X, Y = np.meshgrid(x, y);

plt.figure(figsize=(14, 8));

#横坐标，纵坐标，高度，透明度， cmap是颜色对应表
#等高线的填充颜色
plt.contourf(X, Y, get_height(X, Y), 16, alpah=0.7, cmap=plt.cm.hot);

#这里是等高线的线
#C = plt.contour(X, Y, get_height(X, Y), 16, color="black", linewidth=0.5);
C = plt.contour(X, Y, get_height(X, Y), 16, color='black', linewidth=.5)

# adding label
plt.clabel(C, inline=True, fontsize=16);

plt.xticks(());
plt.yticks(());


plt.show();




