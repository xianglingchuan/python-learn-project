import numpy as np;
from scipy import io as spio;
from scipy import special as special;
from scipy import linalg;
from scipy import optimize;
import matplotlib.pyplot as plt;

print("\n\r");
print("====================================");
print("统计和随机数：scipy.stats");
print("====================================");

print("=== 直方图和概率密度函数 ===");
a = np.random.normal(size=1000);
bins = np.arange(-4, 5);
print("bins====>", bins);
histogram = np.histogram(a, bins=bins, normed=True);
bins = 0.5*(bins[1:] + bins[:-1]);
print("bins====>", bins);

from scipy import stats;
b = stats.norm.pdf(bins); #norm是正态分布
#plt.plot(bins, histogram);
print("b======>", b);
plt.plot(bins, b);
#plt.show();

loc, std = stats.norm.fit(a);
print("loc====>", loc);
print("std====>", std);

print("=== 百分位 ===");
print(np.median(a));

#它也被叫作50百分位点，因为有50%的观测值在它之下：
print(stats.scoreatpercentile(a, 50));

#同样我们可以计算百分之九十百分点
print(stats.scoreatpercentile(a, 90));

print("=== 统计检测 ===");
a = np.random.normal(0, 1, size=100);
b = np.random.normal(1, 1, size=10);
print("a=====>",a);
print("b=====>",b);
var = stats.ttest_ind(a, b);
print(var);
#输出结果由以下部分组成：
#T统计量：它是这么一种标志，与不同两个随机过程之间成比例并且幅度和差异的显著程度有关^3。
#p值：两个过程相同的概率。如果接近1,这两个过程是几乎完全相同的。越靠近零，两个过程越可能有不同的均值。










