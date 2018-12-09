# -*- coding: utf-8 -*-
# !/usr/bin/python

print("============= 切比雪夫距离 ===============");
import numpy as np;
vec1 = np.mat([1, 2, 3, 4]);
vec2 = np.mat([5, 6, 7, 8]);

#方法一、根据公式求解
dist1 = np.max(np.abs(vec1-vec2));
print ("切比雪夫距离测试结果是:"+str(dist1));

#方法二、根据scipy库求解
from scipy.spatial.distance import pdist;
Vec = np.vstack([vec1, vec2]);
dist2 = pdist(Vec, 'chebyshev', p=1);
print ("切比雪夫距离测试结果是:"+str(dist2));



