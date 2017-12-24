#!/usr/bin/env python
# -*- coding: utf-8 -*-
from TransferMoneyAccount import *;
from DBUtil import *;

sourceAccountId = 1; #转帐帐号ID
targetAccountId = 2; #转向帐号ID
money = 222;  #转帐金额

dbUtil = DBUtil("learn");
transfer = TransferMoneyAccount(dbUtil);
try:
    transfer.transferMoney(sourceAccountId,targetAccountId,money);
except Exception as e:
    print e;


