# -*- coding: utf-8 -*-
# !/usr/bin/python

print("============= 元组 ===============");
print("\n==== 操作元组 ====");
def calltuple(tuples):
    for r in tuples:
        print(r, end=" ");
calltuple(tuples=('刘备',"张飞",'关羽'));



print("============= 集合 ===============");
print("\n==== 操作元组 ====");
def callSet(basket):
    result = set(basket);
    print(result);
callSet(basket={'apple', 'orange', 'apple', 'pear', 'orange', 'banana'});

print("============= 字典 ===============");
print("\n==== 操作字典 ====");
def calldict(dicts):
    print ("原始字典:%s" % (dicts));
    dicts['欧阳修'] = '宋朝';
    print ("追加后的字典:%s" % (dicts));
    print ("字典键的集合:%s" % (list(dicts.keys())));
    print ("字典健排序:%s" % (sorted(dicts.keys())));
    print ("字典值的集合:%s" % (list(dicts.values())));
calldict(dicts={'李白':'唐朝', "杜甫":"唐朝"});



