import numpy as np;
from scipy import io as spio;
from scipy import special as special;
import matplotlib.pyplot as plt;

print("\n\r");
print("====================================");
print("快速傅里叶变换：scipy.fftpack");
print("====================================");

time_step = 0.02;
period = 5;
time_vec = np.arange(0, 20, time_step)
print(time_vec);
sig = np.sin(2 * np.pi / period * time_vec) + 0.5 * np.random.randn(time_vec.size)
print("sig======>", sig);

sample_freq = sig;
pidxs = np.where(sample_freq > 0);
print("pidxs======>", pidxs);
freqs = sample_freq[pidxs]
print("freqs======>", freqs);
sig_fft = [0.4, 0.9];
power = np.abs(sample_freq)[pidxs]
print("power======>", power);


#信号频率可以这样被找到：
freq = freqs[power.argmax()]
print("freq=====>", freq);
result = np.allclose(freq, 1./period)
print(result);

#现在高频噪声将被从傅里叶变换信号中移除：
#result = sig_fft[np.abs(sample_freq) > freq] = 0;

plt.figure()
plt.plot(time_vec, sig)

print("==========time_vec============");
print(time_vec);
print("======================");

print("==========sample_freq============");
print(sample_freq);
print("======================");

plt.plot(time_vec, sample_freq, linewidth=3)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()





# In [40]: time_step = 0.02
# In [41]: period = 5
# In [42]: time_vec = np.arange(0, 20, time_step)
# In [43]: sig = np.sin(2 * np.pi / period * time_vec) + \
#    ....: 0.5 * np.random.randn(time_vec.size)


