# -*- coding: utf-8 -*-
# !/usr/bin/python

#构建 GitHub的兴趣图

'''
度中心性(Degree Centrality)
中介中心性/中间中心性(Between Centrality)
接近中心性(Closeness Centrality)
'''
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
print("=== 加星的用户集合 ===");
print(stargazers);




#定义好变量g;
g = nx.DiGraph()
g.add_node(repo.name+'(repo)', type='repo', lang=repo.language, owner=user.login)
for sg in stargazers:
    g.add_node(sg.login+'(user)', type='user');
    g.add_edge(sg.login+'(user)', repo.name+"(repo)", type="gazes");



for i, sg in enumerate(stargazers):
    #增加关注联系，如果有关注者的话
    print("i====>",i);
    if(i<=9): #总数有243,由于访问原因，只循环前10
        try:
            for follower in sg.get_followers():
                print(follower);
                if follower.login + '(user)' in g:
                    print("follower.login======>",follower.login);
                    g.add_edge(follower.login+'(user)', sg.login+"(user)", type='follows')
        except Exception: #ssl.SSLError
            sys.stderr.write("Encountered an error fetching folowers for", sg.login, "Skpiiing");
            print("Processed", i+1, " stargazers. Num nodes/edges in graph", g.number_of_nodes(), "/", g.number_of_nodes());

# print("Rate limit remaining", client.rate_limiting);
#
#
# #接下来，对关联关系进行统计
# from operator import itemgetter;
# from collections import Counter;
#
# #显示更新的图信息
# print(nx.info(g), '\n');
#
#
# #每个打星用户的关注者数量不同
# #print(    len([e for e in g.edges_iter(data=True) if e[2]['type'] == 'follows']), '\n');
# print(len([e for e in g.edges(data=True) if e[2]['type'] == 'follows']), '\n');
#
#
# #查看某个打星用户有多少关注者
# # print(len([e
# #            for e in e.edges_iter(data=True)
# #                if e[2]['type']=='follows' and e[1]=='freeman-lab(user)']), '\n')
#
#
# #打印最多的前10个节点
# print("==== 打印最多的前10个节点 ====");
# #print(list(sorted([n for n in g.edges_iter()], key=itemgetter(1), reverse=True)[:10]), '\n');
# print(list(sorted([n for n in g.edges()], key=itemgetter(1), reverse=True)[:10]), '\n');
#
#
# #对每个打星用户的关注者数目计数
# print("==== 对每个打星用户的关注者数目计数 ====")
# #c = Counter([e[1] for e in g.edges_iter(data=True) if e[2]['type']=='follows']);
# c = Counter([e[1] for e in g.edges(data=True) if e[2]['type']=='follows']);
#
# popular_users = [(u, f) for (u, f) in c.most_common() if f >0];
# print("受欢迎用户数量: ", len(popular_users));
# print("前流行的用户:", popular_users[:10]);



h = g.copy()
#移除中心节点
h.remove_node('findspark(repo)');

dc = sorted(nx.degree_centrality(h).items(),
            key=itemgetter(1), reverse=True);
print("Degree Centrality(度中心性)");
print(dc[:10], '\n');
#[('rgbkrk(user)', 0.041152263374485604), ('stared(user)', 0.02880658436213992), ('esafak(user)', 0.02469135802469136), ('freeman-lab(user)', 0.02469135802469136), ('nfultz(user)', 0.02469135802469136), ('fly51fly(user)', 0.01234567901234568), ('gauravssnl(user)', 0.01234567901234568), ('rholder(user)', 0.00823045267489712), ('he0x(user)', 0.00823045267489712), ('ryan-williams(user)', 0.00823045267489712)]



bc = sorted(nx.betweenness_centrality(h).items(),
            key=itemgetter(1), reverse=True);
print("Betweenness Centrality(中介中心性/中间中心性)");
print(bc[:10], '\n');
#[('rgbkrk(user)', 0.00034010135020236026), ('esafak(user)', 0.00017005067510118013), ('ryan-williams(user)', 1.7005067510118014e-05), ('pchalasani(user)', 0.0), ('rdhyee(user)', 0.0), ('rholder(user)', 0.0), ('freeman-lab(user)', 0.0), ('he0x(user)', 0.0), ('cbouey(user)', 0.0), ('stared(user)', 0.0)]

print("closeness Centrality(接近中心性)");
cc = sorted(nx.closeness_centrality(h).items(),
            key=itemgetter(1), reverse = True);
print(cc[:10])
#[('freeman-lab(user)', 0.03632751525471832), ('rgbkrk(user)', 0.035567313345091126), ('stared(user)', 0.029263831732967538), ('rdhyee(user)', 0.022792022792022793), ('esafak(user)', 0.01646090534979424), ('rholder(user)', 0.00823045267489712), ('he0x(user)', 0.00823045267489712), ('pchalasani(user)', 0.00411522633744856), ('ryan-williams(user)', 0.00411522633744856), ('cbouey(user)', 0.0)]





