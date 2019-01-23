# -*- coding: utf-8 -*-
# !/usr/bin/python
'''
模块               功能
scipy.cluster     矢量量化 / K-均值
scipy.constants   物理和数学常数
scipy.fftpack     傅里叶变换
scipy.integrate   积分程序
scipy.interpolate 插值
scipy.io          数据输入输出
scipy.linalg      线性代数程序
scipy.ndimage     n维图像包
scipy.odr         正交距离回归
scipy.optimize    优化
scipy.signal      信号处理
scipy.sparse      稀疏矩阵
scipy.spatial     空间数据结构和算法
scipy.special     任何特殊数学函数
scipy.stats       统计
'''
import numpy as np;
from scipy import io as spio;
a = np.ones((3, 3));
print(a);
spio.savemat('file.mat', {'a':a}); #保存到file文件中
data = spio.loadmat('file.mat', struct_as_record=True);
print(data);















