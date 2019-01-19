# -*- coding: utf-8 -*-
# !/usr/bin/python

#可视化

from operator import itemgetter;
import networkx as nx;

import os
import json
from IPython.display import IFrame
from IPython.core.display import display
from networkx.readwrite import json_graph


from operator import itemgetter;
from github import Github;
import networkx as nx;
import sys;

ACCESS_TOKEN = '23777b727db037245ee9c9815775b3fe4c7e390c';
#USER = 'xianglingchuan';
#REPO = 'php-shopnc'
USER = 'minrk';
REPO ='findspark'
client = Github(ACCESS_TOKEN);
user = client.get_user(USER);
repo = user.get_repo(REPO);
stargazers = list(repo.get_stargazers()) #加星的用户集合
#print("=== 加星的用户集合 ===");
#print(stargazers);

#定义好变量g;
g = nx.DiGraph()
g.add_node(repo.name+'(repo)', type='repo', lang=repo.language, owner=user.login)
for sg in stargazers:
    g.add_node(sg.login+'(user)', type='user');
    g.add_edge(sg.login+'(user)', repo.name+"(repo)", type="gazes");




print("Stats on the full graph");
print(nx.info(g))
#只提取用户和语言节点from operator import itemgetter;
from github import Github;
import networkx as nx;
import sys;

ACCESS_TOKEN = '23777b727db037245ee9c9815775b3fe4c7e390c';
#USER = 'xianglingchuan';
#REPO = 'php-shopnc'
USER = 'minrk';
REPO ='findspark'
client = Github(ACCESS_TOKEN);
user = client.get_user(USER);
repo = user.get_repo(REPO);
stargazers = list(repo.get_stargazers()) #加星的用户集合
#print("=== 加星的用户集合 ===");
#print(stargazers);

#定义好变量g;
g = nx.DiGraph()
g.add_node(repo.name+'(repo)', type='repo', lang=repo.language, owner=user.login)
for sg in stargazers:
    g.add_node(sg.login+'(user)', type='user');
    g.add_edge(sg.login+'(user)', repo.name+"(repo)", type="gazes");
mtsw_users = [n for n in g if g.node[n]['type']=="user"] +[n for n in g if g.node[n]['type']=="lang"]


h = g.subgraph(mtsw_users);
print("Stats on the extracted subgraph");
print(nx.info(h))
#json导出
d = json_graph.node_link_data(h)
json.dump(d, open("force.json", 'w'))
viz_file = "files/force.html";
#D3可视化
display(IFrame(viz_file, '100%', '900px'));

