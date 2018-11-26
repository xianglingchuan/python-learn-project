#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TransferMoneyAccount(object):

     def __init__(self, dbUtil):
         self.dbUtil = dbUtil;
         self.course = self.dbUtil.getCursor()

     #转帐方法
     def transferMoney(self,sourceAccountId, targetAccountId, money):
         print "transferMoney...";
         try:
             #验证帐号是否合法
             #pass;
             self.checkAccount(sourceAccountId);
             self.checkAccount(targetAccountId);
             #验证帐号金额是否满足转出
             self.hasEnoughMoney(sourceAccountId, money);
             #减去帐号金额
             self.reduceMoney(sourceAccountId, money);
             #添加帐号金额
             self.addMoney(targetAccountId, money);
             self.dbUtil.conn.commit();

         except Exception as e:
             self.dbUtil.conn.rollback();
             raise e;

     # 验证帐号是否合法
     def checkAccount(self,accountId):
         try:
             sql = "select * from account where accountId=%s" % accountId;
             print "checkAccount sql:%s" % sql;
             self.course.execute(sql);
             rs = self.course.fetchall();
             if len(rs)!=1:
                 raise Exception("帐号%s不存在" % accountId);
         finally:
              pass;

     #验证帐号金额是否满足转出
     def hasEnoughMoney(self, accountId, money):
         try:
             sql = "select * from account where accountId=%s" % accountId;
             print "hasEnoughMoney sql:%s" % sql;
             self.course.execute(sql);
             rs = self.course.fetchone();
             accountMoney = rs[1];
             if(accountMoney < money):
                 raise Exception("帐号%s余额不足" % accountId);
         finally:
             pass;


     # 减去帐号金额
     def reduceMoney(self, accountId, money):
         try:
             pass;
             sql = "update account set money=money-%s where accountId=%s" % (money, accountId);
             print "reduceMoney sql:%s" % sql;
             self.course.execute(sql);
             if self.course.rowcount != 1:
                 raise Exception("减去金额，帐号%s金额失败" % accountId);
         finally:
             pass;


     # 添加帐号金额
     def addMoney(self, accountId, money):
         try:
             sql = "update account set money=money+%s where accountId=%s" % (money, accountId);
             print "addMoney sql:%s" % sql;
             self.course.execute(sql);
             if self.course.rowcount != 1:
                 raise Exception("添加金额, 帐号%s金额失败" % accountId);
         finally:
             pass;