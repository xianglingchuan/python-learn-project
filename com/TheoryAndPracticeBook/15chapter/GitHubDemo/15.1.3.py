# -*- coding: utf-8 -*-
# !/usr/bin/python

#使用NetworkX构建兴趣图

from github import Github;
import networkx as nx;

ACCESS_TOKEN = '23777b727db037245ee9c9815775b3fe4c7e390c';
#USER = 'xianglingchuan';
#REPO = 'php-shopnc'
USER = 'minrk';
REPO ='findspark'
client = Github(ACCESS_TOKEN);
user = client.get_user(USER);
repo = user.get_repo(REPO);
stargazers = list(repo.get_stargazers()) #加星的用户集合
print("=== 加星的用户集合 ===");
print(stargazers);

g = nx.DiGraph()
g.add_node(repo.name+'(repo)', type='repo', lang=repo.language, owner=user.login)
for sg in stargazers:
    g.add_node(sg.login+'(user)', type='user');
    g.add_edge(sg.login+'(user)', repo.name+"(repo)", type="gazes");

print("=== 打印图的基本属性 ===");
print(nx.info(g), "\n");

print("=== 打印项目和用户点的基本属性 ===");
print(g.node['findspark(repo)'])
print(g.node['sandysnunes(user)'], '\n');


print("=== 打印这条边属性 ===");
print(g['sandysnunes(user)']['findspark(repo)'])

print("=== 打印起点为XXX的信息 ===");
print(g['sandysnunes(user)'])
print(g['findspark(repo)'])



print("=== 打印用户的出入度信息 ===");
print(g.in_edges(['sandysnunes(user)']));
print(g.out_edges(['sandysnunes(user)']));


print("=== 打印项目的出入度信息 ===");
print(g.in_edges(['findspark(repo)']))
print(g.out_edges(['findspark(repo)']))

