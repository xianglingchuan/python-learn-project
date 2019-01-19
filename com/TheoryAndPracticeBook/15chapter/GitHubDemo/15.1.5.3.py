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
#print("=== 加星的用户集合 ===");
#print(stargazers);

#定义好变量g;
g = nx.DiGraph()
g.add_node(repo.name+'(repo)', type='repo', lang=repo.language, owner=user.login)
for sg in stargazers:
    g.add_node(sg.login+'(user)', type='user');
    g.add_edge(sg.login+'(user)', repo.name+"(repo)", type="gazes");


#找出活跃项目
MAX_REPOS = 500;
for i, sg in enumerate(stargazers):
    print(sg.login);
    if (i <= 9):  # 总数有243,由于访问原因，只循环前10
        try:
            for starred in sg.get_starred()[:MAX_REPOS]: #Slice to avoid supernodes
                g.add_node(starred.name + "(repo)", type="repo", lang=starred.language,
                owner=starred.owner.login);
                g.add_edge(sg.login+"(user)", starred.name+'(repo)', type='gazes');
        except Exception: #ssl.SSLError:
            print("Encountered an error fetching starred repos for", sg.login, "Skipping.")
            print("Processed", i+1, "stargazers' starred repos");
            print("Num nodes/edges in graph", g.number_of_nodes(), "/", g.number_of_edges());
            print("Rate limit", client.rate_limiting);

print(nx.info(g), '\n');
#获取图里面所有项目构成列表
repos = [n for n in g.nodes() if g.node[n]['type'] == 'repo']
#关注最多的前10个项目
print("==== 关注最多的前10个项目 ====");
print("Popular repositories");
print(sorted([(n, d)
              for(n, d) in g.in_degree()
                  if g.node[n]['type']=='repo'],
              key=itemgetter(1), reverse=True)[:10])

print("Respositories that luzhijun has bookmarked");
print([(n, g.node[n]['lang'])
       for n in g['luzhijun(user)']
           if g['luzhijun(user)'][n]['type'] == "gazes"])

#用户喜爱的程序语言
print("==== 用户喜爱的程序语言 ====");
print("Propramming languages luzhijun is interested in");
print(list(set([g.node[n]['lang']
                for n in g['luzhijun(user)']
                if g['luzhijun(user)'][n]['type']=="gazes"])))


print("Propramming languages xianglingchuan is interested in");
print(list(set([g.node[n]['lang']
                for n in g['xianglingchuan(user)']
                if g['xianglingchuan(user)'][n]['type']=="gazes"])))



#查看关注项目最多的用户(超过MAX_REPOS)
print("==== 查看关注项目最多的用户(超过MAX_REPOS) ====");
print("Supernode candidates")
print(sorted([(n, len(g.out_edges(n)))
              for n in g.nodes()
                 if g.node[n]['type']=='user' and len(g.out_edges(n)) > MAX_REPOS],
             key=itemgetter(1), reverse=True));


#找出热门语言
print("==== 找出热门语言 ====");
repos = [n
         for n in g.nodes()
             if g.node[n]['type'] == 'repo']
for repo in repos:
    #清除None，有此空项目语言为None
    lang = (g.node[repo]['lang'] or "") + "(lang)"
    #加星于repo的用户
    stargazers = [u
        for (u, r, d) in g.in_edges(repo, data=True)
                  if d['type'] == 'gazes'
    ]
    for sg in stargazers:
        g.add_node(lang, type='lang')
        g.add_edge(sg, lang, type='programes')
        g.add_edge(lang, repo, type='implements')


#接下来看一下对语言的统计信息
print(nx.info(g), '\n');
#显示图里有什么语言
print([n
       for n in g.nodes()
       if g.node[n]['type']=='lang'])
#某个用户使用的语言
print([n
       for n in g['ocanbascil(user)']
       if g['ocanbascil(user)'][n]['type']=='programs'], '\n')


#查询最热门的语言
print("Most popular languages")
print(sorted([(n, g.in_degree(n))
    for n in g.nodes()
        if g.node[n]['type']=='lang'], key=itemgetter(1), reverse=True)[:10])



#查询用某种语言的有多少人
python_programmers = [
        u for (u, l) in g.in_edges('Python(lang)')
             if g.node[u]['type'] == 'user']
print("Number of Python programmers:", len(python_programmers));


javascript_programmers =[
             u for (u, l) in g.in_edges('JavaScript(lang)')
                 if g.node[u]['type'] == 'user']
print("Number of JavaScription programmers:", len(javascript_programmers));


#两个语言都用的人
print("Number of programmers who use JavaScription and Python");
print(len(set(javascript_programmers).intersection(set(python_programmers)) ));

#只用python不用JS的人
print("Number of programmers who use JavaScription but not Python");
print(len(set(javascript_programmers).difference(set(python_programmers))))

