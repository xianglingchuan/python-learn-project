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

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

#加载数据集
#california_housing_dataframe = pd.read_csv("https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",");
california_housing_dataframe = pd.read_csv("../../resource/california_housing_train.csv", sep=",");

#对加载数据进行随机处理
california_housing_dataframe = california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index));

#对数据中房子价格进行除1000计算(median_house_value)
california_housing_dataframe["median_house_value"] /= 1000.0;

#检查数据
california_housing_dataframe.describe();
#print ("california_housing_dataframe=>", california_housing_dataframe);



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

    # 将pandas数据转换成np数组
    features = {key: np.array(value) for key, value in dict(features).items()}

    # 构建数据集，并配置批处理/重复
    ds = Dataset.from_tensor_slices((features, targets))  # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)


    #如果指定洗牌数据。
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    #返回下一批数据
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels





"""
训练一个特征的线性回归模型
    @:param  learning_rate<一个“浮点数”,学习速率>
    @:param  steps<训练步骤的总数>
    @:param  batch_size<传递给模型的批次大小值>
    @:param  input_feature<指定特征数据列字段>
    @:return void
"""
def train_model(learning_rate, steps, batch_size, input_feature="total_rooms"):

    periods = 10
    #将训练步骤除以10
    steps_per_period = steps / periods

    #定义特征列字段
    my_feature = input_feature
    #获取特征列数据
    my_feature_data = california_housing_dataframe[[my_feature]]

    #目标列字段
    my_label = "median_house_value"
    #目标列数据
    targets = california_housing_dataframe[my_label]


    # 创建特征列
    feature_columns = [tf.feature_column.numeric_column(my_feature)]

    # 创建输入功能
    # 创建训练输入功能
    training_input_fn = lambda: my_input_fn(my_feature_data, targets, batch_size=batch_size)
    # 创建评估输入功能
    prediction_input_fn = lambda: my_input_fn(my_feature_data, targets, num_epochs=1, shuffle=False)


    # 创建一个线性回归对象, learning_rate=学习率
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    ##来进行裁剪，确保数值稳定性以及防止梯度爆炸。
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
    linear_regressor = tf.estimator.LinearRegressor(
        feature_columns=feature_columns, #特征列
        optimizer=my_optimizer  #线性回归对象
    )

    #设置为绘制每个周期的模型线的状态
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    plt.title("逐周期学习线")
    plt.ylabel(my_label) #y坐标是median_house_value
    plt.xlabel(my_feature) #x坐标标记是total_rooms


    # 获取预测样式信息
    sample = california_housing_dataframe.sample(n=300)
    plt.scatter(sample[my_feature], sample[my_label])
    colors = [cm.coolwarm(x) for x in np.linspace(-1, 1, periods)]

    # 对模型进行训练，但要在循环中进行，这样我们才能定期评估损失指标。
    print("培训模式...")
    print("RMSE (在训练数据):")
    root_mean_squared_errors = []
    for period in range(0, periods):
        # 从先验状态开始训练模型
        linear_regressor.train(
            input_fn=training_input_fn, #训练数据函数
            steps=steps_per_period #训练的次数
        )

        # 休息一下，计算一下预测
        predictions = linear_regressor.predict(input_fn=prediction_input_fn)
        predictions = np.array([item['predictions'][0] for item in predictions])

        # 计算损失
        root_mean_squared_error = math.sqrt(metrics.mean_squared_error(predictions, targets))

        # 打印当前的损失
        print("  period %02d : %0.2f" % (period, root_mean_squared_error))

        # 将这段时间的损失指标添加到我们的列表中
        root_mean_squared_errors.append(root_mean_squared_error)

        # 最后，跟踪权重和偏差。
        # 使用一些数学方法来确保数据和线条画得整齐。
        # 将预测格式化为一个NumPy数组，这样我们就可以计算错误度量。
        y_extents = np.array([0, sample[my_label].max()])

        # 重量
        weight = linear_regressor.get_variable_value('linear/linear_model/%s/weights' % input_feature)[0]
        # 偏差
        bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')

        x_extents = (y_extents - bias) / weight
        x_extents = np.maximum(np.minimum(x_extents, sample[my_feature].max()),sample[my_feature].min())
        y_extents = weight * x_extents + bias
        plt.plot(x_extents, y_extents, color=colors[period])
        #plt.show(); #展示每次训练的结果
    print("Model training finished.")


    # 输出一段时间内损失指标的图表
    plt.subplot(1, 2, 2)
    plt.ylabel('RMSE')
    plt.xlabel('Periods')
    plt.title("均方根误差与周期")
    plt.tight_layout()
    plt.plot(root_mean_squared_errors)
    plt.show();

    # 输出带有校准数据的表
    calibration_data = pd.DataFrame()
    calibration_data["predictions"] = pd.Series(predictions)
    calibration_data["targets"] = pd.Series(targets)
    display.display(calibration_data.describe())

    print("Final RMSE (on training data): %0.2f" % root_mean_squared_error)

#train_model(0.0000001,100,1);
#Final RMSE (on training data): 237.42

#调整模型超参数，以降低损失和更符合目标分布。 约 5 分钟后，如果您无法让 RMSE 低于 180
#train_model(0.00002,500,5);
#Final RMSE (on training data): 167.53

#train_model(0.00002,100,1);
#Final RMSE (on training data): 214.42

#train_model(0.00001,500,5);
#Final RMSE (on training data): 187.39

#train_model(0.00001,100,1);
#Final RMSE (on training data): 225.63


#任务 2：尝试其他特征
#使用 `population` 特征替换 `total_rooms` 特征，看看能否取得更好的效果
#train_model(0.00002,500,5, "population");
#Final RMSE (on training data): 189.80

#train_model(0.00002,100,1, "population");
#Final RMSE (on training data): 225.63

#train_model(0.00001,500,5, "population");
#Final RMSE (on training data): 209.81


train_model(0.00001,100,1, "population");
#Final RMSE (on training data): 231.48


#train_model(0.00003,1000,10, "population");
#Final RMSE (on training data): 177.41