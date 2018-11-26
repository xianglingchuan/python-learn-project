# -*- coding: utf-8 -*-
#!/usr/bin/python
import json
import os;
import shutil;

print ("+++++++++++++++++++++++++++++")
print ("文件移动")
print ("+++++++++++++++++++++++++++++")


#############################
#复制文件到指定的目录下
def copyFiles(sourceDir, targetDir, filename):
    #oldFileName=filename
    path,sfileName = os.path.split(filename)
    #print "sfileName--->",sfileName;
    #print "path--->", path;
    # #cp $sourceFile $targetFile
    sourceDir=sourceDir+filename
    targetDir=targetDir+sfileName
    #shutil.copyfile(sourceDir,targetDir);
    print ("copy %s -> %s\n" % (sourceDir, targetDir))


#############################
#解析json文件
def loadFont(fileName):
    f = open(fileName)  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    lists = json.load(f)
    return lists

def execute():
    basePath="/Users/xianglingchuan/Documents/work/pythonWork/learnProject/com/com/fileCopy/";
    #basePath="/chroot/data/fileCopy/";
    lists = loadFont(basePath+"files.json")
    for item in lists:
        path = item['path']
        #print(path)
        targetDir=basePath+"data/"
        sourceDir="/chroot/www/bank_music/rabbit/www/Upload/Audio/"
        copyFiles(sourceDir, targetDir, path);

if __name__=='__main__':
    execute()
    print("执行完成.");