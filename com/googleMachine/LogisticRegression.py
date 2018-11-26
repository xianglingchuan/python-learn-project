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

逻辑回归 (Logistic Regression)
    逻辑回归会生成一个介于 0 到 1 之间（不包括 0 和 1）的概率值，而不是确切地预测结果是 0 还是 1。
    以用于检测垃圾邮件的逻辑回归模型为例。如果此模型推断某一特定电子邮件的值为 0.932，则意味着该电子邮件是垃圾邮件的概率为 93.2%。
    更准确地说，这意味着在无限训练样本的极限情况下，模型预测其值为 0.932 的这组样本实际上有 93.2% 是垃圾邮件，其余的 6.8% 不是垃圾邮件。
"""



