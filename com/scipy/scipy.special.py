import numpy as np;
from scipy import io as spio;
from scipy import special as special;

print("\n\r");
print("====================================");
print("特殊函数：scipy.special");
print("====================================");

print("=== 贝塞尔函数，如scipy.special.jn() (整数n阶贝塞尔函数) ===");
data = special.jn(22, 33);
print(data);

arrA = [11, 22, 33];
arrB = [44, 55, 66];
data = special.jn(arrA, arrB);
print(data);


print("=== 椭圆函数: scipy.special.ellipj() (雅可比椭圆函数，……) ===");
x1 = [0.4, 0.5, 0.3];
x2 = [0.6, 0.7, 0.8];
#x1, x2, out1=None, out2=None, out3=None, out4=None
data = special.ellipj(x1, x2);
print(data);



print("=== 伽马函数：scipy.special.gamma() ===");
#还要注意scipy.special.gammaln,这个函数给出对数坐标的伽马函数，因此有更高的数值精度
x = [0.4, 0.6, 0.8];
data = special.gammaln(x)
print(data);