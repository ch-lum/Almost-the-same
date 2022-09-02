from re import A
import networkx as nx
import matplotlib.pyplot as plt

l1 = ['a', 'b', 'c', 'd']
l2 = ['a', 'b', 'e', 'd']

megalist = [l1,l2]

G = nx.Graph()

for x in megalist:
    G.add_nodes_from(x)
    tup = []
    for i in range(len(x)-1):
        tup.append(tuple([x[i], x[i+1]]))

    G.add_edges_from(tup)

nx.draw(G)



plt.show()