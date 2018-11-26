# -- coding: utf-8 --
#############################
#Array(数组）
#############################
   #rank--数组的维数
import  numpy as np;
a = np.array([1,2,3]);

print (a)

#显示数据类型
print (type(a))
#显示数据的形状，也就是几维数组
print (a.shape)
a = a.reshape(1,-1)
print (a.shape)

a = np.array([1,2,3,4,5,6])
print (a.shape)
a = a.reshape(2,-1)
print (a.shape)
print (a)

a = a.reshape((-1,2));
print (a)
print(a.shape);

#直接替换指定索引值内容
print ("###############################");
print ("直接替换指定索引值内容");
print ("###############################");
print (a[2,0]);
a[2,0] = 55;
print (a)

#zeros(创建值为0的多维数组)
print ("###############################");
print ("zeros(创建值为0的多维数组)");
print ("###############################");
a = np.zeros((3,3));
print (a);

#ones(创建值为1的多维数组)
print ("###############################");
print ("ones(创建值为1的多维数组)");
print ("###############################");
a = np.ones((4,4));
print (a);

#full(创建值为指定数值的多维数组)
print ("###############################");
print ("full(创建值为指定数值的多维数组)");
print ("###############################");
a = np.full((2,3), 55);
print (a)

#eye(创建指定维度的对角值为1的数组)
print ("###############################");
print ("eye(创建指定维度的对角值为1的数组)");
print ("###############################");
a = np.eye(4);
print (a);

#random.random(创建为随机数的多维数组0-1之间随机)
print ("###############################");
print ("random.random(创建为随机数的多维数组0-1之间随机)");
print ("###############################");
a  = np.random.random((3,4));
print (a)











