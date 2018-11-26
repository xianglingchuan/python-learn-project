# coding=utf-8

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

print("==========================================================")
print("多个figure,并加上特殊点注释");
print("==========================================================")


x = np.linspace(-1, 1, 50);
y1 = 2 * x + 1;
y2 = 2 **x + 1;

#第一个参数表示的是编号，第二个表示的是图表的长宽
plt.figure(figsize=(12, 8));

#当我们需要在画板中绘制两条线的时候，可以使用下面的方法:
plt.plot(x, y2);
plt.plot(x, y1,
         color='red',   #线颜色
         linewidth=1.0, #线宽
         linestyle='--' #线样式
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


#显示交叉点
x0 = 1;
y0 = 2*x0 + 1;
# s表示点的大小，默认rcParams['lines.markersize']**2
plt.scatter(x0, y0, s = 66, color='b');
#定义线的范围，X的范围是定值，y的范围是从y0到0的位置
# lw的意思是linewidth，线宽
plt.plot([x0, x0], [y0, 0], 'k-.', lw=2.5);


# 设置关键位置的提示信息
plt.annotate(r'$2x+1=%s$' %
             y0,
             xy=(x0, y0),
             xycoords='data',

             xytext=(+30, -30),
             textcoords='offset points',
             fontsize=16,  # 这里设置的是字体的大小
             # 这里设置的是箭头和箭头的弧度
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2')
            )

# 在figure中显示文字信息
# 可以使用\来输出特殊的字符\mu\ \sigma\ \alpha
plt.text(0, 3,
         r'$This\ is\ a\ good\ idea.\ \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':16,'color':'r'})


plt.show();







