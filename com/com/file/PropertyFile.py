# -- coding: utf-8 --
roomPath = "../../../static/file/";
# file = open(roomPath+"1.txt", "r");
# print file.fileno();
# print file.mode;
# print file.encoding;
# print file.closed;
# print file;

# Python标准文件
# 文件标准输入: sys.stdin
# 文件标准输出: sys.stdout
# 文件标准错误: sys.stderr;
import sys;

print "\nsys.stdin\n";
print "stdin---->",sys.stdin.fileno();
#sys.stdin.read(); #读入用户输入的内容
print "指针位置:%d, 读写模式是:%s" %(sys.stdin.fileno(),sys.stdin.mode);
inputStr = raw_input("请用户输入内容:");
print "输入内容是:",inputStr;
print "\n\n===================";


print "\nsys.stdout\n";
print "指针位置:%d, 读写模式是:%s" %(sys.stdout.fileno(),sys.stdout.mode);
print sys.stdout.write("直接输出到屏幕上....");
print "\n\n===================";


print "\nsys.stderr\n";
print "指针位置:%d, 读写模式是:%s" %(sys.stderr.fileno(),sys.stderr.mode);
print sys.stderr.write("error...");