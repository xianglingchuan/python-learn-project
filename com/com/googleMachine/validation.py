# -*- coding: utf-8 -*-
#!/usr/bin/python

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

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

#加载数据文件
california_housing_dataframe = pd.read_csv("../../../resource/california_housing_train.csv", sep=",");


#对数据正确的随机处理方法，如果没有会对训练结果产生影响
#注意注释、或不注释之间的区别
california_housing_dataframe = california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index))


"""
从加利福尼亚住房数据集准备输入特性
    @:param  california_housing_dataframe<DataFrame希望包含数据来自加州住房数据集>
    @:return 一个DataFrame，它包含要用于模型的特性，包括合成功能
"""
def preprocess_features(california_housing_dataframe):

  selected_features = california_housing_dataframe[
    ["latitude",
     "longitude",
     "housing_median_age",
     "total_rooms",
     "total_bedrooms",
     "population",
     "households",
     "median_income"]]
  processed_features = selected_features.copy()

  # 创建一个合成特性
  processed_features["rooms_per_person"] = ( california_housing_dataframe["total_rooms"] /
    california_housing_dataframe["population"])
  return processed_features



"""
准备目标特性(例如加州住房数据集
    @:param  california_housing_dataframe<DataFrame希望包含数据来自加州住房数据集>
    @:return 包含目标特性的DataFrame
"""
def preprocess_targets(california_housing_dataframe):
  output_targets = pd.DataFrame()
  #以几千美元为单位来衡量这个目标
  output_targets["median_house_value"] = (
    california_housing_dataframe["median_house_value"] / 1000.0)
  return output_targets



#对于训练训，我们从共17000个样本中选择前12000样本
#特征数据
training_examples = preprocess_features(california_housing_dataframe.head(12000))
training_examples.describe();
#目标数据
training_targets = preprocess_targets(california_housing_dataframe.head(12000))
training_targets.describe()


#对于验证集,从共17000个样本中选择后5000个样本
#特征数据
validation_examples = preprocess_features(california_housing_dataframe.tail(5000))
validation_examples.describe();
#目标数据
validation_targets = preprocess_targets(california_housing_dataframe.tail(5000))
validation_targets.describe();



#任务 2：绘制纬度/经度与房屋价值中位数的曲线图
plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
ax.set_title("Validation Data")

ax.set_autoscaley_on(False)
ax.set_ylim([32, 43])
ax.set_autoscalex_on(False)
ax.set_xlim([-126, -112])
plt.scatter(validation_examples["longitude"],
            validation_examples["latitude"],
            cmap="coolwarm",
            c=validation_targets["median_house_value"] / validation_targets["median_house_value"].max())

ax = plt.subplot(1,2,2)
ax.set_title("Training Data")

ax.set_autoscaley_on(False)
ax.set_ylim([32, 43])
ax.set_autoscalex_on(False)
ax.set_xlim([-126, -112])
plt.scatter(training_examples["longitude"],
            training_examples["latitude"],
            cmap="coolwarm",
            c=training_targets["median_house_value"] / training_targets["median_house_value"].max())
_ = plt.plot()
plt.show();