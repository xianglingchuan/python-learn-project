# -*- coding: utf-8 -*-
# !/usr/bin/python

print("============= 余弦距离 ===============");
import numpy as np;
vec1 = [1, 3, 2, 4];
vec3 = [5, 6, 7, 8];
#方法一、根据公式求解
dist1 = np.dot(vec1,vec3)/(np.linalg.norm(vec1)*np.linalg.norm(vec3));
#print ("余弦距离测试结果是:"+dist1.tostring());
print ("余弦距离测试结果是:"+str(dist1));

#方法二、根据scipy库求解
from scipy.spatial.distance import pdist;
Vec = np.vstack([vec1, vec3]);
dist2 = 1-pdist(Vec, "cosine");
print("余弦距离测试结果是:"+str(dist2));

