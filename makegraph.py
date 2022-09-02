import networkx as nx
import json
import matplotlib.pyplot as plt

LETTERS = 3

FILE_NAME = "words dataset/scowl.json"

#Opens JSON file
with open(FILE_NAME) as f:
    #Return JSON data as dictionary
    allWords = json.load(f)

#Turn dictionary into array for some reason instead of list
arrayAllWords = list(allWords.keys())

#Called fourLetters but can be any size words
fourLetters = tuple([x for x in arrayAllWords if len(x) == LETTERS])

def all_but_one(start):
    #Start needs to have same amount of letters as LETTERS
    i = 0
    result = []
    copy = list(fourLetters)

    while i < LETTERS:
        after = start[(i+1):]
        before = start[:i]

        part = [x for x in copy if (x.endswith(after) and x.startswith(before))]
        result.extend(part)
        i += 1

    return result

G = nx.Graph()
G.add_nodes_from(fourLetters)

for word in fourLetters:
    edges = []
    similar = all_but_one(word)
    for child in similar:
        edges.append(tuple([word, child]))

    G.add_edges_from(edges)

#To .graphml file
nx.write_graphml(G, str(LETTERS) + 'words.graphml')