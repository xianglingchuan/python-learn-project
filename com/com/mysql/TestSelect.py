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
print cursor.rowcount;
rs = cursor.fetchall();
for row in rs:
    #print row[0];
    #print row[1];
    print ("userId:%s, userName:%s") % row;





cursor.close();
conn.close();