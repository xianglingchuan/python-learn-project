import numpy as np;
from scipy import io as spio;
from scipy import special as special;
from scipy import linalg;
from scipy import optimize;
import matplotlib.pyplot as plt;

print("\n\r");
print("====================================");
print("优化和拟合：scipy.optimize");
print("====================================");
def f(x):
    return x**2 + 10 * np.sin(x)
x = np.arange(-10, 10, 0.1);
print(plt.plot(x, f(x)));
#plt.show();
#找到这个函数最小值一般而有效的方法是从初始点使用梯度下降法。BFGS算法^1是做这个的好方法：

result = optimize.fmin_bfgs(f, 0);
print(result);

result = optimize.fmin_bfgs(f, 3, disp=0);
print(result);

grid = (-10, 10, 0.1);
xmin_global = optimize.brute(f, (grid,));
print("xmin_global=====>", xmin_global);

#为了找到局部最小，我们把变量限制在(0, 10)之间，使用scipy.optimize.fminbound():
xmin_local = optimize.fminbound(f, 0, 10);
print("xmin_local=====>",xmin_local);

print("=== 找到标量函数的根 ===");
root = optimize.fsolve(f, 1);
print("root====>", root);

root = optimize.fsolve(f, -2.5);
print("root=====>", root);

print("=== 曲线拟合 ===");
xdata = np.linspace(-10, 10, num=20);
ydata = f(xdata) + np.random.randn(xdata.size);

def f2(x, a, b):
    return a*x**2 + b*np.sin(x);
guess = [2, 2];
params, params_covariance = optimize.curve_fit(f2, xdata, ydata, guess);
print("params======>", params);











