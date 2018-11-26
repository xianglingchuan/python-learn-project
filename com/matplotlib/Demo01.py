# coding=utf-8

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

print("==========================================================")
print("简单演示");
print("==========================================================")

# 从[-1,1]中等距去50个数作为x的取值
x = np.linspace(-1, 1, 50);
print (x);

y = 2*x + 1;
# print (y);
#第一个是横坐标的值，第二个是纵坐标的值
# plt.plot(x, y);
# plt.show();


y = 2**x + 1;
plt.plot(x, y);
plt.show();




