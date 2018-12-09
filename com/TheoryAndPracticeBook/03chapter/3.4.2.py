# -*- coding: utf-8 -*-
# !/usr/bin/python

print("============= 欧氏距离 ===============");
import numpy as np;
vec1 = np.mat([1, 2, 3, 4]);
vec2 = np.mat([5, 6, 7, 8]);

#方法一、根据公式求解
dist1 = np.sqrt(np.sum(np.square(vec1-vec2)));
print ("欧氏距离测试结果是:", str(dist1));

#方法二、根据scipy为求解
from scipy.spatial.distance import pdist;
Vec = np.vstack([vec1, vec2]);
dist2 = pdist(Vec);
print ("欧氏距离测试结果是:", str(dist2));

Vec2 = np.vstack([vec2, vec1]);
dist3 = pdist(Vec2);
print ("欧氏距离测试结果是:", str(dist3));


#方法三、根据公式求解
from numpy import *;
dist4 = sqrt((vec1-vec2)*(vec1-vec2).T);
print ("欧氏距离测试结果是:", str(dist4));


