# -- coding: utf-8 --
# /usr/bin/python

import ConfigParser
import string, os, sys

roomPath = "../../../static/file/";
cf = ConfigParser.ConfigParser();
cf.read(roomPath+"config.ini");
#print cf;

#读取所有的section块
sections = cf.sections();
print sections;

#获取某一个section块的option
options = cf.options("userinfo");
print options;

#获取某一个section块的key=value数组
print cf.items("userinfo");

name = cf.get("userinfo","name");
pwd = cf.get("userinfo","pwd");
age = cf.getint("userinfo","age");
print "name:",name,"pwd:",pwd,"age:",age;


#设置某一个option值
cf.set("userinfo","pwd","123456");
cf.write(open(roomPath+"config.ini","w"));

#添加section块
# cf.add_section("wechat");
# cf.set("wechat","appid","123456");
# cf.set("wechat","appSecure","654321");
# cf.set("wechat","number",11);
# cf.write(open(roomPath+"config.ini","w"));


#移除section或option
# cf.remove_option("wechat","number");
# cf.remove_section("wechat");
# cf.write(open(roomPath+"config.ini","w"));



