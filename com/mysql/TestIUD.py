# -- coding: utf-8 --
import MySQLdb;

conn = MySQLdb.Connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    passwd = "111111",
    db = "learn",
    charset = "utf8",
    );
cursor = conn.cursor();

#测试正常操作
'''
insertSql = "insert into user(userId, userName) VALUE (10, 'user10')";
updateSql = "update user set userName='user99' where userId=9 ";
delteSql = "delete from user where userId < 3";

cursor.execute(insertSql);
print "insert number: ",cursor.rowcount;
cursor.execute(updateSql);
print "update number: ",cursor.rowcount;
cursor.execute(delteSql);
print "delete number: ",cursor.rowcount;
conn.commit();
'''

#测试使用事务回滚
insertSql = "insert into user(userId, userName) VALUE (10, 'user10')";
updateSql = "update user set userName='user99' where userId=9 ";
delteSql = "delete from user where userd < 3";

try:
    cursor.execute(insertSql);
    print "insert number: ", cursor.rowcount;
    cursor.execute(updateSql);
    print "update number: ", cursor.rowcount;
    cursor.execute(delteSql);
    print "delete number: ", cursor.rowcount;
    conn.commit();
except Exception as e:
    print e;
    conn.rollback();

cursor.close();
conn.close();