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

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

#加载数据
california_housing_dataframe = pd.read_csv("../../resource/california_housing_train.csv", sep=",")
california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))


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
  processed_features["rooms_per_person"] = (
    california_housing_dataframe["total_rooms"] /
    california_housing_dataframe["population"])
  return processed_features


"""
对目录数据进行处理
    @:param  california_housing_dataframe<DataFrame希望包含数据来自加州住房数据集>
    @:return 一个DataFrame，它包含要用于模型的目标，包括合成功能
"""
def preprocess_targets(california_housing_dataframe):
  output_targets = pd.DataFrame()

  #创建一个布尔分类特征，表示是否median_house_value高于设置的阈值。
  output_targets["median_house_value_is_high"] = (
    california_housing_dataframe["median_house_value"] > 265000).astype(float)
  return output_targets



# 选择数据12000条做为训练数据
training_examples = preprocess_features(california_housing_dataframe.head(12000))
training_targets = preprocess_targets(california_housing_dataframe.head(12000))

# 选择5000条做为验证数据
validation_examples = preprocess_features(california_housing_dataframe.tail(5000))
validation_targets = preprocess_targets(california_housing_dataframe.tail(5000))

# Double-check that we've done the right thing.
print("Training examples summary:")
display.display(training_examples.describe())
print("Validation examples summary:")
display.display(validation_examples.describe())

print("Training targets summary:")
display.display(training_targets.describe())
print("Validation targets summary:")
display.display(validation_targets.describe())


"""
构造张量流特征列
    @:param  input_features<要使用的数字输入特性的名称>
    @:return 一组特性列
"""
def construct_feature_columns(input_features):
  return set([tf.feature_column.numeric_column(my_feature)
              for my_feature in input_features])


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

    # 构建数据集，并配置批处理/重复
    ds = Dataset.from_tensor_slices((features, targets))  # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)

    # 如果指定洗牌数据
    if shuffle:
        ds = ds.shuffle(10000)

        # 返回下一批数据
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels



"""
训练一个多元特征的线性回归模型
除了培训，这个功能还可以打印培训进度信息，以及随着时间的推移，培训和验证的损失
    @:param  learning_rate<一个“浮点数”,学习速率>
    @:param  steps<训练步骤的总数>
    @:param  batch_size<传递给模型的批次大小值>
    @:param  training_examples<DataFrame 用作训练的输入特性>
    @:param  training_targets<DataFrame 用作训练的目标>
    @:param  validation_examples<DataFrame 用作验证的输入特性>
    @:param  validation_targets<DataFrame 用作验证的目标>
    @:return 一组特性列
"""
def train_linear_regressor_model(
        learning_rate,
        steps,
        batch_size,
        training_examples,
        training_targets,
        validation_examples,
        validation_targets):


    periods = 10
    steps_per_period = steps / periods

    # 创建一个线性回归对象, learning_rate=学习率
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    ##来进行裁剪，确保数值稳定性以及防止梯度爆炸
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
    linear_regressor = tf.estimator.LinearRegressor(
        feature_columns=construct_feature_columns(training_examples), #特征列
        optimizer=my_optimizer #线性回归对象
    )

    # 创建输入功能
    training_input_fn = lambda: my_input_fn(training_examples,
                                            training_targets["median_house_value_is_high"],
                                            batch_size=batch_size)
    # 创建预测功能
    predict_training_input_fn = lambda: my_input_fn(training_examples,
                                                    training_targets["median_house_value_is_high"],
                                                    num_epochs=1,
                                                    shuffle=False)
    # 创建预测校验功能
    predict_validation_input_fn = lambda: my_input_fn(validation_examples,
                                                      validation_targets["median_house_value_is_high"],
                                                      num_epochs=1,
                                                      shuffle=False)


    # 训练模型，但是要在循环中这样做，这样我们可以定期评估损失度量
    print("Training model...")
    print("RMSE (on training data):")
    training_rmse = []
    validation_rmse = []
    for period in range(0, periods):
        # 从先验状态开始训练模型
        linear_regressor.train(
            input_fn=training_input_fn,
            steps=steps_per_period
        )

        # 计算一下预测
        training_predictions = linear_regressor.predict(input_fn=predict_training_input_fn)
        training_predictions = np.array([item['predictions'][0] for item in training_predictions])

        # 计算一下校验
        validation_predictions = linear_regressor.predict(input_fn=predict_validation_input_fn)
        validation_predictions = np.array([item['predictions'][0] for item in validation_predictions])

        # 计算培训和验证损失
        training_root_mean_squared_error = math.sqrt(
            metrics.mean_squared_error(training_predictions, training_targets))
        validation_root_mean_squared_error = math.sqrt(
            metrics.mean_squared_error(validation_predictions, validation_targets))
        # 打印当前的损失
        print("  period %02d : %0.2f" % (period, training_root_mean_squared_error))
        # 将这段时间的损失指标添加到我们的列表中
        training_rmse.append(training_root_mean_squared_error)
        validation_rmse.append(validation_root_mean_squared_error)
    print("Model training finished.")




    #plt.hist(validation_predictions)



    #输出一段时间内损失指标的图表
    plt.ylabel("RMSE")
    plt.xlabel("Periods")
    plt.title("Root Mean Squared Error vs. Periods")
    plt.tight_layout()
    plt.plot(training_rmse, label="training")
    plt.plot(validation_rmse, label="validation")
    plt.legend()
    plt.show();

    return linear_regressor



linear_regressor = train_linear_regressor_model(
    learning_rate=0.000001,
    steps=200,
    batch_size=20,
    training_examples=training_examples,
    training_targets=training_targets,
    validation_examples=validation_examples,
    validation_targets=validation_targets)


