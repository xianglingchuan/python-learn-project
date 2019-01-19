import networkx as nx;

G = nx.MultiGraph()
G.add_path([0,1,2,3])
print([e for e in G.edges()])