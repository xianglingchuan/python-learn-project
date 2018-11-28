# -*- coding: utf-8 -*-
# !/usr/bin/python

print("============= List列表 ===============");
"""
list.append(x) 添加元素到列表尾部
list.extend(L) 列表合并
list.insert(i, x) 在指定位置插入一个元素
list.remove(x) 删除列表中值为x的第一个元素
list.pop([i])  从列表的指定位置删除元素,并将其返回
list.clear()  从列表中删除所有元素,相当于del a[:]
list.index(x) 返回列表中第一个值为x的元素索引
list.count(x) 返回x在列表中出现的次数
list.sort() 对列表中的元素就地进行排序
list.reverse() 就地倒排列表中的元素
list.copy() 返回列表的一个浅拷贝,等同于 a[:]
"""
print("\n==== 列表的切分 ====");
def callList(names):
    print (names[-1:]); #输出列表最后一个元素
    print (names[:3]); #输出列表前三个元素
callList(names=["this", "is", "a", "list"]);

print("\n==== 列表作堆栈(先进先出) ====");
def SomeList(stack):
    print ("原始列表(栈):%s" % (stack));
    stack.append("马超");
    stack.append("孙权");
    print("追加后列表(栈):%s" % (stack));
    stack.pop();
    stack.pop();
    print("出栈后的数据:%s" % (stack));
SomeList(stack=['刘备',"张飞",'关羽']);



print("\n==== 列表作队列(先进后出) ====");
#把列表当做队列使用，使用队列时调用collections.deque,它为在首尾两端快速插入和删除而设计
from collections import deque;
def SomeList2(queue):
    print ("原始列表:%s" % (queue));
    queue.append("马超");
    queue.append("孙权");
    print("追加后列表:%s" % (queue));
    #stack.pop();
    #stack.pop();
    queue.popleft();
    queue.popleft();
    print("出列后的数据:%s" % (queue));
SomeList2(queue=deque(['刘备',"张飞",'关羽']));

print("\n==== 列表推导式 ====");
def callList(nums):
    squares = [n**2 for n in nums];
    print(squares);
callList(nums=[2,4,6,8])

print("\n==== 列表的矩阵转秩 ====");
def countList(matrix):
    result = [[row[i] for row in matrix] for i in range(4)]
    print(result);
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
];
countList(matrix);

