# coding=utf-8

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

print("==========================================================")
print("tick能见度设备");
print("==========================================================")


x = np.linspace(-1, 1, 50);
y = 2 * x + 1;

#第一个参数表示的是编号，第二个表示的是图表的长宽
plt.figure(figsize=(12, 8));

#当我们需要在画板中绘制两条线的时候，可以使用下面的方法:
plt.plot(x, y,
         color='r',   #线颜色
         linewidth=10.0, #线宽
         alpha=0.5
         )

ax = plt.gca();

#将右边的上边的边框的颜色去掉
ax.spines['right'].set_color("none");
ax.spines['top'].set_color("none");
#绑定x轴和y轴
ax.xaxis.set_ticks_position("bottom");
ax.yaxis.set_ticks_position("left");
#定义x轴和y轴的位置
ax.spines['bottom'].set_position(("data",0));
ax.spines['left'].set_position(("data",0));

#可以使用tick设置透明度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12);
    label.set_bbox(dict(facecolor='y', edgecolor='None', alpha=0.7))




plt.show();







