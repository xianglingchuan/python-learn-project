# -*- coding: utf-8 -*-
# !/usr/bin/python

print("============= 汉明距离 ===============");
import numpy as np;
v1 = np.random.random(10) > 0.5;
v2 = np.random.random(10) > 0.5;

vec1 = np.asarray(v1, np.int32);
vec2 = np.asarray(v2, np.int32);

#方法一、根据公式求解
dist1 = np.mean(vec1 != vec2);
print ("汉明距离测试结果是:"+str(dist1));

# #方法二、根据scipy库求解
from scipy.spatial.distance import pdist;
Vec = np.vstack([vec1, vec2]);
dist2 = pdist(Vec, 'hamming');
print ("汉明距离测试结果是:"+str(dist2));