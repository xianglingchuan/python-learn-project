# coding=utf-8

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

print("==========================================================")
print("散点图");
print("==========================================================")



n = 1024;
X = np.random.normal(0, 1, n);
Y = np.random.normal(0, 1, n);
T = np.arctan2(X, Y);
plt.scatter(np.arange(50), np.arange(50));

plt.xticks(());
plt.yticks(());



plt.show();







