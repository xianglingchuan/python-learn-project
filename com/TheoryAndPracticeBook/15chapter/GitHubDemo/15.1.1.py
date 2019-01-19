# -*- coding: utf-8 -*-
# !/usr/bin/python
'''
Github自带API地址
  https://developer.github.com/v3/

创建API连接

pygithub

获取指定用户仓库
'''
from github import Github;
ACCESS_TOKEN = '23777b727db037245ee9c9815775b3fe4c7e390c';
USER = "xianglingchuan";
client = Github(ACCESS_TOKEN);
user = client.get_user(USER);
REPOS = user.get_repos();
print(list(REPOS));

