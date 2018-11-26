# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
降低损失

降低损失：迭代方法

降低损失 (Reducing Loss)：梯度下降法

降低损失 (Reducing Loss)：学习速率
    梯度下降法算法用梯度乘以一个称为学习速率（有时也称为步长）的标量，以确定下一个点的位置。
    例如，如果梯度大小为 2.5，学习速率为 0.01，则梯度下降法算法会选择距离前一个点 0.025 的位置作为下一个点。

降低损失 (Reducing Loss)：随机梯度下降法


概括而言，以下是在 tf.estimator 中实现的线性回归程序的格式：

# Set up a linear classifier.
# 建立一个线性分类器。
classifier = tf.estimator.LinearClassifier()

# Train the model on some example data.
# 在一些示例数据上训练模型。
classifier.train(input_fn=train_input_fn, steps=2000)

# Use it to predict.
# 用它来预测。
predictions = classifier.predict(input_fn=predict_input_fn)



'''
import tensorflow as tf










