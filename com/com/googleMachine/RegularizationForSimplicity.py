# -*- coding: utf-8 -*-
# !/usr/bin/python


from __future__ import print_function

import math

from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

"""
任务 1：按原样运行具有所有指定向量积特征的模型。模型与数据拟合的方式是否有任何意外？ 问题是什么？
    出乎意料的是，该模型的决策边界看起来有些不可思议。尤其是，左上方的某个区域朝着蓝色的方向演变，虽然数据中对其没有明显的支持。
    请注意从 INPUT 到 OUTPUT 的 5 条线的相对厚度，这些线表示 5 个特征的相对权重。从 X1 和 X2 发出的线比从自特征组合发出的线厚得多。因此，与常规（未组合）的特征相比，特征组合对模型的贡献要小得多。


任务 2：尝试移除各种向量积特征以提高性能（虽然影响甚微）。为什么移除特征可以提高性能？
    移除所有特征组合可获得更稳定的模型（左上角不再有过拟合的曲线边界），并可使测试损失收敛。
    经过 1000 次迭代之后，测试损失的值应该略低于使用特征组合时的相应值（虽然您的结果可能会因数据集而略有不同）。
    本练习中的数据基本上是线性数据加噪点。 如果我们使用的模型太复杂（如组合过多），该模型便有机会与训练数据中的噪点拟合，但这样往往会降低该模型在测试数据方面的性能。

"""



