# -- coding: utf-8 --
#from DBUtil import *;
from DBUtil import DBUtil;

sql = "select * from user";
dbUtil = DBUtil('learn');
cursor = dbUtil.getCursor();
cursor.execute(sql);
list = cursor.fetchall();
print list;




