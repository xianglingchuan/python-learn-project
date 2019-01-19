# -*- coding: utf-8 -*-
# !/usr/bin/python
import networkx as nx;

#创建有向图
g = nx.DiGraph();

#加条边 x->y
g.add_edge('X', 'Y');

#打印图的相关数据信息
print(nx.info(g), '\n');
print("Nodes:", g.nodes());
print("Edges:", g.edges());

#节点属性
print("X props:", g.node['X']);
print("Y props:", g.node['Y']);
#边属性
print("X=>Y props:", g['X']['Y']);
#更新节点信息
g.node['X'].update({"prop1" : "value1"});
print("X props:", g.node['X']);
#更新边信息
g['X']['Y'].update({"label":"label1"});
print("X=>Y props:", g['X']['Y']);

#有向图和无向图都可给边赋予权重，用到的方法是:add_weighted edges from;
g.add_weighted_edges_from([('X', 'Y', 10.0)]);
print(g.get_edge_data('X', 'Y'));






