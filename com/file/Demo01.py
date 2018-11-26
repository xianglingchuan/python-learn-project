# -*- coding: utf-8 -*-

roomPath = "../../../static/file/";
# fileObject = open(roomPath+"2.txt", 'w+');
# print type(fileObject);
# fileObject.write("i am is fileWrite");
# fileObject.close();
#
# fileObject = open(roomPath+"2.txt", 'r+');
# str = fileObject.read();
# print str;


print ("r 只读方式打开, 文件必须存在");
#fileObject = open(roomPath+"2new.txt", 'r');
fileObject = open(roomPath+"2.txt", 'r');
print (fileObject.read());
fileObject.close();

print ("\n\n============================");
print ("w 只写方式打开 文件不存在创建文件");
#打开新的文件
fileObject = open(roomPath+"writeNew.txt", 'w');
fileObject.close();

#打开已经存在内容的文件,内容会被清空掉
fileObject = open(roomPath+"2.txt", 'w');
#print "2.txt内容是---->",fileObject.read();
fileObject.close();

print ("\n\n============================");
print ("a 追加方式打开 文件不存在创建文件");
#fileObject = open(roomPath+"1.txt", "a");
#fileObject.write("test line2");


print ("\n\n============================");
print ("r+/w+ 读写方式打开");
fileObject = open(roomPath+"1.txt", "r+");
print (fileObject.read());
fileObject.write("test onlin3");
fileObject.close();

#如果存在文件将会先删除在创建新的
fileObject = open(roomPath+"1w.txt", "w+");
fileObject.write("test onlin3");
fileObject.close();



print ("\n\n============================");
print ("a+ 追加和读写方式打开");
fileObject = open(roomPath+"1a.txt", "a+");
fileObject.write("append file");
print (fileObject.read());
fileObject.close();
fileObject = open(roomPath+"1a.txt", "r+");
print (fileObject.read());


