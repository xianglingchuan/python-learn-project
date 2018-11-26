# -- coding: utf-8 --

import  numpy as np;
#############################
#indexing
#############################
a = np.array([[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]])
print (a[-2:, 1:3])

print (a[-2:][1:3]);

print (a[1, -2])
print (a);
print a.shape;

b  = a[-2:, 1:3];
print b;
print b.shape;

b = a[2,1:3];
print b;
print b.shape;

b = a[1,2]
print b;
print b.shape;

print (a)
#给数组指定列加值
print ("###############################");
print ("给数组指定列加值");
print ("###############################");
a[np.arange(3), 1] += 10;
print (a);

print (np.arange(3))
print (np.arange(3,7))

#给数组指定列加值(第二种方法)
print ("###############################");
print ("给数组指定列加值(第二种方法)");
print ("###############################");
a[np.arange(3),[1,1,1]] += 10;
print a;

#给数组指定列加值(第三种)
print ("###############################");
print ("给数组指定列加值(第三种)");
print ("###############################");
a[[0,1,2], [1,1,1]] += 10;
print a;

#将值大于10的显示出来
print ("###############################");
print ("将值大于10的显示出来");
print ("###############################");
print a[a>10];

print a[a<10];


#############################
#元素的数据类型
#############################
a = np.array([1,2]);
print a;
print a.dtype;

a = np.array([1.1,2.2])
print a;
print a.dtype;

a = np.array([1, 2.2]);
print a;
print a.dtype;

a = np.array([1.1,2.6]);
print a;
a = np.array([1.1,2.6], dtype=np.int64)
print a;
print a.dtype;

a = np.array([1.1,2.6]);
b = np.array(a, dtype=np.int64);
print b;
print b.dtype;




#############################
#数学运算与常用函数
#############################
a = np.array([[1,2],
             [3,4]])


b = np.array([[5,6],
             [7,8]]);
print a+b;
print a-b;

print np.subtract(a,b);

print a*b;
print b/a;

print np.divide(a,b);

print np.sqrt(a)

print a;
b = np.array([[1,2,3],
             [4,5,6]])
print b;
#矩阵的乘法操作
print ("###############################");
print ("#矩阵的乘法操作");
print ("###############################");
print a.dot(b);





#############################
#常用函数
#############################
#sum 求和值
print ("###############################");
print ("sum 求和值");
print ("###############################");
a = np.array([[1,2],[3,4]]);
print a;
print np.sum(a);
print np.sum(a,axis=0);
print np.sum(a,axis=1);


##mean 求平均值
print ("###############################");
print ("mean 求平均值");
print ("###############################");
print np.mean(a);
print np.mean(a,axis=0);
print np.mean(a,axis=1);


##uniform 生成指定的随机数
print ("###############################");
print ("uniform 生成指定的随机数");
print ("###############################");
print np.random.uniform(3,4);
print np.random.uniform(1,100);


##tile 将一个数组重复指定次数
print ("###############################");
print ("tile 将一个数组重复指定次数");
print ("###############################");
print a;
print np.tile(a,(1,2));
print np.tile(a,(2,1));
print np.tile(a,(2,3));



##argsort 对数组进行排序 返回数组排序后的索引值
print ("###############################");
print ("argsort 对数组进行排序 返回数组排序后的索引值");
print ("###############################");
a = np.array([[3,6,4,11],
              [5,10,1,3]]);
print a.argsort();

print a.argsort(axis=0);


##矩阵转置
print ("###############################");
print ("矩阵转置");
print ("###############################");
print a;
print a.T;
print np.transpose(a);


##矩阵转置
print ("###############################");
print ("广播");
print ("###############################");
a = np.array([
    [1,2,3],
    [2,3,4],
    [12,13,14],
    [3,4,5]
]);
b = np.array([1,2,3]);
for i in range(4):
    a[i, :] += b
print a;


print a+np.tile(b,(4,1));

print a+b;











