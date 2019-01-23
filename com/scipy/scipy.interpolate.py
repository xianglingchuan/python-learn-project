import numpy as np;
from scipy import io as spio;
from scipy import special as special;
from scipy import linalg;
from scipy import optimize;
import matplotlib.pyplot as plt;

print("\n\r");
print("====================================");
print("插值：scipy.interpolate");
print("====================================");

#通过想象接近正弦函数的实验数据：
measured_time = np.linspace(0, 1, 10);
noise = (np.random.random(10)*2 -1) * 1e-1;
measures = np.sin(2 * np.pi * measured_time) + noise;
print("measures====>", measures);

#scipy.interpolate.interp1d类会构建线性插值函数
from scipy.interpolate import  interp1d;
linear_interp = interp1d(measured_time, measures);
print("linear_interp====>", linear_interp);

#然后scipy.interpolate.linear_interp实例需要被用来求得感兴趣时间点的值
computed_time = np.linspace(0, 1, 50);
linear_results = linear_interp(computed_time);
print("linear_results===>", linear_results);

#三次插值也能通过提供可选关键字参数kind来选择
cubic_interp = interp1d(measured_time, measures, kind='cubic');
cubic_results = cubic_interp(computed_time);
print("cubic_results===>", cubic_results);





















