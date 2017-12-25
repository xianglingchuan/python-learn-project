# -- coding: utf-8 --

roomPath = "../../../static/file/";


print ("文件指针操作练习");
# file = open(roomPath+"pointer.txt", "w+");
# file.write("0123456789abcdefg");


import  os;
file = open(roomPath+"pointer.txt", "r+");

print "当前指针位置:",file.tell();
print file.read(3);
print "当前指针位置:",file.tell();

file.seek(0,os.SEEK_SET);
print "当前指针位置:",file.tell();
print file.read(3);

file.seek(0,os.SEEK_END);
print "指针指向结尾的值是:",file.tell();
#从结尾向前移动5个位置
file.seek(-5,os.SEEK_CUR);
print file.read();
print file.tell();


#将我们的文件指针位置指向文件的的长度之外
#这里没有像教程一样报错，但是读取内容是空的
file.seek(20, os.SEEK_END);
print file.tell();
print "读取的内容是:",file.read();
