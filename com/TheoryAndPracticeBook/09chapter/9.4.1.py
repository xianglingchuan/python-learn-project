# -*- coding: utf-8 -*-
# !/usr/bin/python
from jpype import *;


# 调用HanLP的java包，如下路径下载并解压c盘即可：
# 启动JVM，Linux需替换分号;为冒号:
#startJVM(getDefaultJVMPath(), "-Djava.class.path=/Users/xianglingchuan/Documents/work/pythonWork/learnProject/resource/jar/hanlp/hanlp-1.7.0.jar;/Users/xianglingchuan/Documents/work/pythonWork/learnProject/resource/jar/hanlp", "-Xms1g", "-Xmx1g")
startJVM(getDefaultJVMPath(),"-ea","-Djava.class.path=/Users/xianglingchuan/Documents/work/pythonWork/learnProject/resource/jar/hanlp/hanlp-1.7.0.jar;/Users/xianglingchuan/Documents/work/pythonWork/learnProject/resource/jar/hanlp")


#默认分词
paraStr1='中国科学院计算技术研究所的宗成庆教授正在教授自然语言处理课程'

print("="*30+"HanLP分词"+"="*30)
HanLP = JClass('com.hankcs.hanlp.HanLP');
print(HanLP.segment(paraStr1))

#一直报错误信息,无法测试成功
'''
Traceback (most recent call last):
  File "/Users/xianglingchuan/Documents/work/pythonWork/learnProject/com/TheoryAndPracticeBook/09chapter/9.4.1.py", line 16, in <module>
    HanLP = JClass('com.hankcs.hanlp.HanLP');
  File "/Users/xianglingchuan/software/Anaconda3/anaconda3/lib/python3.6/site-packages/jpype/_jclass.py", line 73, in JClass
    raise _RUNTIMEEXCEPTION.PYEXC("Class %s not found" % name)
jpype._jexception.RuntimeExceptionPyRaisable: java.lang.RuntimeException: Class com.hankcs.hanlp.HanLP not found

'''




