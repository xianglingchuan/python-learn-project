class Book(object):

    def __init__(self, age):
        self.age = age;


    # 以下画线开头的不能直接方问的类属性，需要通过类提供的接口进行访问
    _age = 33;

    #特殊方法专用，不用轻意定义
    __sex__ = "boy";

    def getAge(self):
        return self._age;
        #return self._age;




