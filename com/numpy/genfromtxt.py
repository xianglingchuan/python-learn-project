# -*- coding: utf-8 -*-
# !/usr/bin/python

import csv
import numpy as np;


print("=== 案例一：温度传感器 (temperature sensor) 数据 ===");
#file_for_reading = open('thermistor.txt', 'r') # 'r' 意味着只读
#file_for_writing = open('thermistor.txt', 'w') # 'w' 是写入
#file_for_appending = open('thermistor.txt', 'a') # 'a' 是添加
#file_for_xxx.close() # 完成操作后要关闭文件

with open(r"thermistor.txt","rb") as f:
    reader = csv.reader(f,delimiter='\t')
    for row in reader:
        # 行号从1开始
        #print(reader.line_num, row);
        print(row);


    # print(type(reader));
    # print(list(reader));
    # print(reader.line_num, row)
    # for row in reader:
    #     print(row);
    # number=[]
    # time = []
    # data=[]
    # for row in reader:
    #     print(row);
    #     # number.append(row[0])
    #     # time.append(row[1])
    #     # data.append(float(row[2]))




