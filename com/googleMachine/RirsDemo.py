
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


#文章地址
#https://vimsky.com/article/3637.html


import os
from six.moves.urllib.request import urlopen

import numpy as np
import tensorflow as tf

# Data sets
IRIS_TRAINING = "iris_training.csv"
IRIS_TRAINING_URL = "http://download.tensorflow.org/data/iris_training.csv"

IRIS_TEST = "iris_test.csv"
IRIS_TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

def main():
  # 如果培训和测试集不是本地存储的 下载它们。
  if not os.path.exists(IRIS_TRAINING):
    #读取内容
    raw = urlopen(IRIS_TRAINING_URL).read()
    with open(IRIS_TRAINING, "wb") as f:
      f.write(raw) #保存内容

  if not os.path.exists(IRIS_TEST):
    raw = urlopen(IRIS_TEST_URL).read()
    with open(IRIS_TEST, "wb") as f:
      f.write(raw)


  # 加载数据集
  #另载培训数据集
  training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=IRIS_TRAINING,
      target_dtype=np.int,
      features_dtype=np.float32)

  #加载测试数据集
  test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=IRIS_TEST,
      target_dtype=np.int,
      features_dtype=np.float32)

  # 指定所有特性都具有实值数据
  feature_columns = [tf.feature_column.numeric_column("x", shape=[4])]

  # 分别用10、20、10个单元构建3层DNN。
  classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                          hidden_units=[10, 20, 10],
                                          n_classes=3,
                                          model_dir="../../resource/Rirs/tmp/iris_model")


  # 定义培训输入
  # training_set.data==培训数据集
  # training_set.target==
  train_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(training_set.data)},
      y=np.array(training_set.target),
      num_epochs=None,
      shuffle=True)


  # 火车模型
  # 使用三层DNN训练数据，步长为2000次
  classifier.train(input_fn=train_input_fn, steps=2000)



  # 定义测试输入
  test_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(test_set.data)},
      y=np.array(test_set.target),
      num_epochs=1,
      shuffle=False)


  # 评估的准确性
  accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]
  print("\n测试的准确性: {0:f}\n".format(accuracy_score))

  # 对两个新花样本进行分类
  new_samples = np.array(
      [[6.4, 3.2, 4.5, 1.5],
       [5.8, 3.1, 5.0, 1.7]], dtype=np.float32)
  predict_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": new_samples},
      num_epochs=1,
      shuffle=False)

  predictions = list(classifier.predict(input_fn=predict_input_fn))
  predicted_classes = [p["classes"] for p in predictions]

  print("新样本，阶级预测:{}\n" .format(predicted_classes))

if __name__ == "__main__":
    main()
