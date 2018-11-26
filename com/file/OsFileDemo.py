# -- coding: utf-8 --
roomPath = "../../../static/file/";
'''
使用os模块打开文件
os.open(filename, flag, model): 打开文件
  flag: 打开文件方式
  os.O_CREAT: 创建文件
  os.O_RDONLY: 只读方式打开
  os.O_WRONLY: 只定方式打开
  os.O_RDWR: 读写方式打开


os.read(fd, buffersize); 读取文件
os.write(fd, string); 写入文件
os.lseek(fd, pos, how): 文件指针操作
os.close(fd): 关闭文件
'''
import  os;

#以创建和读写方式打开文件
file = os.open(roomPath+"os.txt", os.O_CREAT | os.O_RDWR);
#写入文件内容
os.write(file,"os.open(filename, flag, model)");
#重新设置文件指针位置到开始
print os.lseek(file,0,os.SEEK_SET);
#读取内容
print os.read(file,100);
#关闭文件
os.close(file);


'''
os模块方法介绍
access(path, mode)   判断该文件权限:F_OK存在，权限：R_OK,W_OK,X_OK
listdir(path)  返因当前目录下所有文件组成的列表
remove(path)  删除文件
rename(old, new) 修改文件或者目录名
mkdir(path,mode) 创建目录
makedirs(path, mode) 创建多级目录
removedirs(path) 删除多级目录
rmdir(path) 删除目录(目录必须空目录)
'''

print os.access("os.txt", os.F_OK);
print os.access("os.txt", os.R_OK);
print os.access("os.txt", os.W_OK);
print os.access("os.txt", os.X_OK);

print os.listdir(roomPath);
#print os.remove(roomPath+"1a.txt");
#print os.listdir(roomPath);
#print os.rename(roomPath+"1.txt", roomPath+"1-new.txt");
#os.mkdir(roomPath+"/test1");
#os.makedirs(roomPath+"/test2/test3/test4");
#os.rmdir(roomPath+"/test1");
#os.removedirs(roomPath+"/test2/test3/test4");



'''
os.path模块方法介绍
exists(path) 当前路径是否存在
isdir(s) 是否是一个目录
isfile(path) 是不是一个文件
getsize(filename) 返回文件大小
dirname(p) 返回路径目录
basename(p) 返回路径的文件名
'''
print os.path.exists(roomPath);
print os.path.isdir(roomPath);
print os.path.isfile(roomPath+"/read.txt");
print os.path.getsize(roomPath+"/read.txt");
print os.path.dirname(roomPath+"/write.txt");
print os.path.basename(roomPath+"/write.txt");













