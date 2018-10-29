# coding=utf-8

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

print("==========================================================")
print("同时绘制多条曲线");
print("==========================================================")


x = np.linspace(-1, 1, 50);
y1 = 2 * x + 1;
y2 = 2 **x + 1;

#第一个参数表示的是编号，第二个表示的是图表的长宽
plt.figure(num=3, figsize=(8, 5));

#当我们需要在画板中绘制两条线的时候，可以使用下面的方法:
plt.plot(x, y2);
plt.plot(x, y1,
         color='red',   #线颜色
         linewidth=1.0, #线宽
         linestyle='--' #线样式
         )
#设备轴线的lable(标签)
plt.xlabel("I am x");
plt.ylabel("I am y");


#设置取值参数范围
plt.xlim((-1, 2)); #x参数范围
plt.ylim((1, 3)); #y参数范围

#设置点的位置
new_ticks = np.linspace(-1, 2, 5);
plt.xticks(new_ticks);
# 为点的位置设置对应的文字。
# 第一个参数是点的位置，第二个参数是点的文字提示。
plt.yticks([-2, -1.8, -1, 1.22, 3],
          [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$readly\ good$'])
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

plt.show();






plt.show();







