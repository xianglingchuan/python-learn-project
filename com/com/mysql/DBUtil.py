#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb;

class DBUtil(object):

    conn = None;

    cursor = None;

    def __init__(self, dbName):
        print "DBUtil __init__";
        self.dbName = dbName;
        self.createConnect();

    #创建数据库链接
    def createConnect(self):
        self.conn = MySQLdb.Connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd="111111",
            db="learn",
            charset="utf8",
        );

    def getCursor(self):
        print "DBUtil getCursor";
        if self.cursor == None:
            self.cursor = self.conn.cursor();
        return self.cursor;

    def __del__(self):
        print "DBUtil __del__";
        if self.cursor != None:
            self.cursor.close();
        if self.conn != None:
            self.conn.close();