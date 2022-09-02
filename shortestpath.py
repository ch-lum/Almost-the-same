import networkx as nx

SOURCE = 'edge'
TARGET = 'ymir'

G = nx.read_graphml('graphs and gephi\\fourwords.graphml')

print(nx.shortest_path(G, source=SOURCE, target=TARGET))