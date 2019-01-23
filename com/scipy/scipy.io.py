# -*- coding: utf-8 -*-
# !/usr/bin/python


import numpy as np;
from scipy import io as spio;

print("\n\r");
print("====================================");
print("文件输入/输出:scipy.io");
print("====================================");

print("=== 导入和保存matlab文件");
a = np.ones((3, 3));
print(a);
spio.savemat('file.mat', {'a':a}); #保存到file文件中
data = spio.loadmat('file.mat', struct_as_record=True);
print(data);

print("=== 读取图片(scipy.misc.imread) ====");
from scipy import misc;
imgFile = "../../resource/scipy/file.jpg";
imgData = misc.imread(imgFile);
print(imgData);

print("=== 读取图片(matplotlib.pyplot.imread) ====");
import matplotlib.pyplot as plt;
imgData = plt.imread(imgFile);
print(imgData);



print("=== 载入txt文件(numpy.loadtxt()/numpy.savetxt()) ===")
a = np.random.rand(5,5);
print(a);
#保存数组到文件中
np.savetxt("file.txt", a, fmt='%0.8f');
#从txt文件中读取数据
b = np.loadtxt("file.txt", dtype=np.float32);
print("从txt文件中读取数据内容是:");
print(b);


print("=== 智能导入文本/csv文件(numpy.genfromtxt()/numpy.recfromcsv()) ===")
#稍后


print("=== 高速,有效率但numpy特有的二进制格式(numpy.save()/numpy.load()) ===")
#写入内容
#np.save("file2.txt", "二进制格式内容");
np.save("file2.txt", a);
#读取内容
data = np.load("file2.txt.npy", mmap_mode='r+');
print(data);




