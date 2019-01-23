import numpy as np;
from scipy import io as spio;
from scipy import special as special;
from scipy import linalg;
from scipy import optimize;
import matplotlib.pyplot as plt;
from scipy import signal;

print("\n\r");
print("====================================");
print("信号处理：scipy.signal");
print("====================================");
#scipy.signal.detrend()：移除信号的线性趋势

t = np.linspace(0, 5, 100);
x = t + np.random.normal(size=100);
import pylab as pl;
pl.plot(t, x, linewidth=3);

pl.plot(t, signal.detrend(x), linewidth=3)
pl.show();

#scipy.signal.resample():使用FFT重采样n个点
t = np.linspace(0, 5, 100);
x = np.sin(t);
pl.plot(t, x, linewidth=3);
pl.plot(t[::2], signal.resample(x, 50), 'ko');
pl.show();







