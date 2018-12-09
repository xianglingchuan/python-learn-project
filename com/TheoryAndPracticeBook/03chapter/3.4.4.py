# -*- coding: utf-8 -*-
# !/usr/bin/python

print("============= 明可夫斯基距离 ===============");
import numpy as np;
vec1 = np.mat([1, 2, 3, 4]);
vec2 = np.mat([5, 6, 7, 8]);

#方法一、根据scipy库求解
from scipy.spatial.distance import pdist;
Vec = np.vstack([vec1, vec2]);
dist1 = pdist(Vec, 'minkowski', p=1);
print ("当p=1时就是曼哈顿距离，结果是:", str(dist1));

#方法二、根据公式求解二
dist2 = np.sqrt(np.sum(np.square(vec1-vec2)));
print ("当p=2时就是欧式距离，结果是:", str(dist2));

from numpy import *;
#方法三、根据公式求解, p=1
dist3 = sum(abs(vec1- vec2));
print ("当p=1时就是曼哈顿距离，结果是:", str(dist3));

#方法四、根据公式求解,p=2
dist4 = sqrt((vec1 - vec2) * (vec1-vec2).T);
print ("当p=2时就是欧式距离，结果是:", str(dist4));



