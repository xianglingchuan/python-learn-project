# -- coding: utf-8 --
'''
  read([size]): 读取文件(读取size个字节，默认读取全部)
  readline([size]): 读取一行
  readlines([size]): 读取完文件，返回每一行所组成的列表
  iter: 使用迭代器读取文件
'''
roomPath = "../../../static/file/";
#print ("read([size]): 读取文件(读取size个字节，默认读取全部)");
#file = open(roomPath+"read.txt", 'r+');
#读取全部内容
#print file.read();

#读取指定字节数内容
#print file.read(10);


print ("readline([size]): 读取一行");
#默认读取一行数据
#print file.readline();

#这里的size也是表示字符长度的意思，表示读取一行中的字符长度
#print  file.readline(100);


print ("readlines([size]): 读取完文件，返回每一行所组成的列表");

import  io;
#读取当前缓存内容的大小
print io.DEFAULT_BUFFER_SIZE;
#readlines只能读取指定缓存大小左右的内容

# bigfile = open(roomPath+"bigfile.txt", "w+");
# i = 0;
# while(i<10000000):
#     bigfile.write("www.python.org=="+str(i)+"\n");
#     i+=1;



#不知道是不是版本原因，还是其它的，我这里可以读取到全部1000行内容
# bigfile = open(roomPath+"bigfile.txt", "r+");
# lines = bigfile.readlines();
# print "读取的总行数是:",len(lines);
# print lines;


# bigfile = open(roomPath+"bigfileNew.txt", "w+");
# i = 0;
# while(i<1000):
#     bigfile.write("www.python.org=="+str(i)+"\n");
#     i+=1;
#迭代器读取文件内容
# bigfile = open(roomPath+"bigfileNew.txt", "r+");
# fileIter = iter(bigfile);
# line = 0;
# for iter in fileIter:
#     line +=1;
#     print "第"+str(line)+"行:"+iter;
# print line;












