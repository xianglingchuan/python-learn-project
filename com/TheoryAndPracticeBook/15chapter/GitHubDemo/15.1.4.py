# -*- coding: utf-8 -*-
# !/usr/bin/python

#NetworkX部分统计指标
'''
度中心性(Degree Centrality)
中介中心性/中间中心性(Between Centrality)
接近中心性(Closeness Centrality)
'''
from operator import itemgetter;
import networkx as nx;
kkg = nx.generators.small.krackhardt_kite_graph()
print("Degree Centrality(度中心性)");
print(sorted(nx.degree_centrality(kkg).items(),
             key=itemgetter(1), reverse=True),'\n');
print("Betweenness Centrality(中介中心性/中间中心性)")
print(sorted(nx.betweenness_centrality(kkg).items(),
             key=itemgetter(1), reverse=True), '\n');
print("Closeness Centrality(接近中心性)");
print(sorted(nx.closeness_centrality(kkg).items(),
             key=itemgetter(1), reverse=True));



