# -*- coding: utf-8 -*-
#!/usr/bin/python

from __future__ import print_function

import math


#加载必要的库
from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

#错误打印级别
tf.logging.set_verbosity(tf.logging.ERROR)
#pandas打印数据的最大行数
pd.options.display.max_rows = 10
#pandas float格式化
pd.options.display.float_format = '{:.1f}'.format

#加载数据集
#california_housing_dataframe = pd.read_csv("https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",");
california_housing_dataframe = pd.read_csv("../../resource/california_housing_train.csv", sep=",");
#print (california_housing_dataframe);

#对加载数据进行随机处理,会打乱以前的排序顺序
california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index));
#print(california_housing_dataframe['median_house_value']);


#对数据中房子价格进行除1000计算(median_house_value)
california_housing_dataframe["median_house_value"] /= 1000.0;
#print(california_housing_dataframe['median_house_value']);


#检查数据
california_housing_dataframe.describe();
#print ("california_housing_dataframe=>", california_housing_dataframe);



########################################
#构建第一个模型
########################################



#第1步，定义特征并配置特征列
#定义输入特性:total_rooms(总计房间数)
my_feature = california_housing_dataframe[["total_rooms"]];
#print ("======== my_feature ========");
#print (my_feature);
'''
            total_rooms
12007       1540.0
'''

#为total_rooms配置数值特性列。
feature_columns = [tf.feature_column.numeric_column("total_rooms")]
print ("=======feature_columns ========");
print (feature_columns);
#[_NumericColumn(key='total_rooms', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None)]



#第2步 定义目标
# 定义目标，将合计房子价格做为目标
targets = california_housing_dataframe["median_house_value"]
print ("====== targets ======");
print (targets);
'''
4810    172.2
16858   100.0
4575    500.0
13297   291.9
2830    251.3
'''


#第3步 配置LinearRegressor
#使用梯度下降法作为训练模型的优化器。

#来进行梯度下降法（内部实现是小批量随机梯度下降法）训练模型
#learning_rate为学习率为0.0000001
my_optimizer=  tf.train.GradientDescentOptimizer(learning_rate=0.0000001)

#来进行裁剪，确保数值稳定性以及防止梯度爆炸。
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)


# 使用我们的特性列和优化器配置线性回归模型。
# 为梯度下降设置0.0000001的学习率。
linear_regressor = tf.estimator.LinearRegressor(
    feature_columns=feature_columns, #特征列,为total_rooms
    optimizer=my_optimizer #传入用梯度下降法作为训练模型的优化器
)




# 第4步 定义输入函数
"""
训练一个特征的线性回归模型
    @:param  features<特征数据，目前为数据集中的total_rooms>
    @:param  targets<目标数据，目前为数据集中的median_house_value>
    @:param  batch_size<传递给模型的批次大小值>
    @:param  shuffle<True/Flash,是否洗牌数据>
    @:param  num_epochs<重复数据的epoch数,无限重复>
    @:return 下一个数据批处理的元组(features<特性>, labels<标签>)
    例: ({'total_rooms': <tf.Tensor 'IteratorGetNext:0' shape=(?,) dtype=float64>}, <tf.Tensor 'IteratorGetNext:1' shape=(?,) dtype=float64>)
"""
def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):

    # 将pandas数据转换成np数组。
    features = {key: np.array(value) for key, value in dict(features).items()}

    # 构建数据集，并配置批处理/重复。
    ds = Dataset.from_tensor_slices((features, targets))  # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)


    #如果指定洗牌数据。
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    #返回下一批数据。
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels

#tempDate = my_input_fn(my_feature, targets);
#print ("=========== tempDate ==========");
#print (tempDate);
#({'total_rooms': <tf.Tensor 'IteratorGetNext:0' shape=(?,) dtype=float64>}, <tf.Tensor 'IteratorGetNext:1' shape=(?,) dtype=float64>)




#第5步 训练模型
linear_regressor.train(input_fn = lambda:my_input_fn(my_feature, targets), steps=100);




#第6步 评估模型
#为预测创建一个输入函数。
#注意:因为我们对每个例子只做了一个预测，所以我们没有
#需要在这里重复或洗牌数据
prediction_input_fn =lambda: my_input_fn(my_feature, targets, num_epochs=1, shuffle=False)


# 在linear_regressor上调用predict()来进行预测。
predictions = linear_regressor.predict(input_fn=prediction_input_fn)
#print("========= predictions =========");
#print (predictions);
#<generator object Estimator.predict at 0x1c2a9bd9e8>


# 将预测格式化为一个NumPy数组，这样我们就可以计算错误度量。
predictions = np.array([item['predictions'][0] for item in predictions])
print ("========= predictions =========");
print (predictions);
#[0.13999903 0.06049961 0.20864853 ... 0.06594957 0.05029968 0.04709971]


# 打印平均平方误差和根平均平方误差
mean_squared_error = metrics.mean_squared_error(predictions, targets)
print ("mean_squared_error======>", mean_squared_error);
root_mean_squared_error = math.sqrt(mean_squared_error)
print("平均平方误差(关于训练数据): %0.3f" % mean_squared_error)
print("均方根误差(关于训练数据): %0.3f" % root_mean_squared_error)

min_house_value = california_housing_dataframe["median_house_value"].min()
max_house_value = california_housing_dataframe["median_house_value"].max()
min_max_difference = max_house_value - min_house_value

print("最小值。房屋价值中值: %0.3f" % min_house_value)
print("Max。房屋价值中位数: %0.3f" % max_house_value)
print("最小值和最大值的区别.: %0.3f" % min_max_difference)
print("均方根误差: %0.3f" % root_mean_squared_error)




#绘制散点图
calibration_data = pd.DataFrame()
calibration_data["predictions"] = pd.Series(predictions)
calibration_data["targets"] = pd.Series(targets)
calibration_data.describe();


#获取预测样式信息
sample = california_housing_dataframe.sample(n=300)
# 获取最小和最大total_rooms值。
x_0 = sample["total_rooms"].min();
x_1 = sample["total_rooms"].max();
#X坐标展示total_rooms值，



# 检索训练过程中产生的最终重量和偏差
# linear_regressor是训练方法
# 重量
weight = linear_regressor.get_variable_value('linear/linear_model/total_rooms/weights')[0]
#print ("========= weight =========");
#print (weight);
#[5.e-05]
#偏差
bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')
#print ("======= bias ========");
#print (bias);
#[2.5979848e-08]


# 获取最小和最大total_rooms值的预计median_house_values
# y坐标的最小值是: weight(重量) * x_0(total_rooms最小值) + bias(偏差)
y_0 = weight * x_0 + bias
# y坐标的最大值是: weight(重量) * x_1(total_rooms最大值) + bias(偏差)
y_1 = weight * x_1 + bias


# 绘制从(x_0, y_0)到(x_1, y_1)的回归线。
plt.plot([x_0, x_1], [y_0, y_1], c='r')


# 标记图形轴。
plt.ylabel("Median_house_value")
plt.xlabel("Total_rooms")


# 从我们的数据样本绘制散点图。
plt.scatter(sample["total_rooms"], sample["median_house_value"])

#显示图形
plt.show()


















