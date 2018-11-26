# -- coding: utf-8 --

roomPath = "../../../static/file/";

# file = open(roomPath+"write.txt",'w');
# file.write("111111\n");
#
# file.writelines("222222\n");
#
# file.writelines(("1\n","2\n","3\n","4\n"));
#
# line = ["A\n",'B\n','C\n','D\n'];
# file.writelines(line);


#文件打开次数的系统限制
# for i in range(1024):
#     f = open(roomPath+"write.txt", 'w');
#     print "%d : %d" % (i, f.fileno());


listf = [];
#4932，mac上系统最多打开文件数是4932
for i in range(1020):
    listf.append(open(roomPath+"write.txt", "w"));
    print ("%d : %d " % (i, listf[i].fileno()));

