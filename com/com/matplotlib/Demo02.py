# coding=utf-8

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

print("==========================================================")
print("显示多个图像");
print("==========================================================")

#多个figure
x = np.linspace(-1, 1, 50);
y1 = 2 * x + 1;
y2 = 2 **x + 1;

#使用figure()函数重新申请一个figure对象
#注意，每次调用figure的时候都会重新申请一个figure对象
plt.figure();
#第一个是横坐标的值，第二个是纵坐标的值
plt.plot(x, y1);


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




plt.show();







