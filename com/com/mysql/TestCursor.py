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
sql = "select * from user";


cursor.execute(sql);

print cursor.fetchone();
print cursor.fetchmany(3);
print cursor.fetchall();
print cursor.rowcount;

sqlCount = "select count(*) from user";
cursor.execute(sqlCount);
print cursor.fetchone();






cursor.close();
conn.close();