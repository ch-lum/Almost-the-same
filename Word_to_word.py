import json
import numpy as np
from anytree import Node, RenderTree, ZigZagGroupIter
from datetime import datetime
import networkx as nx
import matplotlib.pyplot as plt

#CONSTANTS
START = "road"
TARGET = "name"
ONE_ANSWER = False #I'd recommend only switching this to False if you are unhappy with the True results, takes much longer (10x) and more memory
GRAPH = True #Only matters if ONE_ANSWER = False

LETTERS = len(START)
FILE_NAME = 'scowl.json'

#Print Starting information
start = datetime.now()
start_time = start.strftime("%H:%M:%S")
print("Starting Time:", start_time)
print('going from ' + START + ' to ' + TARGET, '\n')


#Opens JSON file
with open(FILE_NAME) as f:
    #Return JSON data as dictionary
    allWords = json.load(f)

#Turn dictionary into array for some reason instead of list
arrayAllWords = np.array(list(allWords.keys()))

#Called fourLetters but can be any size words
fourLetters = tuple([x for x in arrayAllWords if len(x) == LETTERS])

#There is no way to tell if there's going to be no solution
def all_but_one(start, last = -1):
    #Start needs to have same amount of letters as LETTERS
    i = 0
    result = []
    copy = list(fourLetters)

    #Check if start is string or Node, if node do cooler things
    if type(start) == str:
        pass
    else:
        used = start.ancestors
        start = start.name
        try:
            copy.remove(start)
        except:
            pass
        #Only check for letters that weren't changed in the last iteration
        if len(used) != 0:
            last = [i for i in range(LETTERS) if used[-1].name[i] != start[i]][0]


    while i < LETTERS:
        if i == last:
            i += 1
            continue
        after = start[(i+1):]
        before = start[:i]

        part = [x for x in copy if (x.endswith(after) and x.startswith(before))]
        result.extend(part)
        i += 1

    return np.array(result)


#HERE IT GOES!
complete = False
root = Node(START)
first = True
count = 0
solutions = []

while (not complete) and count < 20:
    #Get all the nodes based on tier
    nodes = [[node for node in children] for children in ZigZagGroupIter(root)]

    print('iteration: ' + str(count))
    print('current number of tests: ' + str(len(nodes[-1])))    

    if first:
        first = False
        words = all_but_one(root)

        for x in words:
            Node(x, parent=root)
        
        count += 1
        continue

    for x in nodes[-1]:
        if TARGET == x.name:
            solution = [y.name for y in x.ancestors]
            solution.append(TARGET)
            complete = True
            if ONE_ANSWER:
                break
            else:
                solutions.append(solution)

        children = all_but_one(x)
        for y in children:
            Node(y, parent=x)
    
    
    count += 1
    
    #for pre, fill, node in RenderTree(root):
    #    print("%s%s" % (pre, node.name))

ending = datetime.now()
ending_time = ending.strftime("%H:%M:%S")
difference = ending - start
difference_seconds = difference.total_seconds()



print('\ntime completed:', ending_time, '\ntotal time:', difference_seconds, 'seconds\n')
if ONE_ANSWER:
    print('the shortest path found is ' + str(count) + ' long and is\n', solution)
else:
    print(len(solutions), 'solutions were found of length ' + str(count) + ':')
    for x in solutions:
        print(x)
    
    #Graph multiple solutions
    if GRAPH:

        G = nx.DiGraph()

        for x in solutions:
            G.add_nodes_from(x)
            tup = []
            for y in range(len(x)-1):
                tup.append(tuple([x[y], x[y+1]]))

            G.add_edges_from(tup)
        
        size = 1800 - count * 10
        nx.draw_networkx(G, node_size=size, node_color='white')

        plt.show()